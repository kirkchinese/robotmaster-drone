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
        # 存储来自ground truth的圆的位置
        self.poses_gt = []

    def circle_pos_callback(self, circle_pos):
        # 接收来自ground truth的圆的位置并存储
        self.poses_gt = circle_pos.poses
            
class odometry_class():
    def __init__(self):
        # 初始化四元数和旋转矩阵
        self.q = np.float32([0, 0, 0, 1])
        self.R = tf.transformations.quaternion_matrix(self.q)[0:3, 0:3]
        # 定义旋转矩阵,将相机坐标系转换到世界坐标系
        self.rmatrix = np.float32([[1, 0, 0, 0], 
                                    [0, 1, 0, 0], 
                                    [0, 0, 1, 0], 
                                    [0, 0, 0, 1]])
        # 初始化位置
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
        # 接收里程计数据并更新四元数和位置
        curq = np.float32([odom.pose.orientation.x, odom.pose.orientation.y, odom.pose.orientation.z, odom.pose.orientation.w])
        r1m = tf.transformations.quaternion_matrix(curq)
        R_ = self.rmatrix.dot(r1m)
        self.q = tf.transformations.quaternion_from_matrix(R_)
        self.R = R_[0:3, 0:3]

        self.pos = np.float32([odom.pose.position.x, odom.pose.position.y, odom.pose.position.z])
        
class images_class():
    def __init__(self, odom, prefix):
        # 存储图像信息
        self.images = []
        # 初始化CVBridge
        self.bridge = CvBridge()
        # 存储前缀以便保存图像
        self.prefix = prefix
        # 计数器以跟踪图像的数量
        self.count = 0
        # 存储里程计数据以便与图像数据相关联
        self.odom = odom
        
    def image_callback(self, image):
        # 接收来自相机的图像数据并存储
        self.img = self.bridge.imgmsg_to_cv2(image, desired_encoding='bgr8')
        self.count+=1
        self.images.append([self.count, time.time(), self.img, self.odom.R, self.odom.pos])
        # 保存图像数据
        #np.savez(self.prefix + '/yy/images_picture/sfm3_data/{}.npz'.format(self.count), img = self.img, R = self.odom.R, pos = self.odom.pos)   #     npz的来源 npz格式是一种压缩格式,可以存储多个数组,并且可以方便地读取和写入。np.savez函数可以将多个数组保存到一个npz文件中,npz文件的扩展名是.npz。npz文件中的数组可以通过索引或者键名来访问。

def target2msg(target):
    # 将目标转换为PoseStamped消息
    msg = PoseStamped() # 创建 msg 对象
    msg.header.stamp= rospy.Time.now()# 记录时间
    msg.pose.position.x = target[0] # 赋值 
    msg.pose.position.y = target[1]
    msg.pose.position.z = target[2]
    msg.pose.orientation.x = target[3]
    return msg

def check_ellp(frame, sfm, thresh = 0.5):
    # 检查帧中检测到的椭圆是否在模型中的预期位置上
    origin_ellp = np.float32(frame.ellp[0]).reshape([1, 2])
    wt = frame.p2w_v2(sfm, origin_ellp)
    if np.linalg.norm(sfm.origin - wt) > thresh:
        # print("check[c,oellp,wt,occ]:", origin_ellp, wt, sfm.origin)
        return False
    else:
        return True
    
def calc_res(frame, sfm, circle):
    # 计算帧中检测到的椭圆与模型的预期位置之间的残差
    _, _, pix = frame.w2p(sfm, circle)
    diff = frame.cnt - pix
    return np.sum(np.sqrt(np.sum(diff * diff, axis = 1)))

def angle_vec(vec1, vec2):
    # 计算两个向量之间的夹角和法向量
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
    # 计算相机相对于模型的偏航角
    tp = sfm.origin[0] - pos
    tp[2] = 0
    vec, yaw = angle_vec(np.float32([1, 0, 0]), tp)
    if vec[2] < 0: yaw = -yaw
    return yaw

def calc_Dpt(sfm, pos):
    # 计算相机相对于模型的深度
    D_cur = -sfm.origin.dot(sfm.ABC)
    return D_cur, (pos.dot(sfm.ABC) + D_cur) / np.linalg.norm(sfm.ABC)

