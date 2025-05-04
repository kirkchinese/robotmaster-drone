#pragma once
#include <ros/ros.h>
#include <Eigen/Dense>
#include <airsim_ros/RotorPWM.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/PoseStamped.h>

class PIDController {
public:
    PIDController(ros::NodeHandle& nh);

    void setDesiredState(const Eigen::VectorXf& X_des);
    void odomCallback(const nav_msgs::Odometry::ConstPtr& msg);
    void runControlLoop();

private:
    Eigen::Vector4f computePWM(const Eigen::VectorXf& X_des, const Eigen::VectorXf& X_real);
    void loadPIDParameters();
    void publishPWM(const Eigen::Vector4f& pwm);

    ros::Subscriber target_sub_;
    void targetCallback(const geometry_msgs::PoseStamped::ConstPtr& msg);

    // ROS members
    ros::NodeHandle nh_;
    ros::Subscriber odom_sub_;
    ros::Publisher pwm_pub_;

    // PID parameters
    struct PIDParams {
        // Position control
        float Kp_x, Ki_x, Kd_x;
        float Kp_y, Ki_y, Kd_y;
        float Kp_z, Ki_z, Kd_z;

        // Velocity control
        float Kp_vx, Kd_vx;
        float Kp_vy, Kd_vy;

        // Attitude control
        float Kp_phi, Kd_phi;
        float Kp_theta, Kd_theta;
        float Kp_psi, Kd_psi;

        // Physical parameters
        float mass;
        float gravity;
        float armlength;
        float Ct, Cq;
        float Fmax;

        // Limits
        float max_v;
        float max_acc;
        float max_ang;

        // Inertia
        float Ixx, Iyy, Izz;
    } params_;

    // State variables
    Eigen::VectorXf X_des_;
    Eigen::VectorXf X_real_;
    bool has_odom_;

    // Integral terms
    float integral_e_x_, integral_e_y_, integral_e_z_;
    float last_e_x_, last_e_y_, last_e_z_;
    float last_e_vx_, last_e_vy_;
    float last_e_phi_, last_e_theta_, last_e_psi_;
};