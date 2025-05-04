import rospy

from geometry_msgs.msg import PoseStamped
from cv_bridge import CvBridge
import tf

import numpy as np
import cv2
import time

from reproj import SFM, FRAME, p2w_w2p_once, calc_circle

class circle_gt():
    def __init__(self):
        self.poses_gt = []

    def circle_pos_callback(self, circle_pos):
        self.poses_gt = circle_pos.poses
            
class odometry_class():
    def __init__(self):
        self.q = np.float32([0, 0, 0, 1])
        self.R = tf.transformations.quaternion_matrix(self.q)[0:3, 0:3]
        # self.rmatrix = np.float32([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        self.rmatrix = np.float32([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.pos = np.float32([0, 0, 0])
        # self.vel = np.float32([0, 0, 0])
        
    # Vins 订阅版本
    # def odom_callback(self, odom):
    #     curq = np.float32([odom.pose.pose.orientation.x, odom.pose.pose.orientation.y, odom.pose.pose.orientation.z, odom.pose.pose.orientation.w])
    #     r1m = tf.transformations.quaternion_matrix(curq)
    #     R_ = self.rmatrix.dot(r1m)
    #     self.q = tf.transformations.quaternion_from_matrix(R_)
    #     self.R = R_[0:3, 0:3]
    #     self.pos = np.float32([odom.pose.pose.position.x, -odom.pose.pose.position.y, -odom.pose.pose.position.z])
    #     self.vel = np.float32([odom.twist.twist.linear.x, -odom.twist.twist.linear.y, -odom.twist.twist.linear.z])
    
    def odom_callback(self, odom):
        curq = np.float32([odom.pose.orientation.x, odom.pose.orientation.y, odom.pose.orientation.z, odom.pose.orientation.w])
        r1m = tf.transformations.quaternion_matrix(curq)
        R_ = self.rmatrix.dot(r1m)
        self.q = tf.transformations.quaternion_from_matrix(R_)
        self.R = R_[0:3, 0:3]

        self.pos = np.float32([odom.pose.position.x, odom.pose.position.y, odom.pose.position.z])
        
class images_class():
    def __init__(self, odom, prefix):
        self.images = []
        self.bridge = CvBridge()
        self.prefix = prefix
        self.count = 0
        self.odom = odom
        
    def image_callback(self, image):
        self.img = self.bridge.imgmsg_to_cv2(image, desired_encoding='bgr8')
        self.count+=1
        self.images.append([self.count, time.time(), self.img, self.odom.R, self.odom.pos])
        #np.savez(self.prefix + '/yy/images_picture/sfm3_data/{}.npz'.format(self.count), img = self.img, R = self.odom.R, pos = self.odom.pos)

def target2msg(target):
    msg = PoseStamped() # 创建 msg 对象
    msg.header.stamp= rospy.Time.now()
    msg.pose.position.x = target[0]
    msg.pose.position.y = target[1]
    msg.pose.position.z = target[2]
    msg.pose.orientation.x = target[3]
    return msg

def check_ellp(frame, sfm, thresh = 0.5):
    origin_ellp = np.float32(frame.ellp[0]).reshape([1, 2])
    wt = frame.p2w_v2(sfm, origin_ellp)
    if np.linalg.norm(sfm.origin - wt) > thresh:
        print("check[c,oellp,wt,occ]:", origin_ellp, wt, sfm.origin)
        return False
    else:
        return True
    
def calc_res(frame, sfm, circle):
    _, _, pix = frame.w2p(sfm, circle)
    diff = frame.cnt - pix
    return np.sum(np.sqrt(np.sum(diff * diff, axis = 1)))

def angle_vec(vec1, vec2):
    norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cost = np.dot(vec1, vec2) / norm
    vec = np.cross(vec1, vec2)
    vec = vec / np.linalg.norm(vec)
    angle = np.arccos(cost)
    angle_ = angle * 180.0 / np.pi
    if angle_ < 1 or angle_ > 179:
        return np.float32([0, 0, 1]), 0.0
    return vec, angle

def calc_yaw(sfm, pos):
    tp = sfm.origin[0] - pos
    tp[2] = 0
    vec, yaw = angle_vec(np.float32([1, 0, 0]), tp)
    if vec[2] < 0: yaw = -yaw
    return yaw

def calc_Dpt(sfm, pos):
    D_cur = -sfm.origin.dot(sfm.ABC)
    return D_cur, (pos.dot(sfm.ABC) + D_cur) / np.linalg.norm(sfm.ABC)

