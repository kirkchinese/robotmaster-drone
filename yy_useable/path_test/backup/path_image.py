#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rospy
from traj_utils.msg import CirclePoses
from sensor_msgs.msg import CompressedImage, Image
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from cv_bridge.boost.cv_bridge_boost import getCvType
from cv_bridge import CvBridge, CvBridgeError

import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

import rospy
import tf2_ros
import tf
from geometry_msgs.msg import TransformStamped
import numpy as np


# !pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple 



def get_ellp(image): 
   thresh = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 220)) * 128
   contours,hierarchy = cv2.findContours(thresh, 1, 2)
   ellps = []
   for cnt in contours:
       if cnt.shape[0] < 10: 
           continue
       ellp = cv2.fitEllipse(cnt)
       ellps.append(ellp)
       
   return thresh, contours, ellps
   
def draw(image, thresh, blank1, blank2):
   plt.figure(figsize=(10,10))
   plt.subplot(221)
   plt.imshow(image)
   plt.subplot(222)
   plt.imshow(thresh)
   plt.subplot(223)
   plt.imshow(blank1)
   plt.subplot(224)
   plt.imshow(blank2)
   plt.show()


class circle_gt():
    def __init__(self):
        self.poses_gt = []

    def circle_pos_callback(self, circle_pos):
        self.poses_gt = circle_pos.poses
            
class images_class():
    def __init__(self, prefix):
        self.images = []
        self.bridge = CvBridge()
        self.prefix = prefix
        self.count = 0
        self.ellps = []
        
    def image_callback(self, image):
        stamp = time.time()
        img = self.bridge.imgmsg_to_cv2(image, desired_encoding='bgr8')
        #np.savez(self.prefix + "/" + str(self.count), img = img, stamp = stamp)
        self.count+=1
        self.ellps = get_ellp(img)[2]
        self.images.append([stamp, img, self.ellps])
        np.savez(self.prefix + "/" + str(self.count), img = img, stamp = stamp)
            
class odometry_class():
    def __init__(self):
        self.q = np.float32([0, 0, 0, 1])
        self.rmatrix = np.float32([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        self.pos = np.float32([0, 0, 0])
        self.vel = np.float32([0, 0, 0])
        
    def odom_callback(self, odom):
        curq = np.float32([odom.pose.pose.orientation.x, odom.pose.pose.orientation.y, odom.pose.pose.orientation.z, odom.pose.pose.orientation.w])
        r1m = tf.transformations.quaternion_matrix(curq)
        self.q = tf.transformations.quaternion_from_matrix(self.rmatrix.dot(r1m))
        self.pos = np.float32([odom.pose.pose.position.x, -odom.pose.pose.position.y, -odom.pose.pose.position.z])
        self.vel = np.float32([odom.twist.twist.linear.x, -odom.twist.twist.linear.y, -odom.twist.twist.linear.z])


cgt = circle_gt()
odom = odometry_class()
left_images = images_class("left")
right_images = images_class("right")
rospy.init_node('pylistener',anonymous=True)
#Subscriber函数第一个参数是topic的名称,第二个参数是接受的数据类型,第三个参数是回调函数的名称
odom_sub = rospy.Subscriber("/vins_fusion/imu_propagate", Odometry, odom.odom_callback)
circle_sub = rospy.Subscriber("/airsim_node/drone_1/debug/circle_poses_gt", CirclePoses, cgt.circle_pos_callback)
left_sub = rospy.Subscriber("/airsim_node/drone_1/front_left/Scene", Image, left_images.image_callback, queue_size=3)
right_sub = rospy.Subscriber("/airsim_node/drone_1/front_right/Scene", Image, right_images.image_callback, queue_size=3)
pub = rospy.Publisher("/reference_path", PoseStamped, queue_size=10)


# In[5]:


def get_diff(ch, hw, factor):
    diff = np.zeros(3, np.float32)
    if len(ch) == 0: return diff
    origin_ = ch[0][0]
    diff[1] = hw[1] * 0.5 - origin_[0]
    diff[2] = hw[0] * 0.5 - origin_[1]
    return factor * diff


# In[6]:

while (len(cgt.poses_gt) == 0): time.sleep(0.5)

class reference_path():
    def __init__(self, cgt, odom, left):
        self.cgt = cgt
        self.odom = odom
        self.cur_target = np.float32([0, 0, -1.53, 0])
        self.circle_id = 0
        self.norm_thresh = 0.5
        self.left = left
        
    def update_msg(self):
        msg = PoseStamped() # 创建 msg 对象
        msg.header.stamp= rospy.Time.now()
        msg.pose.position.x = self.cur_target[0]
        msg.pose.position.y = -self.cur_target[1]
        msg.pose.position.z = -self.cur_target[2]
        msg.pose.orientation.x = self.cur_target[3]
        self.msg = msg
        
    def update_target(self, thresh = 40.0):
        cur_pos = odom.pos
        circle_info = self.cgt.poses_gt[self.circle_id]
        circle_target = np.float32([circle_info.position.x, circle_info.position.y, circle_info.position.z, circle_info.yaw / 180 * np.pi])
        print("-----------", self.circle_id, np.linalg.norm(cur_pos - circle_target[0:3]))
        print(circle_target)
        ch = [ellp for ellp in self.left.ellps if ellp[1][0] > thresh or ellp[1][1] > thresh]
        diff = get_diff(ch, (480, 640), -0.01)
        self.cur_target[0:3] = 0.5 * cur_pos + 0.5 * circle_target[0:3] + diff
        self.cur_target[3] = circle_target[3]
        print("update:", cur_pos, "circle_tar:", circle_target, "cur_tar", self.cur_target)
        print("ellp++++++++++++++++++", diff)
        for ellp in ch:
            print(ellp)
        


# In[ ]:


rpath = reference_path(cgt, odom, left_images)
rpath.norm_thresh = 4
while 1:
    print("publish----", time.time())
    rpath.update_target()
    rpath.update_msg()
    msg = PoseStamped() # 创建 msg 对象
    msg.header.stamp= rospy.Time.now()
    msg.pose.position.x = cgt.poses_gt[1].position.x;
    msg.pose.position.y = -cgt.poses_gt[1].position.y;
    msg.pose.position.z = -cgt.poses_gt[1].position.z;
    msg.pose.orientation.x = cgt.poses_gt[1].yaw / 180 * np.pi;
    #pub.publish(msg)
    #break
    pub.publish(rpath.msg)
    time.sleep(0.3)