from reproj import calc_wps
class reference_path():
    def __init__(self, cgt, odom, left, right, img2binary, scale):
        self.cgt = cgt
        self.odom = odom # 里程计数据
        # 左右目的相机数据 
        self.left = left
        self.right = right
        # 上一个圆的数据
        self.last_info = []
        self.last_left_index = 0
        # 二值化图像数据
        self.img2binary = img2binary
        # 存储图像的比例因子
        self.scale = scale
        self.REC_MIN = 10
        # 记录当前圆的id
        self.count_circle = 0
        
    def start_new_circle(self, circle_id):
        """
            该方法主要用于初始化和开始检测一个新的圆。
            它处理了不同 circle_id 的情况，初始化了多个变量和模型，并计算了当前目标的位置和方向。
            该方法依赖于多个外部变量和函数，如 self.cgt.poses_gt、self.odom.pos 和 calc_yaw，因此在运行前需要确保这些变量和函数已正确定义和初始化。
        """
        # 开始检测到一个新的圆
        self.circle_id = circle_id  
        """
        存储当前圆的标识符。
        """
        self.is_crossed = False  
        # 标志当前圆是否已穿过，初始化为False
        self.D_pt = 10.0 # 初始化相机深度
        if circle_id != 0:
            self.last_info = [self.circle_target, self.sfm, self.left.images]
            self.left.images = []
        # 如果 circle_id 不为零，则保存上一个圆的信息（目标、结构化运动学模型和图像）并清空当前图像列表
        
        self.last_left_index = 0
        # 初始化上一个左相机图像的索引
        self.count_circle = 0
        # 初始化检测到的圆的数量。
        self.no_rec = 0
        # 初始化未记录的计数。
        
        circle_info = self.cgt.poses_gt[self.circle_id]  # 飞行器落地的原因在这里 原因是初始化的时候cgt.poses_gt[0]的位置是正数,在地下。
        # 当前推断的最优解决方案是增加一个判断函数,判断一下,如果当前圆的z轴坐标大于0(坐标系问题)那么就将这个Z取反
        if self.cgt.poses_gt[self.circle_id].position.z > 0:
            circle_info.position.z = -self.cgt.poses_gt[self.circle_id].position.z
        
        # 初始化模型
        self.circle_target = np.float64([circle_info.position.x, circle_info.position.y, circle_info.position.z, circle_info.yaw / 180 * np.pi])
        # 将当前圆的信息转换为 NumPy 数组，并存储到 self.circle_target。这个数组包含圆的位置 (x, y, z) 和偏航角 (yaw)。
        origin, yaw, vec = self.circle_target[0:3].reshape([1, -1]), self.circle_target[3], np.float32([0, 0, 1])
        # 从 self.circle_target 中提取出圆的位置 (origin) 和偏航角 (yaw)，并将偏航角转换为弧度。
        # # 初始化结构化运动学模型（SFM）和当前结构化运动学模型（cur_sfm）
        self.sfm = SFM(origin.copy(), vec.copy(), yaw)
        self.cur_sfm = SFM(origin.copy(), vec.copy(), yaw)
        # 初始化当前帧为None
        self.cur_frame = None
        # 设置结构化运动学模型初始化标志为True
        self.sfm_init_flag = True
        # 初始化航点（wps）为None
        self.wps = None
        # 设置航点完成标志为False
        self.wp_finished = False
        # 记录开始穿越圆的时间
        self.cross_starting_time = time.time()
        # 复制当前圆的目标信息到real_target
        self.real_target = self.circle_target.copy()
        # 计算目标与当前位置在x轴上的差值dx
        dx = self.real_target[0] - self.odom.pos[0]
        # 根据差值确定方向
        self.direction = dx / np.abs(dx)
        # 如果circle_id为0，设置当前目标为当前位置和目标位置的中点
        if circle_id == 0:
            self.cur_target = self.real_target.copy()
            self.cur_target[0:2] = 0.5 * (self.odom.pos[0:2] + self.real_target[0:2])
            self.cur_target[2] = self.real_target[2]
        else:
            # 否则，设置当前目标的偏航角，并计算目标位置的中点
            self.cur_target[3] = self.real_target[3]
            self.cur_target[0:2] = 0.5 * (self.odom.pos[0:2] + self.real_target[0:2])
            self.cur_target[2] = self.real_target[2]
            # 使用calc_yaw函数计算当前目标的偏航角
        self.cur_target[3] = calc_yaw(self.sfm, self.cur_target[0:3])
        
    def update_sfm(self, update_thresh = 5.0):
        """
            update_thresh：更新阈值，默认值为 5.0。
            用于判断当前 SFM 与上一个 SFM 之间的距离是否足够大以进行更新。
            left_index：当前左相机图像的索引。
            cur_time：当前时间。
        """
        #print("usfm", self.left.count, self.sfm.origin, self.sfm_init_flag, self.count_circle)
        left_index = len(self.left.images)
        cur_time = time.time()
        for idx in range(self.last_left_index, left_index):
            if not self.is_crossed:
                self.is_crossed = self.crossed(self.odom.R, self.odom.pos)
                # 如果尚未穿过圆，则调用 crossed 方法检查是否已穿过。
            count, time_img, img, R, pos = self.left.images[idx]
            if cur_time - time_img > 0.3:
                continue
            # 获取图像信息并跳过过时的图像
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
            # print("update_sfm cur:", count, self.cur_sfm.origin, round(self.cur_sfm.yaw, 3))
            # print("update_sfm last:", count, self.sfm.origin, round(self.sfm.yaw, 3))
            self.cur_sfm = SFM(self.sfm.origin.copy(), self.sfm.vec.copy(), self.sfm.yaw)
        self.last_left_index = left_index

    """
    提供的代码片段中的函数calc_target负责根据系统的当前状态计算无人机的目标位置。目标位置表示为具有四个元素的numpy数组:x、y、z坐标和偏航(围绕z轴旋转)
    该功能首先从当前SFM(同步定位和映射)模型中提取原点和偏航。
    然后,它使用原点的x、y、z坐标和偏航创建一个目标numpy数组。
    然后,该函数根据当前目标坐标和真实目标坐标的加权平均值调整目标的x和y坐标。权重分别为0.3和0.7。
    真实目标的坐标会用调整后的目标坐标进行更新。
    当前目标的x和y坐标是无人机位置和真实目标坐标的平均值。
    如果SFM模型已初始化(即self.SFM_init_flag为True),则当前目标的z坐标设置为比目标z坐标低1.0个单位,并使用calc_yaw函数计算偏航。
    如果SFM模型尚未初始化,则当前目标的z坐标设置为目标z坐标和无人机z坐标的平均值。偏航是使用calc_yaw函数计算的。
    然后,该功能检查无人机的位置是否接近SFM模型的原点。如果距离小于0.3个单位,则is_crossed标志设置为True。如果距离小于0.1个单位,则当前目标的x坐标将增加3.0个单位,偏航设置为0。
    最后,根据无人机的位置和SFM模型的原点更新当前目标的x、y和z坐标。
    """
    def calc_target(self):
        origin_, yaw_ = self.sfm.origin, self.sfm.yaw
        target_ = np.float32([origin_[0, 0], origin_[0, 1], origin_[0, 2], yaw_])
        target_[0:3] = 0.3 * target_[0:3] + 0.7 * self.real_target[0:3]     # 这里我把权重调成了0.2和0.8
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
            if norm < 0.5:     # 这个地方的参数norm 对穿过的判定具有影响 这导致了无人机在穿过圆圈时无法正确调整其位置 原本设置的是0.3 现在是0.2 
                self.is_crossed  = True
                if norm < 0.2:
                    self.cur_target[0:3] = self.sfm.origin[0]
                    self.cur_target[0] += 3.0
                    self.cur_target[3] = 0    
            self.cur_target[0:3] = pos + vec / norm * 3.0
            self.cur_target[3] = yaw
            print(self.sfm.yaw*180/np.pi) 

    """
    该功能负责确定无人机是否已成功穿过圆形路径。
    """
    def crossed(self, R, pos, thresh_pt2plane = 0.5, thresh_time = 2.5):
        # 计算当前深度和SFM模型中点的深度
        D_cur, D_pt = calc_Dpt(self.sfm, pos)
        # 检查是否检测到最小圈数、当前深度和点深度之间的差异是否小于阈值、是否超过时间阈值以及无人机位置是否接近SFM模型的原点
        flag1 = self.count_circle > self.REC_MIN
        # 检查深度差的绝对值是否低于阈值
        flag2 = np.abs(D_pt) < thresh_pt2plane
        # 检查自交叉口开始以来经过的时间是否高于阈值
        flag3 = time.time() - self.cross_starting_time > thresh_time
        #检查无人机的位置是否接近SFM模型的原点
        flag4 = np.linalg.norm(pos - self.sfm.origin[0]) < thresh_pt2plane
        #存储深度差以供进一步分析
        self.D_pt = D_pt
        
        #print("crossed", flag1, flag2, flag3, D_cur, D_pt)
        return flag1 and flag2 and flag3 and flag4
    


