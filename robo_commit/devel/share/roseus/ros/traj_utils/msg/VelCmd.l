;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::VelCmd)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'VelCmd (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::VELCMD")
  (make-package "TRAJ_UTILS::VELCMD"))

(in-package "ROS")
;;//! \htmlinclude VelCmd.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass traj_utils::VelCmd
  :super ros::object
  :slots (_twist ))

(defmethod traj_utils::VelCmd
  (:init
   (&key
    ((:twist __twist) (instance geometry_msgs::Twist :init))
    )
   (send-super :init)
   (setq _twist __twist)
   self)
  (:twist
   (&rest __twist)
   (if (keywordp (car __twist))
       (send* _twist __twist)
     (progn
       (if __twist (setq _twist (car __twist)))
       _twist)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Twist _twist
    (send _twist :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Twist _twist
       (send _twist :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Twist _twist
     (send _twist :deserialize buf ptr-) (incf ptr- (send _twist :serialization-length))
   ;;
   self)
  )

(setf (get traj_utils::VelCmd :md5sum-) "a787b2802160dcc7fe02d089e10afe56")
(setf (get traj_utils::VelCmd :datatype-) "traj_utils/VelCmd")
(setf (get traj_utils::VelCmd :definition-)
      "geometry_msgs/Twist twist
# string vehicle_name
================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :traj_utils/VelCmd "a787b2802160dcc7fe02d089e10afe56")


