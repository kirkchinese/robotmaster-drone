#include "pid_controller/PIDController.hpp"
#include <algorithm>
#include <iostream>

PIDController::PIDController(ros::NodeHandle& nh) 
    : nh_(nh), 
      has_odom_(false), 
      integral_e_x_(0), integral_e_y_(0), integral_e_z_(0),
      last_e_x_(0), last_e_y_(0), last_e_z_(0),
      last_e_vx_(0), last_e_vy_(0),
      last_e_phi_(0), last_e_theta_(0), last_e_psi_(0) {

    loadPIDParameters();

    // odom_sub_ = nh_.subscribe("/vins_fusion/imu_propagate", 1, &PIDController::odomCallback, this);
    odom_sub_ = nh_.subscribe("/eskf_odom", 1, &PIDController::odomCallback, this);
    pwm_pub_ = nh_.advertise<airsim_ros::RotorPWM>("/airsim_node/drone_1/rotor_pwm_cmd", 1);
    target_sub_ = nh_.subscribe("/target_pose", 1, &PIDController::targetCallback, this);

    X_des_ = Eigen::VectorXf::Zero(12);
    X_real_ = Eigen::VectorXf::Zero(12);
}

void PIDController::targetCallback(const geometry_msgs::PoseStamped::ConstPtr& msg) {
    Eigen::VectorXf new_des(12);
    new_des.setZero();

    new_des[0] = msg->pose.position.x;
    new_des[1] = msg->pose.position.y;
    new_des[2] = msg->pose.position.z;

    Eigen::Quaternionf q(
        msg->pose.orientation.w,
        msg->pose.orientation.x,
        msg->pose.orientation.y,
        msg->pose.orientation.z
    );
    auto euler = q.toRotationMatrix().eulerAngles(2, 1, 0);
    new_des[6] = euler[2]; // roll
    new_des[7] = euler[1]; // pitch
    new_des[8] = euler[0]; // yaw

    setDesiredState(new_des);
    ROS_INFO_STREAM("New target received: " << new_des[0] << ", " << new_des[1] << ", " << new_des[2]);
}

void PIDController::loadPIDParameters() {
    ros::NodeHandle pnh("~");

    // 位置控制
    pnh.param("Kp_x", params_.Kp_x, 1.0f);
    pnh.param("Ki_x", params_.Ki_x, 0.01f);
    pnh.param("Kd_x", params_.Kd_x, 0.1f);

    pnh.param("Kp_y", params_.Kp_y, 1.0f);
    pnh.param("Ki_y", params_.Ki_y, 0.01f);
    pnh.param("Kd_y", params_.Kd_y, 0.1f);

    pnh.param("Kp_z", params_.Kp_z, 2.0f);
    pnh.param("Ki_z", params_.Ki_z, 0.01f);
    pnh.param("Kd_z", params_.Kd_z, 25.0f);

    // 速度控制
    pnh.param("Kp_vx", params_.Kp_vx, 0.5f);
    pnh.param("Kd_vx", params_.Kd_vx, 1.0f);
    
    pnh.param("Kp_vy", params_.Kp_vy, 0.5f);
    pnh.param("Kd_vy", params_.Kd_vy, 1.0f);

    // 姿态控制
    pnh.param("Kp_phi", params_.Kp_phi, 17.0f);
    pnh.param("Kd_phi", params_.Kd_phi, 940.0f);

    pnh.param("Kp_theta", params_.Kp_theta, 20.0f);
    pnh.param("Kd_theta", params_.Kd_theta, 750.0f);

    pnh.param("Kp_psi", params_.Kp_psi, 5.0f);
    pnh.param("Kd_psi", params_.Kd_psi, 250.0f);

    // 物理参数
    pnh.param("mass", params_.mass, 0.9f);
    pnh.param("gravity", params_.gravity, 9.8f);
    pnh.param("armlength", params_.armlength, 0.18f);
    pnh.param("Ct", params_.Ct, 0.0003677f);
    pnh.param("Cq", params_.Cq, 4.888e-6f);
    pnh.param("Fmax", params_.Fmax, 4.179f*3);

    // Limits
    pnh.param("max_v", params_.max_v, 2.0f);
    pnh.param("max_acc", params_.max_acc, 5.0f);
    pnh.param("max_ang", params_.max_ang, 0.5f);

    // Inertia
    pnh.param("Ixx", params_.Ixx, 0.0046890742f);
    pnh.param("Iyy", params_.Iyy, 0.0069312f);
    pnh.param("Izz", params_.Izz, 0.010421166f);
}

void PIDController::setDesiredState(const Eigen::VectorXf& X_des) {
    if(X_des.size() == 12) {
        X_des_ = X_des;
    }
}

void PIDController::odomCallback(const nav_msgs::Odometry::ConstPtr& msg) {
    Eigen::Quaternionf q(
        msg->pose.pose.orientation.w,
        msg->pose.pose.orientation.x,
        msg->pose.pose.orientation.y,
        msg->pose.pose.orientation.z
    );
    Eigen::Matrix3f R = q.normalized().toRotationMatrix();

    // Convert linear velocity to body frame
    Eigen::Vector3f global_linear_vel(
        msg->twist.twist.linear.x,
        msg->twist.twist.linear.y,
        msg->twist.twist.linear.z
    );
    Eigen::Vector3f body_linear_vel = R.transpose() * global_linear_vel;

    X_real_ << 
        msg->pose.pose.position.x,
        msg->pose.pose.position.y,
        msg->pose.pose.position.z,
        body_linear_vel.x(),
        body_linear_vel.y(),
        body_linear_vel.z(),
        R.eulerAngles(2,1,0).reverse(), // Roll, Pitch, Yaw
        msg->twist.twist.angular.x,
        msg->twist.twist.angular.y,
        msg->twist.twist.angular.z;

    has_odom_ = true;
}

