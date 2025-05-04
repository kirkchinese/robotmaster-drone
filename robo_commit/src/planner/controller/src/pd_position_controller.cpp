#include "pd_position_controller.h"
#include <stdio.h>

bool DynamicConstraints::load_from_rosparams(const ros::NodeHandle& nh)
{
    bool found = true;
    return found;
}

void PIDPositionController::reset_errors()
{
    prev_error_.x = 0.0;
    prev_error_.y = 0.0;
    prev_error_.z = 0.0;
    prev_error_.yaw = 0.0;
    integral_.x = 0.0;
    integral_.y = 0.0;
    integral_.z = 0.0;
    integral_.yaw = 0.0;
}

void PIDPositionController::compute_control_cmd(XYZYaw &curr_position_, XYZYaw &target_position_, double update_control_every_n_sec)
{
    char buf[4096];
    sprintf(buf, "tt:%lf cur position:%f %f %f %f", ros::Time::now().toSec(), curr_position_.x, curr_position_.y, curr_position_.z, curr_position_.yaw);
    std::cerr << buf << std::endl;
    sprintf(buf, "tt:%lf tar position:%f %f %f %f", ros::Time::now().toSec(), target_position_.x, target_position_.y, target_position_.z, target_position_.yaw);
    std::cerr << buf << std::endl;
    curr_error_.x = target_position_.x - curr_position_.x;/* the error of now*/
    curr_error_.y = target_position_.y - curr_position_.y;
    curr_error_.z = target_position_.z - curr_position_.z;
    curr_error_.yaw = math_common::angular_dist(curr_position_.yaw, target_position_.yaw);

    double p_term_x = params_.kp_x * curr_error_.x;/*Get the term of P and D*/
    double p_term_y = params_.kp_y * curr_error_.y;
    double p_term_z = params_.kp_z * curr_error_.z;
    double p_term_yaw = params_.kp_yaw * curr_error_.yaw;

    double d_term_x = params_.kd_x * prev_error_.x;
    double d_term_y = params_.kd_y * prev_error_.y;
    double d_term_z = params_.kd_z * prev_error_.z;
    double d_term_yaw = params_.kd_yaw * prev_error_.yaw;

    prev_error_ = curr_error_; /*make the past same as now*/
    
    /*integral*/
    integral_.x = integral_.x + curr_error_.x  ; /*Get the integral*/
    integral_.y = integral_.y + curr_error_.y ;
    integral_.z = integral_.z + curr_error_.z ;
    integral_.yaw = integral_.yaw + curr_error_.yaw ;

    double i_term_x = params_.ki_x * integral_.x;
    double i_term_y = params_.ki_y * integral_.y;
    double i_term_z = params_.ki_z * integral_.z;
    double i_term_yaw = params_.ki_yaw * integral_.yaw;


    double vx = p_term_x + d_term_x + i_term_x ;
    double vy = p_term_y + d_term_y + i_term_y ;
    double vz = p_term_z + d_term_z + i_term_z ;
    double vyaw = p_term_yaw + d_term_yaw + i_term_yaw ;

    double yaw = curr_position_.yaw + update_control_every_n_sec/2*vyaw;

    vel_cmd_.twist.linear.x = cosf64(yaw)*vx+sinf64(yaw)*vy;
    vel_cmd_.twist.linear.y = -sinf64(yaw)*vx+cosf64(yaw)*vy;
    vel_cmd_.twist.linear.z = vz;
    vel_cmd_.twist.angular.z = vyaw; // todo
    sprintf(buf, "controller-init:%f %f %f %f", vel_cmd_.twist.linear.x, vel_cmd_.twist.linear.y, vel_cmd_.twist.linear.z, vel_cmd_.twist.angular.z);
    std::cerr << buf << std::endl;
}

void PIDPositionController::enforce_dynamic_constraints()
{
    double vel_norm_horz = sqrt((vel_cmd_.twist.linear.x * vel_cmd_.twist.linear.x) + (vel_cmd_.twist.linear.y * vel_cmd_.twist.linear.y));

    if (vel_norm_horz > constraints_.max_vel_horz_abs) {
        vel_cmd_.twist.linear.x = (vel_cmd_.twist.linear.x / vel_norm_horz) * constraints_.max_vel_horz_abs;
        vel_cmd_.twist.linear.y = (vel_cmd_.twist.linear.y / vel_norm_horz) * constraints_.max_vel_horz_abs;
    }

    if (std::fabs(vel_cmd_.twist.linear.z) > constraints_.max_vel_vert_abs) {
        // todo just add a sgn funciton in common utils? return double to be safe.
        // template <typename T> double sgn(T val) { return (T(0) < val) - (val < T(0)); }
        vel_cmd_.twist.linear.z = (vel_cmd_.twist.linear.z / std::fabs(vel_cmd_.twist.linear.z)) * constraints_.max_vel_vert_abs;
    }
    // todo yaw limits
    if (std::fabs(vel_cmd_.twist.linear.z) > constraints_.max_yaw_rate_degree) {
        // todo just add a sgn funciton in common utils? return double to be safe.
        // template <typename T> double sgn(T val) { return (T(0) < val) - (val < T(0)); }
        vel_cmd_.twist.linear.z = (vel_cmd_.twist.linear.z / std::fabs(vel_cmd_.twist.linear.z)) * constraints_.max_yaw_rate_degree;
    }
}
