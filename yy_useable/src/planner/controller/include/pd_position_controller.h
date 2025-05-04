#ifndef _PID_POSITION_CONTROLLER_H_
#define _PID_POSITION_CONTROLLER_H_


#include <ros/ros.h>
#include <tf2/LinearMath/Matrix3x3.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/Pose.h>
#include <math.h>
#include "traj_utils/VelCmd.h"
#include <math_common.h>

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
    double ki_x;
    double ki_y;
    double ki_z;
    double ki_yaw;

    double reached_thresh_xyz;
    double reached_yaw_degrees;

    PIDParams()
        : kp_x(1), kp_y(1), kp_z(1), kp_yaw(1), kd_x(0.8), kd_y(0.8), kd_z(0.8), kd_yaw(0.5), ki_x(0.0), ki_y(0.0), ki_z(0.0), ki_yaw(0.0), reached_thresh_xyz(1), reached_yaw_degrees(4.0)
        //: kp_x(0.02), kp_y(0.02), kp_z(0.02), kp_yaw(0.02), kd_x(0), kd_y(0), kd_z(0), kd_yaw(0), ki_x(0.001), ki_y(0.001), ki_z(0.001), ki_yaw(0.001), reached_thresh_xyz(1), reached_yaw_degrees(5.0)
        //: kp_x(2.16), kp_y(2.16), kp_z(2.16), kp_yaw(2.16), kd_x(0), kd_y(0), kd_z(0), kd_yaw(0), ki_x(0.0001), ki_y(0.0001), ki_z(0.0001), ki_yaw(0.0001), reached_thresh_xyz(1), reached_yaw_degrees(5.0) //15m/s
        //: kp_x(0.045), kp_y(0.045), kp_z(0.045), kp_yaw(0.045), kd_x(0.1), kd_y(0.1), kd_z(0.1), kd_yaw(0.1), ki_x(0.002), ki_y(0.002), ki_z(0.002), ki_yaw(0.002), reached_thresh_xyz(1), reached_yaw_degrees(5.0)
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
        : max_vel_horz_abs(1.8), max_vel_vert_abs(1.8), max_yaw_rate_degree(3)
    {
    }

    bool load_from_rosparams(const ros::NodeHandle& nh);
};

class PIDPositionController
{
public:
    traj_utils::VelCmd vel_cmd_;

    void compute_control_cmd(XYZYaw &current, XYZYaw &target, double t);
    void enforce_dynamic_constraints();
    void reset_errors();
    
private:
    DynamicConstraints constraints_;
    PIDParams params_;
    XYZYaw prev_error_;
    XYZYaw curr_error_;
    XYZYaw integral_;
};

#endif /* _PID_POSITION_CONTROLLER_H_*/