Eigen::Vector4f PIDController::computePWM(const Eigen::VectorXf& X_des, const Eigen::VectorXf& X_real) {
    // 高度控制
    const float e_z = X_des[2] - X_real[2];
    integral_e_z_ += e_z;
    const float de_z = e_z - last_e_z_;
    const float u1 = params_.mass * params_.gravity + 
                    params_.mass * (params_.Kp_z * e_z + 
                                  params_.Ki_z * integral_e_z_ + 
                                  params_.Kd_z * de_z);
    last_e_z_ = e_z;

    // 水平位置控制（X方向）
    const float e_x = X_des[0] - X_real[0];
    integral_e_x_ += e_x;
    const float de_x = e_x - last_e_x_;
    float vxd = params_.Kp_x * e_x + params_.Ki_x * integral_e_x_ + params_.Kd_x * de_x;
    vxd = std::clamp(vxd, -params_.max_v, params_.max_v);
    last_e_x_ = e_x;

    const float e_vx = vxd - X_real[3];
    const float de_vx = e_vx - last_e_vx_;
    float ax = params_.Kp_vx * e_vx + params_.Kd_vx * de_vx;
    ax = std::clamp(ax, -params_.max_acc, params_.max_acc);
    last_e_vx_ = e_vx;

    // 水平位置控制（Y方向）
    const float e_y = X_des[1] - X_real[1];
    integral_e_y_ += e_y;
    const float de_y = e_y - last_e_y_;
    float vyd = params_.Kp_y * e_y + params_.Ki_y * integral_e_y_ + params_.Kd_y * de_y;
    vyd = std::clamp(vyd, -params_.max_v, params_.max_v);
    last_e_y_ = e_y;

    const float e_vy = vyd - X_real[4];
    const float de_vy = e_vy - last_e_vy_;
    float ay = params_.Kp_vy * e_vy + params_.Kd_vy * de_vy;
    ay = std::clamp(ay, -params_.max_acc, params_.max_acc);
    last_e_vy_ = e_vy;

    // 计算期望姿态
    const float psi_des = X_des[8];
    const float cos_psi = std::cos(psi_des);
    const float sin_psi = std::sin(psi_des);

    // 旋转加速度到期望偏航角坐标系
    const float ax_rotated = ax * cos_psi + ay * sin_psi;
    const float ay_rotated = -ax * sin_psi + ay * cos_psi;

    const float u1_clamped = std::max(u1, 1e-6f);
    const float theta_des = std::clamp((ax_rotated * params_.mass) / u1_clamped, -params_.max_ang, params_.max_ang);
    const float phi_des = std::clamp((-ay_rotated * params_.mass) / u1_clamped, -params_.max_ang, params_.max_ang);

    // 姿态控制
    const float e_phi = phi_des - X_real[6];
    const float w_phi = X_real[9];
    const float tau_phi = params_.Kp_phi * e_phi - params_.Kd_phi * w_phi;

    const float e_theta = theta_des - X_real[7];
    const float w_theta = X_real[10];
    const float tau_theta = params_.Kp_theta * e_theta - params_.Kd_theta * w_theta;

    const float e_psi = X_des[8] - X_real[8];
    const float w_psi = X_real[11];
    const float tau_psi = params_.Kp_psi * e_psi - params_.Kd_psi * w_psi;

    // 混控矩阵
    Eigen::Matrix4f M;
    M << 1, 1, 1, 1,
        -1, 1, 1, -1,
        -1, 1, -1, 1,
        -1, -1, 1, 1;

    Eigen::Vector4f u;
    u << u1 / params_.Ct,
         tau_phi / (params_.armlength * params_.Ct * 0.707f),
         tau_theta / (params_.armlength * params_.Ct * 0.707f),
         tau_psi / params_.Cq;

    Eigen::Vector4f thrust = params_.Ct * M.inverse() * u;

    // PWM计算
    Eigen::Vector4f pwm;
    float max_pwm = 0.0f;
    for(int i=0; i<4; ++i) {
        thrust[i] = std::max(thrust[i], 0.0f);
        pwm[i] = thrust[i] / params_.Fmax;
        pwm[i] = std::clamp(pwm[i], 0.1f, 1.0f);
        if(pwm[i] > max_pwm) max_pwm = pwm[i];
    }

    // 统一缩放
    if(max_pwm > 1.0f) {
        const float scale = 1.0f / max_pwm;
        for(int i=0; i<4; ++i) {
            pwm[i] *= scale;
            pwm[i] = std::clamp(pwm[i], 0.1f, 1.0f);
        }
    }

    return pwm;
}

void PIDController::publishPWM(const Eigen::Vector4f& pwm) {
    airsim_ros::RotorPWM msg;
    msg.rotorPWM0 = pwm[0];
    msg.rotorPWM1 = pwm[1];
    msg.rotorPWM2 = pwm[2];
    msg.rotorPWM3 = pwm[3];
    pwm_pub_.publish(msg);
    ROS_DEBUG_STREAM_THROTTLE(1, "PWM output: " << pwm[0] << ", " << pwm[1] << ", " << pwm[2] << ", " << pwm[3]);
}

void PIDController::runControlLoop() {
    if(has_odom_) {
        Eigen::Vector4f pwm = computePWM(X_des_, X_real_);
        publishPWM(pwm);
    }
}