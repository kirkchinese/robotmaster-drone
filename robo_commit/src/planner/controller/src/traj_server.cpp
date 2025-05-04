#include "bspline_opt/uniform_bspline.h"
#include "nav_msgs/Odometry.h"
#include "traj_utils/Bspline.h"
#include "quadrotor_msgs/PositionCommand.h"
#include "std_msgs/Empty.h"
#include "visualization_msgs/Marker.h"
#include "traj_utils/VelCmd.h"
#include <ros/ros.h>
#include "traj_utils/Takeoff.h"
#include "traj_utils/Reset.h"
#include "traj_utils/Land.h"
#include "pd_position_controller.h"
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>
#include <stdio.h>

ros::Publisher pos_cmd_pub;
ros::Publisher airsim_vel_cmd_body_frame_pub_;

ros::ServiceClient takeoff_client;
traj_utils::Takeoff takeoff;
ros::ServiceClient land_client;
traj_utils::Land land;

quadrotor_msgs::PositionCommand cmd;

PIDPositionController ctrl;

double pos_gain[3] = {0, 0, 0};
double vel_gain[3] = {0, 0, 0};

using ego_planner::UniformBspline;

bool receive_traj_ = false;
vector<UniformBspline> traj_;
double traj_duration_;
ros::Time start_time_;
int traj_id_;

// yaw control
double last_yaw_, last_yaw_dot_;
double time_forward_;

double update_control_every_n_sec = 0.01;
bool have_odom_ = false;
XYZYaw curr_position_;

void bsplineCallback(traj_utils::BsplineConstPtr msg)
{
  // parse pos traj

  Eigen::MatrixXd pos_pts(3, msg->pos_pts.size());

  Eigen::VectorXd knots(msg->knots.size());
  for (size_t i = 0; i < msg->knots.size(); ++i)
  {
    knots(i) = msg->knots[i];
  }

  for (size_t i = 0; i < msg->pos_pts.size(); ++i)
  {
    pos_pts(0, i) = msg->pos_pts[i].x;
    pos_pts(1, i) = -msg->pos_pts[i].y;
    pos_pts(2, i) = -msg->pos_pts[i].z;
  }

  UniformBspline pos_traj(pos_pts, msg->order, 0.1);
  pos_traj.setKnot(knots);

  // parse yaw traj

  // Eigen::MatrixXd yaw_pts(msg->yaw_pts.size(), 1);
  // for (int i = 0; i < msg->yaw_pts.size(); ++i) {
  //   yaw_pts(i, 0) = msg->yaw_pts[i];
  // }

  //UniformBspline yaw_traj(yaw_pts, msg->order, msg->yaw_dt);

  start_time_ = msg->start_time;
  traj_id_ = msg->traj_id;

  traj_.clear();
  traj_.push_back(pos_traj);
  traj_.push_back(traj_[0].getDerivative());
  traj_.push_back(traj_[1].getDerivative());

  traj_duration_ = traj_[0].getTimeSum();

  receive_traj_ = true;
}

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

void odometryCallback(const nav_msgs::OdometryConstPtr &msg)
{
    curr_position_.x = msg->pose.pose.position.x;
    curr_position_.y = -msg->pose.pose.position.y;
    curr_position_.z = -msg->pose.pose.position.z;
    curr_position_.yaw = get_yaw_from_quat_msg(msg->pose.pose.orientation);
    have_odom_ = true;
}

std::pair<double, double> calculate_yaw(double t_cur, Eigen::Vector3d &pos, ros::Time &time_now, ros::Time &time_last)
{
  constexpr double PI = 3.1415926;
  constexpr double YAW_DOT_MAX_PER_SEC = PI;
  // constexpr double YAW_DOT_DOT_MAX_PER_SEC = PI;
  std::pair<double, double> yaw_yawdot(0, 0);
  double yaw = 0;
  double yawdot = 0;

  Eigen::Vector3d dir = t_cur + time_forward_ <= traj_duration_ ? traj_[0].evaluateDeBoorT(t_cur + time_forward_) - pos : traj_[0].evaluateDeBoorT(traj_duration_) - pos;
  double yaw_temp = dir.norm() > 0.1 ? atan2(dir(1), dir(0)) : last_yaw_;
  double max_yaw_change = YAW_DOT_MAX_PER_SEC * (time_now - time_last).toSec();
  if (yaw_temp - last_yaw_ > PI)
  {
    if (yaw_temp - last_yaw_ - 2 * PI < -max_yaw_change)
    {
      yaw = last_yaw_ - max_yaw_change;
      if (yaw < -PI)
        yaw += 2 * PI;

      yawdot = -YAW_DOT_MAX_PER_SEC;
    }
    else
    {
      yaw = yaw_temp;
      if (yaw - last_yaw_ > PI)
        yawdot = -YAW_DOT_MAX_PER_SEC;
      else
        yawdot = (yaw_temp - last_yaw_) / (time_now - time_last).toSec();
    }
  }
  else if (yaw_temp - last_yaw_ < -PI)
  {
    if (yaw_temp - last_yaw_ + 2 * PI > max_yaw_change)
    {
      yaw = last_yaw_ + max_yaw_change;
      if (yaw > PI)
        yaw -= 2 * PI;

      yawdot = YAW_DOT_MAX_PER_SEC;
    }
    else
    {
      yaw = yaw_temp;
      if (yaw - last_yaw_ < -PI)
        yawdot = YAW_DOT_MAX_PER_SEC;
      else
        yawdot = (yaw_temp - last_yaw_) / (time_now - time_last).toSec();
    }
  }
  else
  {
    if (yaw_temp - last_yaw_ < -max_yaw_change)
    {
      yaw = last_yaw_ - max_yaw_change;
      if (yaw < -PI)
        yaw += 2 * PI;

      yawdot = -YAW_DOT_MAX_PER_SEC;
    }
    else if (yaw_temp - last_yaw_ > max_yaw_change)
    {
      yaw = last_yaw_ + max_yaw_change;
      if (yaw > PI)
        yaw -= 2 * PI;

      yawdot = YAW_DOT_MAX_PER_SEC;
    }
    else
    {
      yaw = yaw_temp;
      if (yaw - last_yaw_ > PI)
        yawdot = -YAW_DOT_MAX_PER_SEC;
      else if (yaw - last_yaw_ < -PI)
        yawdot = YAW_DOT_MAX_PER_SEC;
      else
        yawdot = (yaw_temp - last_yaw_) / (time_now - time_last).toSec();
    }
  }

  if (fabs(yaw - last_yaw_) <= max_yaw_change)
    yaw = 0.5 * last_yaw_ + 0.5 * yaw; // nieve LPF
  yawdot = 0.5 * last_yaw_dot_ + 0.5 * yawdot;
  last_yaw_ = yaw;
  last_yaw_dot_ = yawdot;

  yaw_yawdot.first = yaw;
  yaw_yawdot.second = yawdot;

  return yaw_yawdot;
}

