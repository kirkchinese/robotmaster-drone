#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np

class PIDControllerClient:
    def __init__(self):
        self.target_pub = rospy.Publisher('/target_pose', PoseStamped, queue_size=10)
        rospy.init_node('pid_controller_client', anonymous=True)
        rospy.loginfo("PID Controller Client Initialized")

    def set_target(self, x, y, z, roll=0.0, pitch=0.0, yaw=0.0):
        """Set target position and orientation"""
        target = PoseStamped()
        target.header.stamp = rospy.Time.now()
        target.header.frame_id = "world"
        
        # Set position
        target.pose.position.x = x
        target.pose.position.y = y
        target.pose.position.z = z
        
        # Convert Euler angles to quaternion
        cy = np.cos(yaw * 0.5)
        sy = np.sin(yaw * 0.5)
        cp = np.cos(pitch * 0.5)
        sp = np.sin(pitch * 0.5)
        cr = np.cos(roll * 0.5)
        sr = np.sin(roll * 0.5)
        
        target.pose.orientation.w = cr * cp * cy + sr * sp * sy
        target.pose.orientation.x = sr * cp * cy - cr * sp * sy
        target.pose.orientation.y = cr * sp * cy + sr * cp * sy
        target.pose.orientation.z = cr * cp * sy - sr * sp * cy
        
        self.target_pub.publish(target)
        rospy.loginfo(f"New target set: x={x:.2f}, y={y:.2f}, z={z:.2f}, roll={roll:.2f}, pitch={pitch:.2f}, yaw={yaw:.2f}")

if __name__ == '__main__':
    try:
        client = PIDControllerClient()
        
        # Example usage
        rospy.sleep(1)  # Wait for publisher to initialize
        
        # Set initial target
        client.set_target(x=1.0, y=0.5, z=1.5)
        
        # # Move to new position after 5 seconds
        # rospy.sleep(5)
        # client.set_target(x=2.0, y=1.0, z=2.0, yaw=np.pi/4)
        
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass