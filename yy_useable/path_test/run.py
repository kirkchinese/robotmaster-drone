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


# 定义所需的变量
cgt = circle_gt() #获得圆环位置的类
odom = odometry_class()

# 初始化 ROS 节点 reference 外面的controllor 正是订阅这个节点的
rospy.init_node('reference',anonymous=True)

# 这里是订阅无人机位置的节点 
# odom_sub = rospy.Subscriber("/vins_fusion/imu_propagate", Odometry, odom.odom_callback)
odom_sub = rospy.Subscriber("/airsim_node/drone_1/debug/pose_gt", PoseStamped, odom.odom_callback)
#circle_sub = rospy.Subscriber("/airsim_node/drone_1/debug/circle_poses_gt", CirclePoses, cgt.circle_pos_callback)

# 圆环的参考路径
circle_sub = rospy.Subscriber("/airsim_node/drone_1/circle_poses", CirclePoses, cgt.circle_pos_callback)

# 自定义的图像处理类,内部包含的函数等待后续的阅读
left_images = images_class(odom, prefix = "left")
right_images = images_class(odom, prefix = "right")
# 左目和右目的图像cb
left_sub = rospy.Subscriber("/airsim_node/drone_1/front_left/Scene", Image, left_images.image_callback, queue_size=5)
right_sub = rospy.Subscriber("/airsim_node/drone_1/front_right/Scene", Image, right_images.image_callback, queue_size=5)

# 等待订阅的节点发布数据(其实是模拟器启动比这个节点慢)
while len(cgt.poses_gt) == 0:
    time.sleep(0.5)
    
# 获取第一个圆的 ground truth 信息
circle_info = cgt.poses_gt[0]


# 转换圆的 ground truth 信息为 numpy 数组
circle_target = np.float32([circle_info.position.x, circle_info.position.y, circle_info.position.z, circle_info.yaw / 180 * np.pi])


# 获取圆的初始位置、偏航角和法向量
origin, yaw, vec = circle_target[0:3].reshape([1, -1]), circle_target[3], [0, 0, 1]

# 初始化 SFM 类
sfm_left = SFM(origin, vec, yaw)
sfm_right = SFM(origin, vec, yaw)

# 发布器定义
pub = rospy.Publisher("/reference_path", PoseStamped, queue_size=10)

# 初始化 IMAGE 类
image_handle = IMAGE(model_path = '/home/misaka/drone/yy_useable/path_test/cnn.pt')

# 初始化 reference_path 类
rpath = reference_path(cgt, odom, left_images, right_images, image_handle.get2_binary, scale = 2)

# 获取当前时间
last_time = time.time()

# 初始化一些变量
publish_count = 0  #发布次数
rpath.is_crossed = True
rpath.circle_id = -1


#print_time = last_time
#last_circle_time = last_time
#thresh = 0.1
#dist = []
#Ds_cur = []
#Ds_pt = []
#tts = []

while 1:
    cur_time = time.time()
    
#    D_cur = -left_images.sfm.origin.dot(left_images.sfm.ABC) / np.linalg.norm(left_images.sfm.ABC)
 #   D_pt = (odom.pos.dot(left_images.sfm.ABC) + D_cur) / np.linalg.norm(left_images.sfm.ABC)
    
  #  tts.append(cur_time)
  #  Ds_cur.append(D_cur)
  #  Ds_pt.append(D_pt)

     # 如果 drone 穿过了圆
    if rpath.is_crossed:
        print('===========================')

        # 开始新的圆
        rpath.start_new_circle(rpath.circle_id + 1)

        # 发布新的目标点
        msg = target2msg(rpath.cur_target)
        pub.publish(msg)
        # 计数器+=1
        publish_count += 1
        # 保存上一个点
        last_wp = rpath.cur_target.copy()
        print("from c{} to c{}".format(rpath.circle_id - 1, rpath.circle_id), round(cur_time, 2), rpath.cur_target, rpath.real_target, rpath.count_circle)
        print('cinfo', rpath.circle_target, "count", left_images.count, "sfm info", rpath.sfm.origin, round(rpath.sfm.yaw, 3))
        print("-----------------publish", publish_count, "++++++++++++++++")
    

    # 计算 drone 与上一个目标点的距离
    norm = np.linalg.norm(odom.pos - last_wp[0:3])
    # 如果 drone 与上一个目标点的距离大于 2.0 或者 drone 与上一个目标点的距离小于 2.0 并且 drone 已经在 0.15 秒内没有发布新的目标点
    if cur_time - last_time > 0.8:
        # 如过drone传过了圆
        if cur_time - rpath.cross_starting_time > 0.15 :   # 源数据1.5,在此因为有GPU的使用改为0.75  (这个数据与受到速度的限制 这导致了0.75的刷新速度处于0.75-1.75之间 出现的问题是时序对不齐)
            # 更新SFM
            rpath.update_sfm()
        # 如果drone与上一个目标点的距离大于 2.0
        if norm > 2.0:   # 源数据是2.0,在此改为1.5
            msg = target2msg(last_wp)
            # 调试用
            pub.publish(msg)
            print("last_wp", last_wp, norm, odom.pos)

        # 更新上一个目标点的时间
        last_time = cur_time
        # 如果 drone 与上一个目标点的距离小于 1.5
    if norm < 2.0 and cur_time - last_time < 10 :
        # 调用 rpath 类中的 calc_target() 方法来计算新的目标点
        rpath.calc_target()
        # 构建一个 PoseStamped 消息,并将新的目标点信息填入其中
        msg = target2msg(rpath.cur_target)
        # 发布新的目标点
        pub.publish(msg)
        # 发布计数器加 1
        publish_count += 1
        # 打印一些有用的信息
        print(round(cur_time, 2), rpath.no_rec, "pc,ic,cc,D_pt", publish_count, left_images.count, rpath.count_circle, rpath.D_pt)
        print("lwp,p,ct,rt", last_wp, odom.pos, rpath.cur_target, rpath.real_target, "sfm info", rpath.sfm.origin, round(rpath.sfm.yaw, 3))
        # 更新上一个目标点
        last_wp = rpath.cur_target.copy()
    # 循环每 30ms
    time.sleep(0.03)