from reproj import calc_wps
class reference_path():
    def __init__(self, cgt, odom, left, right, img2binary, scale):
        self.cgt = cgt
        self.odom = odom
        self.left = left
        self.right = right
        self.last_info = []
        self.last_left_index = 0
        self.img2binary = img2binary
        self.scale = scale
        self.REC_MIN = 10
        self.count_circle = 0
        
    def start_new_circle(self, circle_id):
        self.circle_id = circle_id
        self.is_crossed = False
        self.D_pt = 10.0
        if circle_id != 0:
            self.last_info = [self.circle_target, self.sfm, self.left.images]
            self.left.images = []
        
        self.last_left_index = 0
        self.count_circle = 0
        self.no_rec = 0
        
        circle_info = self.cgt.poses_gt[self.circle_id]
        self.circle_target = np.float64([circle_info.position.x, circle_info.position.y, circle_info.position.z, circle_info.yaw / 180 * np.pi])
        origin, yaw, vec = self.circle_target[0:3].reshape([1, -1]), self.circle_target[3], np.float32([0, 0, 1])
        self.sfm = SFM(origin.copy(), vec.copy(), yaw)
        self.cur_sfm = SFM(origin.copy(), vec.copy(), yaw)
        self.cur_frame = None
        self.sfm_init_flag = True
        self.wps = None
        self.wp_finished = False

        self.cross_starting_time = time.time()

        self.real_target = self.circle_target.copy()
        dx = self.real_target[0] - self.odom.pos[0]
        self.direction = dx / np.abs(dx)

        if circle_id == 0:
            self.cur_target = self.real_target.copy()
            self.cur_target[0:2] = 0.5 * (self.odom.pos[0:2] + self.real_target[0:2])
            self.cur_target[2] = self.real_target[2]
        else:
            self.cur_target[3] = self.real_target[3]
            self.cur_target[0:2] = 0.5 * (self.odom.pos[0:2] + self.real_target[0:2])
            self.cur_target[2] = self.real_target[2]
        self.cur_target[3] = calc_yaw(self.sfm, self.cur_target[0:3])
        
    def update_sfm(self, update_thresh = 5.0):
        #print("usfm", self.left.count, self.sfm.origin, self.sfm_init_flag, self.count_circle)
        left_index = len(self.left.images)
        cur_time = time.time()
        for idx in range(self.last_left_index, left_index):
            if not self.is_crossed:
                self.is_crossed = self.crossed(self.odom.R, self.odom.pos)
            count, time_img, img, R, pos = self.left.images[idx]
            if cur_time - time_img > 0.3:
                continue
            binary = self.img2binary(img)
            frame = FRAME(img, binary, R, pos, scale = self.scale, thresh = 25.0)

            if self.is_crossed: return
            if frame.ch == -1 or (self.count_circle > self.REC_MIN and self.sfm_init_flag and not check_ellp(frame, self.sfm)):
                self.cur_frame = None
                self.no_rec += 1
                continue
            if self.no_rec > 30:
                if self.count_circle < 20:
                    self.count_circle = 0
                self.cur_sfm = SFM(self.sfm.origin.copy(), self.sfm.vec.copy(), self.sfm.yaw)
            self.no_rec = 0
            self.count_circle += 1
            #if self.circle_id == 2:
            #    print('sfm', self.count_circle, idx, count, self.cur_sfm.origin, self.cur_sfm.yaw)
            wt = frame.p2w_v2(self.cur_sfm, frame.cnt)
            wt = p2w_w2p_once(self.cur_sfm, frame, wt)
            origin_, vec_, yaw_, theta, radius = calc_circle(wt)
            self.cur_sfm = SFM(origin_, vec_, yaw_)
            #if self.circle_id == 2:
            #    print('sfm after', self.count_circle, idx, count, self.cur_sfm.origin, self.cur_sfm.yaw)
            self.cur_frame = frame
        if np.linalg.norm(self.cur_sfm.origin - self.sfm.origin) < update_thresh:
            if self.count_circle > self.REC_MIN:
                self.sfm = SFM(self.cur_sfm.origin.copy(), self.cur_sfm.vec.copy(), self.cur_sfm.yaw)
                self.sfm_init_flag = False
        else:
            print("update_sfm cur:", count, self.cur_sfm.origin, round(self.cur_sfm.yaw, 3))
            print("update_sfm last:", count, self.sfm.origin, round(self.sfm.yaw, 3))
            self.cur_sfm = SFM(self.sfm.origin.copy(), self.sfm.vec.copy(), self.sfm.yaw)
        self.last_left_index = left_index

    def calc_target(self):
        origin_, yaw_ = self.sfm.origin, self.sfm.yaw
        target_ = np.float32([origin_[0, 0], origin_[0, 1], origin_[0, 2], yaw_])
        target_[0:3] = 0.3 * target_[0:3] + 0.7 * self.real_target[0:3]
        self.real_target[0:3] = target_[0:3]
        self.cur_target[0:2] = 0.5 * (self.odom.pos[0:2] + self.real_target[0:2])
        if self.sfm_init_flag:
            self.cur_target[2] = target_[2] - 1.0
            self.cur_target[3] = calc_yaw(self.sfm, self.cur_target[0:3])
        else:
            self.cur_target[2] = 0.5 * (target_[2] + self.odom.pos[2])
            self.cur_target[3] = calc_yaw(self.sfm, self.cur_target[0:3])
            pos = self.odom.pos
            vec = self.sfm.origin[0] - pos
            norm = np.linalg.norm(vec)
            if norm > 2.0: return
            yaw = calc_yaw(self.sfm, pos)
            if norm < 0.3:
                self.is_crossed  = True
                if norm < 0.1:
                    self.cur_target[0:3] = self.sfm.origin[0]
                    self.cur_target[0] += 3.0
                    self.cur_target[3] = 0    
            self.cur_target[0:3] = pos + vec / norm * 3.0
            self.cur_target[3] = yaw
        
    def crossed(self, R, pos, thresh_pt2plane = 0.5, thresh_time = 2.5):
        D_cur, D_pt = calc_Dpt(self.sfm, pos)
        flag1 = self.count_circle > self.REC_MIN
        flag2 = np.abs(D_pt) < thresh_pt2plane
        flag3 = time.time() - self.cross_starting_time > thresh_time
        flag4 = np.linalg.norm(pos - self.sfm.origin[0]) < thresh_pt2plane
        self.D_pt = D_pt
        
        #print("crossed", flag1, flag2, flag3, D_cur, D_pt)
        return flag1 and flag2 and flag3 and flag4
    


