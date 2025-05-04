#!/usr/bin/env python

import rospy
import tf2_ros
import tf2_geometry_msgs  # 用于 tf2 与 geometry_msgs 的转换
from sensor_msgs.msg import Imu, PointCloud2
from std_msgs.msg import Header
from sensor_msgs import point_cloud2
from geometry_msgs.msg import TransformStamped
import tf2_sensor_msgs  # 用于转换 PointCloud2

# # 全局变量存储 IMU 的时间戳
# imu_timestamp = None
# tf_buffer = None
# tf_listener = None

# IMU 数据回调函数，更新全局时间戳
# def imu_callback(imu_msg):
#     global imu_timestamp
#     imu_timestamp = imu_msg.header.stamp
#     rospy.loginfo("IMU timestamp updated: %s", imu_timestamp)

# LiDAR 数据回调函数，更新 LiDAR 时间戳并发布
def lidar_callback(lidar_msg):
    # global imu_timestamp, tf_buffer

    # if imu_timestamp is None:
    #     rospy.logwarn("IMU timestamp not available yet.")
    #     return

    # 创建一个新的 PointCloud2 消息，更新时间戳
    # new_lidar_msg = lidar_msg
    # new_lidar_msg.header.stamp = imu_timestamp  # 更新为 IMU 时间戳

    # 坐标系转换：将 LiDAR 数据从 'base_link' 转换到 'map'
    try:
        # 获取从 'base_link' 到 'map' 的转换
        transform = tf_buffer.lookup_transform('world', 'lidar', rospy.Time(0), rospy.Duration(1.0))

        # 转换点云坐标系
        transformed_cloud = tf2_sensor_msgs.do_transform_cloud(lidar_msg, transform)

        # 发布转换后的点云数据
        lidar_pub.publish(transformed_cloud)
        rospy.loginfo("Published transformed LiDAR data with updated timestamp: %s", rospy.Time.now())

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
        rospy.logerr("Transform error: %s", str(e))

if __name__ == '__main__':
    # 初始化 ROS 节点
    rospy.init_node('imu_lidar_sync_node')

    # 初始化 tf2 缓存和监听器
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    # 创建 IMU 数据订阅者
    # imu_sub = rospy.Subscriber('/airsim_node/drone_1/imu/imu', Imu, imu_callback)

    # 创建 LiDAR 数据订阅者
    lidar_sub = rospy.Subscriber('/airsim_node/drone_1/lidar', PointCloud2, lidar_callback)

    # 创建一个新的 Publisher，用于发布修改后的 LiDAR 数据
    lidar_pub = rospy.Publisher('/airsim_node/drone_1/lidar_updated', PointCloud2, queue_size=10)

    # 启动 ROS 循环
    rospy.spin()
