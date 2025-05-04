#!/usr/bin/env python3
import rospy
import numpy as np
from airsim_ros.msg import RotorPWM
from mavros_msgs.msg import AttitudeTarget

class PWMTranslator:
    def __init__(self):
        self.pwm_pub = rospy.Publisher('/airsim_node/drone_1/rotor_pwm_cmd', RotorPWM, queue_size=10)
        rospy.Subscriber('/mavros/setpoint_raw/attitude', AttitudeTarget, self.att_callback)
        
        # 混控矩阵（X型四旋翼）
        self.mixer = np.array([
            [ 1,  1, -1, -1],  # 对应电机0
            [-1,  1,  1, -1],  # 对应电机1
            [ 1, -1, -1,  1],  # 对应电机2
            [-1, -1,  1,  1]   # 对应电机3
        ]) * 0.25

    def att_callback(self, msg):
        thrust = msg.thrust
        # 建议使用四元数转换欧拉角（更准确）
        from tf.transformations import euler_from_quaternion
        q = [msg.orientation.x, msg.orientation.y, 
             msg.orientation.z, msg.orientation.w]
        roll, pitch, yaw = euler_from_quaternion(q)
        
        # 混控计算
        control_vector = np.array([roll, pitch, yaw, thrust])
        pwm_values = np.dot(self.mixer, control_vector)
        
        # 限制范围并发布
        pwm_values = np.clip(pwm_values, 0.0, 1.0)
        
        pwm_msg = RotorPWM()
        pwm_msg.rotorPWM0 = float(pwm_values[0])
        pwm_msg.rotorPWM1 = float(pwm_values[1])
        pwm_msg.rotorPWM2 = float(pwm_values[2])
        pwm_msg.rotorPWM3 = float(pwm_values[3])
        
        self.pwm_pub.publish(pwm_msg)
        rospy.loginfo(f"PWM: {pwm_values}")

if __name__ == '__main__':
    rospy.init_node('pwm_translator')
    translator = PWMTranslator()
    rospy.spin()