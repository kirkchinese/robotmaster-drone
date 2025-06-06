#include "pd_position_controller_simple.h"
#include <Eigen/Eigen>
#include "airsim_ros/PoseCmd.h"
#include "airsim_ros/Takeoff.h"
#include "airsim_ros/Reset.h"
#include "airsim_ros/Land.h"

bool DynamicConstraints::load_from_rosparams(const ros::NodeHandle& nh)
{
    bool found = true;

    // found = found && nh.getParam("max_vel_horz_abs", max_vel_horz_abs);
    // found = found && nh.getParam("max_vel_vert_abs", max_vel_vert_abs);
    // found = found && nh.getParam("max_yaw_rate_degree", max_yaw_rate_degree);
    max_vel_horz_abs = max_vel_horz_abs;
    max_vel_vert_abs = max_vel_vert_abs;
    max_yaw_rate_degree = max_yaw_rate_degree;

    return found;
}

PIDPositionController::PIDPositionController(const ros::NodeHandle& nh, const ros::NodeHandle& nh_private)
    : nh_(nh), nh_private_(nh_private), has_home_geo_(false), reached_goal_(false), has_goal_(false), has_odom_(false), got_goal_once_(false)
{
    constraints_.load_from_rosparams(nh_);
    initialize_ros();
    reset_errors();
}

void PIDPositionController::reset_errors()
{
    prev_error_.x = 0.0;
    prev_error_.y = 0.0;
    prev_error_.z = 0.0;
    prev_error_.yaw = 0.0;
}

void PIDPositionController::initialize_ros()
{
    vel_cmd_ = airsim_ros::VelCmd();
    // ROS params
    update_control_every_n_sec = 0.005;

    // ROS publishers
    // airsim_vel_cmd_world_frame_pub_ = nh_.advertise<airsim_ros::VelCmd>("/airsim_node/drone_1/vel_cmd_world_frame", 1);
    airsim_vel_cmd_body_frame_pub_ = nh_.advertise<airsim_ros::VelCmd>("/airsim_node/drone_1/vel_cmd_body_frame", 1);
    // ROS subscribers
    airsim_odom_sub_ = nh_.subscribe("/airsim_node/drone_1/debug/pose_gt", 50, &PIDPositionController::airsim_odom_cb, this);
    //home_geopoint_sub_ = nh_.subscribe("/airsim_node/home_geo_point", 50, &PIDPositionController::home_geopoint_cb, this);
    // todo publish this under global nodehandle / "airsim node" and hide it from user
    local_position_sub_ = nh_.subscribe("/reference_path", 1, &PIDPositionController::local_position_cb, this);

    // ROS timers
    update_control_cmd_timer_ = nh_private_.createTimer(ros::Duration(update_control_every_n_sec), &PIDPositionController::update_control_cmd_timer_cb, this);

    airsim_ros::Takeoff takeoff;
    ros::ServiceClient takeoff_client;
    takeoff_client = nh_.serviceClient<airsim_ros::Takeoff>("/airsim_node/drone_1/takeoff");
    takeoff_client.call(takeoff);
    ros::Duration(2.0).sleep();
}

// void PIDPositionController::home_geopoint_cb(const airsim_ros::GPSYaw& gps_msg)
// {
//     ROS_INFO("get home geo.");
// }

float get_yaw_from_quat_msg(const geometry_msgs::Quaternion& msg)
{
    Eigen::Quaterniond q(msg.w, msg.x, msg.y, msg.z);
    Eigen::Quaterniond baseq(0.0, 1.0, 0.0, 0.0);
    Eigen::Matrix3d rmtrx = baseq.matrix() * q.matrix();
    Eigen::Vector3d euler = rmtrx.eulerAngles(2, 1, 0);
    
    Eigen::Quaterniond rq(rmtrx);
    
    double siny_cosp = 2 * (rq.w() * rq.z() + rq.x() * rq.y());
    double cosy_cosp = 1 - 2 * (rq.y() * rq.y() + rq.z() * rq.z());
    double yaw = std::atan2(siny_cosp, cosy_cosp);
    
    //std::cout << " q:" << rq.x() <<  " " << rq.y() << " " << rq.z() << " " << rq.w() << " angle:" << euler[0] << " " << euler[1] << " " << euler[2] << " yaw:" << yaw << std::endl;

    return yaw;
}

void PIDPositionController::airsim_odom_cb(const geometry_msgs::PoseStamped& odom_msg)
{
    has_odom_ = true;
    curr_position_.x = odom_msg.pose.position.x;
    curr_position_.y = odom_msg.pose.position.y;
    curr_position_.z = odom_msg.pose.position.z;
    curr_position_.yaw = utils::get_yaw_from_quat_msg(odom_msg.pose.orientation);
    // ROS_INFO("%f %f %f %f", odom_msg.orientation.w, odom_msg.orientation.x,odom_msg.orientation.y,odom_msg.orientation.z);
    // ROS_INFO("GET pose %f %f %f %f", odom_msg.position.x, odom_msg.position.y, odom_msg.position.z, curr_position_.yaw);
}

