;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::SetLocalPosition)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'SetLocalPosition (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::SETLOCALPOSITION")
  (make-package "TRAJ_UTILS::SETLOCALPOSITION"))
(unless (find-package "TRAJ_UTILS::SETLOCALPOSITIONREQUEST")
  (make-package "TRAJ_UTILS::SETLOCALPOSITIONREQUEST"))
(unless (find-package "TRAJ_UTILS::SETLOCALPOSITIONRESPONSE")
  (make-package "TRAJ_UTILS::SETLOCALPOSITIONRESPONSE"))

(in-package "ROS")





(defclass traj_utils::SetLocalPositionRequest
  :super ros::object
  :slots (_x _y _z _yaw _vehicle_name ))

(defmethod traj_utils::SetLocalPositionRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:yaw __yaw) 0.0)
    ((:vehicle_name __vehicle_name) "")
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _yaw (float __yaw))
   (setq _vehicle_name (string __vehicle_name))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:vehicle_name
   (&optional __vehicle_name)
   (if __vehicle_name (setq _vehicle_name __vehicle_name)) _vehicle_name)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _yaw
    8
    ;; string _vehicle_name
    4 (length _vehicle_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _vehicle_name
       (write-long (length _vehicle_name) s) (princ _vehicle_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _vehicle_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _vehicle_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass traj_utils::SetLocalPositionResponse
  :super ros::object
  :slots (_success _message ))

(defmethod traj_utils::SetLocalPositionResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass traj_utils::SetLocalPosition
  :super ros::object
  :slots ())

(setf (get traj_utils::SetLocalPosition :md5sum-) "23cc107c6db5068a5234b2dfe0bcf0bb")
(setf (get traj_utils::SetLocalPosition :datatype-) "traj_utils/SetLocalPosition")
(setf (get traj_utils::SetLocalPosition :request) traj_utils::SetLocalPositionRequest)
(setf (get traj_utils::SetLocalPosition :response) traj_utils::SetLocalPositionResponse)

(defmethod traj_utils::SetLocalPositionRequest
  (:response () (instance traj_utils::SetLocalPositionResponse :init)))

(setf (get traj_utils::SetLocalPositionRequest :md5sum-) "23cc107c6db5068a5234b2dfe0bcf0bb")
(setf (get traj_utils::SetLocalPositionRequest :datatype-) "traj_utils/SetLocalPositionRequest")
(setf (get traj_utils::SetLocalPositionRequest :definition-)
      "#Request : expects position setpoint via x, y, z
#Request : expects yaw setpoint via yaw (send yaw_valid=true)
float64 x
float64 y
float64 z
float64 yaw
string vehicle_name
---
#Response : success=true - (if async=false && if setpoint reached before timeout = 30sec) || (if async=true)
bool success
string message
")

(setf (get traj_utils::SetLocalPositionResponse :md5sum-) "23cc107c6db5068a5234b2dfe0bcf0bb")
(setf (get traj_utils::SetLocalPositionResponse :datatype-) "traj_utils/SetLocalPositionResponse")
(setf (get traj_utils::SetLocalPositionResponse :definition-)
      "#Request : expects position setpoint via x, y, z
#Request : expects yaw setpoint via yaw (send yaw_valid=true)
float64 x
float64 y
float64 z
float64 yaw
string vehicle_name
---
#Response : success=true - (if async=false && if setpoint reached before timeout = 30sec) || (if async=true)
bool success
string message
")



(provide :traj_utils/SetLocalPosition "23cc107c6db5068a5234b2dfe0bcf0bb")


