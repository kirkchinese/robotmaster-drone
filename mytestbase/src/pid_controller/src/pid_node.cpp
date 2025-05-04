#include "pid_controller/PIDController.hpp"
#include <ros/ros.h>

int main(int argc, char** argv) {
    ros::init(argc, argv, "pid_controller");
    ros::NodeHandle nh;

    PIDController controller(nh);

    ros::Rate rate(100); // 100Hz
    while(ros::ok()) {
        controller.runControlLoop();
        ros::spinOnce();
        rate.sleep();
    }

    return 0;
}