#ifndef _POS_CTRL_CPP_
#define _POS_CTRL_CPP_

#include "pos_ctrl.hpp"

int main(int argc, char** argv)
{

    ros::init(argc, argv, "pos_ctrl"); // 初始化ros 节点,命名为 basic
    ros::NodeHandle n; // 创建node控制句柄
    POSCtrl go(&n);
    return 0;
}

POSCtrl::POSCtrl(ros::NodeHandle *nh)
{  
    //创建图像传输控制句柄
    it = std::make_unique<image_transport::ImageTransport>(*nh); 
    front_img = cv::Mat(480, 640, CV_8UC3, cv::Scalar(0));

    takeoff.request.waitOnLastTask = 1;
    land.request.waitOnLastTask = 1;

    // 使用publisher发布速度指令需要定义 Velcmd , 并赋予相应的值后,将他publish()出去
    velcmd.twist.angular.z = 0;//z方向角速度(yaw, deg)
    velcmd.twist.linear.x = 0.5; //x方向线速度(m/s)
    velcmd.twist.linear.y = 0.0;//y方向线速度(m/s)
    velcmd.twist.linear.z = -0.5;//z方向线速度(m/s)

    // 使用publisher发布速度指令需要定义 Velcmd , 并赋予相应的值后,将他publish()出去
    posecmd.roll = 0; //x方向姿态(rad)
    posecmd.pitch = 0;//y方向姿态(rad)
    posecmd.yaw = 0;//z方向姿态(rad)
    posecmd.throttle = 1.0;//油门, (0.0-1.0)

    //无人机信息通过如下命令订阅,当收到消息时自动回调对应的函数
    odom_suber = nh->subscribe<geometry_msgs::PoseStamped>("/airsim_node/drone_1/debug/pose_gt", 1, std::bind(&POSCtrl::odom_local_ned_cb, this, std::placeholders::_1));//状态真值,用于赛道一
    
    CirclePoses = nh->subscribe<airsim_ros::CirclePoses>("/airsim_node/drone_1/debug/circle_poses_gt", 1, std::bind(&POSCtrl::CirclePoses_get_cb, this, std::placeholders::_1));//Circle Poses 真值
    //修改自 五月
    
    front_View_suber = it->subscribe("airsim_node/drone_1/front_left/Scene", 1, std::bind(&POSCtrl::front_view_cb, this,  std::placeholders::_1));

    //通过这两个服务可以调用模拟器中的无人机起飞和降落命令
    takeoff_client = nh->serviceClient<airsim_ros::Takeoff>("/airsim_node/drone_1/takeoff");
    land_client = nh->serviceClient<airsim_ros::Takeoff>("/airsim_node/drone_1/land");
    reset_client = nh->serviceClient<airsim_ros::Reset>("/airsim_node/reset");
    setGoalPosition = nh->serviceClient<airsim_ros::SetLocalPosition>("/airsim_node/local_position_goal/override");
    //通过这两个publisher实现对无人机的速度控制和姿态控制
    vel_publisher = nh->advertise<airsim_ros::VelCmd>("airsim_node/drone_1/vel_cmd_body_frame", 1);
    pose_publisher = nh->advertise<airsim_ros::PoseCmd>("airsim_node/drone_1/pose_cmd_body_frame", 1);

    ros::Timer timer = nh->createTimer(ros::Duration(0.5), &POSCtrl::setPosition_cb, this);
    ros::spin();
}

 /* 文件名:[pos_ctrl.cpp]
 * 作者:〈版权属于编写者“五月”〉
 * 描述:〈run〉
 * 修改人:〈五月〉
 * 修改时间:2024-07-21
 * 修改内容:〈添加了卡死跳出(失败)〉
 */
//time_t first, second;
void POSCtrl::setPosition_cb(const ros::TimerEvent&)


{
    if(!takeoffflag)
        takeoff_client.call(takeoff);
        takeoffflag = 1;
    request11_.request.vehicle_name = "drone_1";
    request11_.request.x = goalpath[goalIdx][0];
    request11_.request.y = goalpath[goalIdx][1]; 
    request11_.request.z = goalpath[goalIdx][2];
    request11_.request.yaw = goalpath[goalIdx][3];
    float d = sqrtf32(powf32((goalpath[goalIdx][0] - Pose[0]),2)+powf32((goalpath[goalIdx][1] - Pose[1]),2)+powf32((goalpath[goalIdx][2] - Pose[2]),2));
    //ROS_INFO("dis to goal: %f", d);
    //ROS_INFO("goal : %f %f %f %f", goalpath[goalIdx][0], goalpath[goalIdx][1], goalpath[goalIdx][2], goalpath[goalIdx][3]);
    if(d < 2) { //门限,原值为5 现值为0.01 修改者 五月。
        goalIdx += 1;
        goalIdx %= circlesCount;
        //first = time(NULL);
    }

    setGoalPosition.call(request11_);  //这一句用于发布goal position
    
}

POSCtrl::~POSCtrl()
{
    // cv::destroyAllWindows();
}

