本人在参加robotmaster-drone比赛中用到的、自己编写的、老师提供的全部代码，系继承原有代码。代码是2022版
2024版代码因为老系统崩溃带走了我的硬盘以及时间过于久远等的缘故，大部分丢了，不确定是不是还存在在这里的哪一处。
正在准备考研，没时间搞这些了，所以全上传上去记录一下，有空再整理。

下面是AI生成给我的md，有多少参考性，我也不清楚（管生不管养.JPG）。
# 基于ROS和AirSim的无人机控制系统

## 项目概述
本项目是一个基于ROS和AirSim的无人机控制系统，主要功能包括：
- 与AirSim仿真器交互控制无人机
- 使用YOLO进行目标检测
- 基于PD控制的位置控制
- 动态路径规划

## 系统要求
- Ubuntu 18.04/20.04
- ROS Melodic/Noetic
- AirSim仿真器
- CUDA (用于YOLO加速)
- Python 3.6+
- OpenCV 4.0+

## 安装指南
1. 克隆本仓库到ROS工作空间的src目录：
   ```bash
   cd ~/catkin_ws/src
   git clone [仓库地址]
   ```

2. 安装依赖：
   ```bash
   sudo apt-get install ros-${ROS_DISTRO}-image-transport ros-${ROS_DISTRO}-cv-bridge
   ```

3. 编译项目：
   ```bash
   cd ~/catkin_ws
   catkin_make
   source devel/setup.bash
   ```

## 使用说明
### 启动AirSim仿真器
1. 启动AirSim并加载相应场景

### 启动ROS节点
1. 启动位置控制节点：
   ```bash
   roslaunch pos_ctrl pos_ctrl.launch
   ```

2. 启动YOLO检测节点：
   ```bash
   roslaunch yolo_ros yolo_detection.launch
   ```

## 功能说明
### 主要节点
1. `pos_ctrl` - 位置控制节点
   - 订阅：/airsim_node/drone_1/debug/pose_gt (无人机位姿)
   - 订阅：/Circle_pose (YOLO检测结果)
   - 发布：/airsim_node/drone_1/vel_cmd_body_frame (速度控制指令)

2. `yolo_sub_and_goal_pub` - YOLO检测与目标发布节点
   - 订阅：/yolomsg_right (YOLO检测结果)
   - 发布：/target (目标位置)

## 注意事项
1. 确保AirSim仿真器正确配置ROS接口
2. YOLO检测需要预训练模型，请放置在正确目录
3. 首次运行时可能需要调整PD控制参数
4. 路径规划基于YOLO检测结果，需确保检测质量

## 示例演示
1. 启动所有节点后，无人机将自动起飞
2. 系统会根据YOLO检测结果自动规划路径
3. 可通过Rviz观察无人机轨迹

## 维护者
- [五月] - 主要开发者
- [jakeluo] - 项目维护