// todo maintain internal representation as eigen vec?
// todo check if low velocity if within thresh?
// todo maintain separate errors for XY and Z
void PIDPositionController::check_reached_goal()
{
    double diff_xyz = sqrt((target_position_.x - curr_position_.x) * (target_position_.x - curr_position_.x) + (target_position_.y - curr_position_.y) * (target_position_.y - curr_position_.y) + (target_position_.z - curr_position_.z) * (target_position_.z - curr_position_.z));

    double diff_yaw = math_common::angular_dist(target_position_.yaw, curr_position_.yaw);

    // todo save this in degrees somewhere to avoid repeated conversion
    if (diff_xyz < params_.reached_thresh_xyz && diff_yaw < math_common::deg2rad(params_.reached_yaw_degrees))
        reached_goal_ = true;
}

void PIDPositionController::local_position_cb(const geometry_msgs::PoseStampedPtr &msg)
{
    // this tells the update timer callback to not do active hovering
    if (!got_goal_once_)
        got_goal_once_ = true;

    target_position_.x = msg->pose.position.x;
    target_position_.y = msg->pose.position.y;
    target_position_.z = msg->pose.position.z;
    target_position_.yaw = msg->pose.orientation.x ;
    ROS_INFO_STREAM("[PIDPositionController] got goal: x=" << target_position_.x << " y=" << target_position_.y << " z=" << target_position_.z << " yaw=" << target_position_.yaw);

    // todo error checks
    // todo fill response
    has_goal_ = true;
    reached_goal_ = false;
}


void PIDPositionController::update_control_cmd_timer_cb(const ros::TimerEvent& event)
{
    // todo check if odometry is too old!!
    // if no odom, don't do anything.
    if (!has_odom_) {
        ROS_ERROR_STREAM("[PIDPositionController] Waiting for goal!");
        return;
    }

    if (has_goal_) {
        check_reached_goal();
        if (reached_goal_) {
            ROS_INFO_STREAM("[PIDPositionController] Reached goal! Hovering at position.");
            has_goal_ = false;
            // dear future self, this function doesn't return coz we need to keep on actively hovering at last goal pose. don't act smart
        }
        else {
            ROS_INFO_STREAM("[PIDPositionController] Moving to goal.");
        }
    }

    // only compute and send control commands for hovering / moving to pose, if we received a goal at least once in the past
    if (got_goal_once_) {
        compute_control_cmd();
        enforce_dynamic_constraints();
        publish_control_cmd();
    }
}

void PIDPositionController::compute_control_cmd()
{
    ROS_INFO("cur position:%f %f %f %f", curr_position_.x, curr_position_.y, curr_position_.z, curr_position_.yaw);
    ROS_INFO("tar position:%f %f %f %f", target_position_.x, target_position_.y, target_position_.z, target_position_.yaw);
    curr_error_.x = target_position_.x - curr_position_.x;
    curr_error_.y = target_position_.y - curr_position_.y;
    curr_error_.z = target_position_.z - curr_position_.z;
    curr_error_.yaw = math_common::angular_dist(curr_position_.yaw, target_position_.yaw);

    double p_term_x = params_.kp_x * curr_error_.x;
    double p_term_y = params_.kp_y * curr_error_.y;
    double p_term_z = params_.kp_z * curr_error_.z;
    double p_term_yaw = params_.kp_yaw * curr_error_.yaw;

    double d_term_x = params_.kd_x * prev_error_.x;
    double d_term_y = params_.kd_y * prev_error_.y;
    double d_term_z = params_.kd_z * prev_error_.z;
    double d_term_yaw = params_.kp_yaw * prev_error_.yaw;

    prev_error_ = curr_error_;

    double vx = p_term_x + d_term_x;
    double vy = p_term_y + d_term_y;
    double vz = p_term_z + d_term_z;
    double vyaw = p_term_yaw + d_term_yaw;

    double yaw = curr_position_.yaw + update_control_every_n_sec/2*vyaw;

    vel_cmd_.twist.linear.x = cosf64(yaw)*vx+sinf64(yaw)*vy;
    vel_cmd_.twist.linear.y = -sinf64(yaw)*vx+cosf64(yaw)*vy;
    vel_cmd_.twist.linear.z = vz;
    vel_cmd_.twist.angular.z = vyaw; // todo
    ROS_INFO("controller-init:%f %f %f %f", vel_cmd_.twist.linear.x, vel_cmd_.twist.linear.y, vel_cmd_.twist.linear.z, vel_cmd_.twist.angular.z);
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
    if (std::fabs(vel_cmd_.twist.angular.z) > constraints_.max_yaw_rate_degree) {
        // todo just add a sgn funciton in common utils? return double to be safe.
        // template <typename T> double sgn(T val) { return (T(0) < val) - (val < T(0)); }
        vel_cmd_.twist.angular.z = (vel_cmd_.twist.angular.z / std::fabs(vel_cmd_.twist.angular.z)) * constraints_.max_yaw_rate_degree;
    }
}

void PIDPositionController::publish_control_cmd()
{
    airsim_vel_cmd_body_frame_pub_.publish(vel_cmd_);
    ROS_INFO("velcmd: %f %f %f %f", vel_cmd_.twist.linear.x, vel_cmd_.twist.linear.y, vel_cmd_.twist.linear.z, vel_cmd_.twist.angular.z);
}