void cmdCallback(const ros::TimerEvent &e)
{
  /* no publishing before receive traj_ */
  if (!receive_traj_ || !have_odom_)
    return;

  ros::Time time_now = ros::Time::now();
  double t_cur = (time_now - start_time_).toSec();

  Eigen::Vector3d pos(Eigen::Vector3d::Zero()), vel(Eigen::Vector3d::Zero()), acc(Eigen::Vector3d::Zero()), pos_f;
  std::pair<double, double> yaw_yawdot(0, 0);

  static ros::Time time_last = ros::Time::now();
  if (t_cur < traj_duration_ && t_cur >= 0.0)
  {
    pos = traj_[0].evaluateDeBoorT(t_cur);
    vel = traj_[1].evaluateDeBoorT(t_cur);
    acc = traj_[2].evaluateDeBoorT(t_cur);

    yaw_yawdot = calculate_yaw(t_cur, pos, time_now, time_last);
    XYZYaw target_;
    // /*
    target_.x = pos[0];
    target_.y = pos[1];
    target_.z = pos[2];
    target_.yaw = yaw_yawdot.first;
    // */
    //17.000000 6.000000 -1.500000 0.000000
    /*
    target_.x = 17.0;
    target_.y = 6.0;
    target_.z = -1.5;
    target_.yaw = 0.0;
    */
    last_yaw_ = yaw_yawdot.first;
    ctrl.compute_control_cmd(curr_position_, target_, update_control_every_n_sec);
    ctrl.enforce_dynamic_constraints();
  }
  else if (t_cur >= traj_duration_)
  {
    std::cerr <<  "=========hover when finish traj_" << std::endl;
    //exit(0);
    /* hover when finish traj_ */
    pos = traj_[0].evaluateDeBoorT(traj_duration_);
    XYZYaw target_;

    target_.x = pos[0];
    target_.y = pos[1];
    target_.z = pos[2];
    target_.yaw = last_yaw_;

    ctrl.compute_control_cmd(curr_position_, target_, update_control_every_n_sec);
    ctrl.enforce_dynamic_constraints();
  }
  else
  {
    cout << "[Traj server]: invalid time." << endl;
  }
  time_last = time_now;

  airsim_vel_cmd_body_frame_pub_.publish(ctrl.vel_cmd_);
  char buf[4096];
  sprintf(buf, "velcmd: %f %f %f %f", ctrl.vel_cmd_.twist.linear.x, ctrl.vel_cmd_.twist.linear.y, ctrl.vel_cmd_.twist.linear.z, ctrl.vel_cmd_.twist.angular.z);
  std::cerr << buf << std::endl;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "traj_server");
  // ros::NodeHandle node;
  ros::NodeHandle nh("~");

  ros::Subscriber bspline_sub = nh.subscribe("planning/bspline", 10, bsplineCallback);
  ros::Subscriber odom_sub = nh.subscribe("/vins_fusion/imu_propagate", 10, odometryCallback);

  pos_cmd_pub = nh.advertise<quadrotor_msgs::PositionCommand>("/position_cmd", 50);
  airsim_vel_cmd_body_frame_pub_ = nh.advertise<traj_utils::VelCmd>("/airsim_node/drone_1/vel_cmd_body_frame", 50);

  takeoff_client = nh.serviceClient<traj_utils::Takeoff>("/airsim_node/drone_1/takeoff");
  takeoff_client.call(takeoff);

  ros::Duration(1.0).sleep();
  //上 ros::Duration (1.0) 改为10.0 下两行解除注释便可以降落 反之则禁用降落
  //land_client = nh.serviceClient<traj_utils::Land>("/airsim_node/drone_1/land");
  //land_client.call(land);
  
  ros::Timer cmd_timer = nh.createTimer(ros::Duration(update_control_every_n_sec), cmdCallback);

  /* control parameter */

  nh.param("traj_server/time_forward", time_forward_, -1.0);
  last_yaw_ = 0.0;
  last_yaw_dot_ = 0.0;

  ros::Duration(1.0).sleep();

  ROS_WARN("[Traj server]: ready.");

  ros::spin();

  return 0;
}
