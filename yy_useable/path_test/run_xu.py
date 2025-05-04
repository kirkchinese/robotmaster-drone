# 引入所需的 ROS 包
import rospy

from geometry_msgs.msg import PoseStamped, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CompressedImage, Image
from traj_utils.msg import CirclePoses

# 引入 OpenCV 所需的函数
from cv_bridge.boost.cv_bridge_boost import getCvType
from cv_bridge import CvBridge, CvBridgeError
# 引入 TF2 所需的包
import tf2_ros
import tf

# 引入 numpy 并设置其输出格式
import numpy as np
np.set_printoptions(precision = 2)
import cv2
import time


# 引入自定义的函数和类 
from reproj import SFM, FRAME, p2w_w2p_once, calc_circle
from reproj import w2p_sim, KRt2proj, init_circle, calc_wps
from path import circle_gt, images_class, odometry_class, reference_path, target2msg, calc_yaw
from CNN import IMAGE

cgt = circle_gt() #获得圆环位置的类
odom = odometry_class()
rospy.init_node('reference',anonymous=True)

# odom_sub = rospy.Subscriber("/vins_fusion/imu_propagate", Odometry, odom.odom_callback)
odom_sub = rospy.Subscriber("/airsim_node/drone_1/debug/pose_gt", PoseStamped, odom.odom_callback)

#circle_sub = rospy.Subscriber("/airsim_node/drone_1/debug/circle_poses_gt", CirclePoses, cgt.circle_pos_callback)
circle_sub = rospy.Subscriber("/airsim_node/drone_1/circle_poses", CirclePoses, cgt.circle_pos_callback)

# 自定义的图像处理类,内部包含的函数等待后续的阅读
left_images = images_class(odom, prefix = "left")
right_images = images_class(odom, prefix = "right")
# 左目和右目的图像cb
left_sub = rospy.Subscriber("/airsim_node/drone_1/front_left/Scene", Image, left_images.image_callback, queue_size=5)
right_sub = rospy.Subscriber("/airsim_node/drone_1/front_right/Scene", Image, right_images.image_callback, queue_size=5)

pub = rospy.Publisher("/reference_path", PoseStamped, queue_size=10)
# 等待订阅的节点发布数据(其实是模拟器启动比这个节点慢)

while len(cgt.poses_gt) == 0:
    time.sleep(0.5)

circle_info = cgt.poses_gt[0]

circle_target = np.float32([circle_info.position.x, circle_info.position.y, circle_info.position.z, circle_info.yaw / 180 * np.pi])

origin, yaw, vec = circle_target[0:3].reshape([1, -1]), circle_target[3], [0, 0, 1]

is_crossed = True

sfm_left = SFM(origin, vec, yaw)
sfm_right = SFM(origin, vec, yaw)

image_handle = IMAGE(model_path = 'yy_useable/path_test/cnn.pt')

rpath = reference_path(cgt, odom, left_images, right_images, image_handle.get2_binary, scale = 2)

last_time = time.time()

publish_count = 0  #发布次数
rpath.is_crossed = True
rpath.circle_id = -1

while 1:
    cur_time = time.time()
    
    print("==========程序运行===========")
    
    if is_crossed:
        print("===========开始穿环============")
        





