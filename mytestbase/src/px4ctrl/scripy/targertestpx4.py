#!/usr/bin/env python
import rospy
from quadrotor_msgs.msg import PositionCommand  # Import the PositionCommand message type
import numpy as np

class PIDControllerClient:
    def __init__(self):
        self.target_pub = rospy.Publisher('/position_cmd', PositionCommand, queue_size=10)
        rospy.init_node('pid_controller_client', anonymous=True)
        rospy.loginfo("PID Controller Client Initialized")

    def set_target(self, x, y, z, vx=0.0, vy=0.0, vz=0.0, yaw=0.0):
        """Set target position, velocity, and yaw"""
        target = PositionCommand()
        target.header.stamp = rospy.Time.now()
        target.header.frame_id = "world"

        # Set position
        target.position.x = x
        target.position.y = y
        target.position.z = z

        # Set velocity
        target.velocity.x = vx
        target.velocity.y = vy
        target.velocity.z = vz

        # Set yaw
        target.yaw = yaw

        self.target_pub.publish(target)
        rospy.loginfo(f"New target set: x={x:.2f}, y={y:.2f}, z={z:.2f}, vx={vx:.2f}, vy={vy:.2f}, vz={vz:.2f}, yaw={yaw:.2f}")

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