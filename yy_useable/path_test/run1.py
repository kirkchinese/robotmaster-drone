
import rospy

from geometry_msgs.msg import PoseStamped, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CompressedImage, Image
from traj_utils.msg import CirclePoses

from cv_bridge.boost.cv_bridge_boost import getCvType
from cv_bridge import CvBridge, CvBridgeError
import tf2_ros
import tf

import numpy as np
np.set_printoptions(precision = 2)
import cv2
import time

from reproj import SFM, FRAME, p2w_w2p_once, calc_circle
from reproj import w2p_sim, KRt2proj, init_circle, calc_wps
from path import circle_gt, images_class, odometry_class, reference_path, target2msg, calc_yaw
from CNN import IMAGE

cgt = circle_gt()
odom = odometry_class()



rospy.init_node('reference',anonymous=True)    # 这段代码初始化了自己的节点名称 reference 
"""
此处为订阅器,订阅了vins的imu_propagate话题,airsim_node的circle_poses话题,airsim_node的front_left/Scene话题,airsim_node的front_right/Scene话题
"""
# odom_sub = rospy.Subscriber("/vins_fusion/imu_propagate", Odometry, odom.odom_callback)
odom_sub = rospy.Subscriber("/airsim_node/drone_1/debug/pose_gt", PoseStamped, odom.odom_callback)
circle_sub = rospy.Subscriber("/airsim_node/drone_1/debug/circle_poses_gt", CirclePoses, cgt.circle_pos_callback)
# circle_sub = rospy.Subscriber("/airsim_node/drone_1/circle_poses", CirclePoses, cgt.circle_pos_callback)


left_images = images_class(odom, prefix = "")
right_images = images_class(odom, prefix = "right")
left_sub = rospy.Subscriber("/airsim_node/drone_1/front_left/Scene", Image, left_images.image_callback, queue_size=5)
#right_sub = rospy.Subscriber("/airsim_node/drone_1/front_right/Scene", Image, right_images.image_callback, queue_size=5)

while len(cgt.poses_gt) == 0:
    time.sleep(0.5)
pub = rospy.Publisher("/reference_path", PoseStamped, queue_size=10)

image_handle = IMAGE(model_path = 'cnn.pt')
rpath = reference_path(cgt, odom, left_images, right_images, image_handle.get2_binary, scale = 2)
last_time = time.time()

publish_count = 0
rpath.is_crossed = True
rpath.circle_id = -1

while 1:
    cur_time = time.time()
    if rpath.is_crossed:
        # print('===========================')
        rpath.start_new_circle(rpath.circle_id + 1)
        msg = target2msg(rpath.cur_target)
        pub.publish(msg)
        publish_count += 1
        last_wp = rpath.cur_target.copy()
        # print("from c{} to c{}".format(rpath.circle_id - 1, rpath.circle_id), round(cur_time, 2), rpath.cur_target, rpath.real_target, rpath.count_circle)
        # print('cinfo', rpath.circle_target, "count", left_images.count, "sfm info", rpath.sfm.origin, round(rpath.sfm.yaw, 3))
        # print("-----------------publish", publish_count, "++++++++++++++++")
    norm = np.linalg.norm(odom.pos - last_wp[0:3])
    if cur_time - last_time > 0.15:
        if cur_time - rpath.cross_starting_time > 1.5:
            rpath.update_sfm()
        if norm > 2.0:
            msg = target2msg(last_wp)
            pub.publish(msg)
            # print("last_wp", last_wp, norm, odom.pos)
        last_time = cur_time
    if norm < 2.0:
        rpath.calc_target()
        msg = target2msg(rpath.cur_target)
        pub.publish(msg)
        publish_count += 1
        # print(round(cur_time, 2), rpath.no_rec, "pc,ic,cc,D_pt", publish_count, left_images.count, rpath.count_circle, rpath.D_pt)
        # print("lwp,p,ct,rt", last_wp, odom.pos, rpath.cur_target, rpath.real_target, "sfm info", rpath.sfm.origin, round(rpath.sfm.yaw, 3))
        last_wp = rpath.cur_target.copy()
    time.sleep(0.03)
