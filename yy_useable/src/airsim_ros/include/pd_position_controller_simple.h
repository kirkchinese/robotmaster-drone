#ifndef _PID_POSITION_CONTROLLER_SIMPLE_H_
#define _PID_POSITION_CONTROLLER_SIMPLE_H_


#include <ros/ros.h>
#include <tf2/LinearMath/Matrix3x3.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseStamped.h>
#include <math.h>
#include <airsim_ros/VelCmd.h>
#include <airsim_ros/SetLocalPosition.h>
#include <airsim_ros/SetGPSPosition.h>
#include <airsim_ros/GPSYaw.h>
#include <math_common.h>
#include <utils.h>

    // todo nicer api
class PIDParams
{
public:
    double kp_x;
    double kp_y;
    double kp_z;
    double kp_yaw;
    double kd_x;
    double kd_y;
    double kd_z;
    double kd_yaw;

    double reached_thresh_xyz;
    double reached_yaw_degrees;

    PIDParams()
        : kp_x(1.2), kp_y(1.2), kp_z(1.2), kp_yaw(2), kd_x(0.8), kd_y(0.8), kd_z(0.8), kd_yaw(0.5), reached_thresh_xyz(1), reached_yaw_degrees(5.0)
    {
    }

};

// todo should be a common representation
struct XYZYaw
{
    double x;
    double y;
    double z;
    double yaw;
};

// todo should be a common representation
class DynamicConstraints
{
public:
    double max_vel_horz_abs; // meters/sec
    double max_vel_vert_abs;
    double max_yaw_rate_degree;

    DynamicConstraints()
        : max_vel_horz_abs(1.2), max_vel_vert_abs(1.2), max_yaw_rate_degree(0.1)
    {
    }

    bool load_from_rosparams(const ros::NodeHandle& nh);
};

class PIDPositionController
{
public:
    PIDPositionController(const ros::NodeHandle& nh, const ros::NodeHandle& nh_private);

    // ROS subscriber callbacks
    void airsim_odom_cb(const geometry_msgs::PoseStamped& odom_msg);
    void local_position_cb(const geometry_msgs::PoseStampedPtr &msg);
    //void home_geopoint_cb(const airsim_ros::GPSYaw& gps_msg);

    void update_control_cmd_timer_cb(const ros::TimerEvent& event);

    void reset_errors();

    void initialize_ros();
    void compute_control_cmd();
    void enforce_dynamic_constraints();
    void publish_control_cmd();
    void check_reached_goal();

private:
    // msr::airlib::GeodeticConverter geodetic_converter_;
    static constexpr bool use_eth_lib_for_geodetic_conv_ = true;

    ros::NodeHandle nh_;
    ros::NodeHandle nh_private_;

    DynamicConstraints constraints_;
    PIDParams params_;
    XYZYaw target_position_;
    XYZYaw curr_position_;
    XYZYaw prev_error_;
    XYZYaw curr_error_;

    bool has_home_geo_;
    airsim_ros::GPSYaw gps_home_msg_;

    double update_control_every_n_sec;

    airsim_ros::VelCmd vel_cmd_;
    bool reached_goal_;
    bool has_goal_;
    bool has_odom_;
    bool got_goal_once_;
    // todo check for odom msg being older than n sec

    // ros::Publisher airsim_vel_cmd_world_frame_pub_;
    ros::Publisher airsim_vel_cmd_body_frame_pub_;
    ros::Subscriber airsim_odom_sub_;
    ros::Subscriber local_position_sub_;
    ros::Subscriber home_geopoint_sub_;

    ros::Timer update_control_cmd_timer_;
};

#endif /* _PID_POSITION_CONTROLLER_SIMPLE_ */