void POSCtrl::odom_local_ned_cb(const geometry_msgs::PoseStamped::ConstPtr& msg)
{
    // ROS_INFO("Get odom_local_ned_cd\n\r  orientation: %f-%f-%f-%f\n\r  position: %f-%f-%f\n\r", 
    // msg->orientation.w, msg->orientation.x, msg->orientation.y, msg->orientation.z, //姿态四元数
    // msg->position.x, msg->position.y,msg->position.z);//位置)
    tf2::Quaternion quat_tf;
    double roll, pitch, yaw;
    tf2::fromMsg(msg->pose.orientation, quat_tf);
    tf2::Matrix3x3(quat_tf).getRPY(roll, pitch, yaw);
    Pose[0] = msg->pose.position.x;
    Pose[1] = msg->pose.position.y;
    Pose[2] = msg->pose.position.z;
    Pose[3] = yaw;

    RPY[0]=roll;
    RPY[1]=pitch;
    RPY[2]=yaw;

}

 /* 文件名:[pos_ctrl.h]
 * 作者:〈版权属于编写者“五月”〉
 * 描述:〈写圆〉
 * 修改人:〈五月〉
 * 修改时间:2024-07-24
 * 修改内容:〈build_parabola〉
 */
float POSCtrl::get_distance(float x1, float y1,float z1,float x2,float y2,float z2)
{
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2));
}

 /* 文件名:[pos_ctrl.cpp]
 * 作者:〈版权属于编写者“五月”〉
 * 描述:〈写圆〉
 * 修改人:〈五月〉
 * 修改时间:2024-07-21
 * 修改内容:〈CirclePoses_get_cb〉
 */
void POSCtrl::CirclePoses_get_cb(const airsim_ros::CirclePoses::ConstPtr& msg)  // 五月改
{   
    int num_circles = msg->poses.size();
    float distance = 7,distance_b = 7;  //距离,修改者 五月。
    if (num_circles > circlesCount) {
        ROS_WARN("Received more circles than expected. Truncating to %d.", circlesCount);
        num_circles = circlesCount;
    }

    for (int i = 1,j = 0; i <= num_circles,j<=num_circles; i+=3,j++) {
        goalpath[i][0] = msg->poses[j].position.x;
        goalpath[i][1] = msg->poses[j].position.y;
        goalpath[i][2] = msg->poses[j].position.z;
        float yaw = msg->poses[j].yaw * M_PI / 180;
        goalpath[i][3] = yaw;
        
        circles[j][0] = msg->poses[j].position.x;
        circles[j][1] = msg->poses[j].position.y;
        circles[j][2] = msg->poses[j].position.z;
        circles[j][3] = yaw;

        if (goalIdx < 12 ){
        goalpath[i+1][0] = goalpath[i][0] + distance_b * cos(yaw);
        goalpath[i+1][1] = goalpath[i][1] + distance_b * sin(yaw);
        goalpath[i+1][2] = goalpath[i][2];
        goalpath[i+1][3] = yaw;

        goalpath[i-1][0] = goalpath[i][0] - distance * cos(yaw);
        goalpath[i-1][1] = goalpath[i][1] - distance * sin(yaw);
        goalpath[i-1][2] = goalpath[i][2];
        goalpath[i-1][3] = yaw;
        }
        else{
        goalpath[i+1][0] = goalpath[i][0] - distance * cos(yaw);
        goalpath[i+1][1] = goalpath[i][1] - distance * sin(yaw);
        goalpath[i+1][2] = goalpath[i][2];
        goalpath[i+1][3] = yaw;

        goalpath[i-1][0] = goalpath[i][0] + distance_b * cos(yaw);
        goalpath[i-1][1] = goalpath[i][1] + distance_b * sin(yaw);
        goalpath[i-1][2] = goalpath[i][2];
        goalpath[i-1][3] = yaw;
        }
    }
}

int POSCtrl::got_circle_id(int id)
{
    int temp = 3*id+3;
    return floor(temp/(id+4));


}

void POSCtrl::front_view_cb(const sensor_msgs::ImageConstPtr& msg)
{
    cv_front_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_8UC3);
    cv::imshow("front_left", cv_front_ptr->image);

    std::string image_path = "/home/misaka/drone/15pass/data/img/front_view_" + std::to_string(image_counter++) + ".png";
    cv::imwrite(image_path, cv_front_ptr->image);
    //这里需要把图像按顺序保存在训练集目录的data文件夹中,同时记录图像这一帧时的位姿与飞机距离圆环中心点的距离,以及此时图像中圆环的yaw角,保存在一个txt文件内。
    std::ofstream file("/home/misaka/drone/15pass/data/front_view.txt", std::ios::app);
    file << std::fixed << std::setprecision(6) << image_counter << ",RPY = (" << RPY[0] << "," << RPY[1] << "," << RPY[2] << "), distance = " << get_distance(Pose[0], Pose[1], Pose[2], circles[got_circle_id(goalIdx)][0], circles[got_circle_id(goalIdx)][1], circles[got_circle_id(goalIdx)][2]) << ", yaw = " << circles[got_circle_id(goalIdx)][3] << "\n";
    //按次序是:飞机的roll,pitch,yaw,距离,yaw
    file.close();
//这段代码有问题,需要修改

    cv::waitKey(10);
    
}


template <typename T> int POSCtrl::sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

void POSCtrl::go_to(float x, float y, float z, float yaw)
{
    ROS_INFO("get updating pose:%f, %f, %f, %f", Pose[0], Pose[1], Pose[2], Pose[3]);
    // double cout = cpid.caculate(10, Pose[2]);
    velcmd.twist.linear.x =0;
    velcmd.twist.linear.y =0;
    velcmd.twist.angular.z = 0;
    velcmd.twist.linear.z = 0;
    // ROS_INFO("output:%f, %f, %f, %f", 0, 0, velcmd.twist.linear.z, 0);
    vel_publisher.publish(velcmd);
}

void POSCtrl::go()
{
    go_to(0, 0, 50, 0);
}

#endif
