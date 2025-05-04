;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::TopicHz)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'TopicHz (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::TOPICHZ")
  (make-package "TRAJ_UTILS::TOPICHZ"))
(unless (find-package "TRAJ_UTILS::TOPICHZREQUEST")
  (make-package "TRAJ_UTILS::TOPICHZREQUEST"))
(unless (find-package "TRAJ_UTILS::TOPICHZRESPONSE")
  (make-package "TRAJ_UTILS::TOPICHZRESPONSE"))

(in-package "ROS")





(defclass traj_utils::TopicHzRequest
  :super ros::object
  :slots (_get ))

(defmethod traj_utils::TopicHzRequest
  (:init
   (&key
    ((:get __get) 0)
    )
   (send-super :init)
   (setq _get (round __get))
   self)
  (:get
   (&optional __get)
   (if __get (setq _get __get)) _get)
  (:serialization-length
   ()
   (+
    ;; int64 _get
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _get
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _get (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _get) (= (length (_get . bv)) 2)) ;; bignum
              (write-long (ash (elt (_get . bv) 0) 0) s)
              (write-long (ash (elt (_get . bv) 1) -1) s))
             ((and (class _get) (= (length (_get . bv)) 1)) ;; big1
              (write-long (elt (_get . bv) 0) s)
              (write-long (if (>= _get 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _get s)(write-long (if (>= _get 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _get
#+(or :alpha :irix6 :x86_64)
      (setf _get (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _get (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass traj_utils::TopicHzResponse
  :super ros::object
  :slots (_vel_cmd_hz _pose_cmd_hz _angle_cmd_hz _imu_hz _image_hz ))

(defmethod traj_utils::TopicHzResponse
  (:init
   (&key
    ((:vel_cmd_hz __vel_cmd_hz) 0.0)
    ((:pose_cmd_hz __pose_cmd_hz) 0.0)
    ((:angle_cmd_hz __angle_cmd_hz) 0.0)
    ((:imu_hz __imu_hz) 0.0)
    ((:image_hz __image_hz) 0.0)
    )
   (send-super :init)
   (setq _vel_cmd_hz (float __vel_cmd_hz))
   (setq _pose_cmd_hz (float __pose_cmd_hz))
   (setq _angle_cmd_hz (float __angle_cmd_hz))
   (setq _imu_hz (float __imu_hz))
   (setq _image_hz (float __image_hz))
   self)
  (:vel_cmd_hz
   (&optional __vel_cmd_hz)
   (if __vel_cmd_hz (setq _vel_cmd_hz __vel_cmd_hz)) _vel_cmd_hz)
  (:pose_cmd_hz
   (&optional __pose_cmd_hz)
   (if __pose_cmd_hz (setq _pose_cmd_hz __pose_cmd_hz)) _pose_cmd_hz)
  (:angle_cmd_hz
   (&optional __angle_cmd_hz)
   (if __angle_cmd_hz (setq _angle_cmd_hz __angle_cmd_hz)) _angle_cmd_hz)
  (:imu_hz
   (&optional __imu_hz)
   (if __imu_hz (setq _imu_hz __imu_hz)) _imu_hz)
  (:image_hz
   (&optional __image_hz)
   (if __image_hz (setq _image_hz __image_hz)) _image_hz)
  (:serialization-length
   ()
   (+
    ;; float64 _vel_cmd_hz
    8
    ;; float64 _pose_cmd_hz
    8
    ;; float64 _angle_cmd_hz
    8
    ;; float64 _imu_hz
    8
    ;; float64 _image_hz
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _vel_cmd_hz
       (sys::poke _vel_cmd_hz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pose_cmd_hz
       (sys::poke _pose_cmd_hz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _angle_cmd_hz
       (sys::poke _angle_cmd_hz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _imu_hz
       (sys::poke _imu_hz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _image_hz
       (sys::poke _image_hz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _vel_cmd_hz
     (setq _vel_cmd_hz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pose_cmd_hz
     (setq _pose_cmd_hz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _angle_cmd_hz
     (setq _angle_cmd_hz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _imu_hz
     (setq _imu_hz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _image_hz
     (setq _image_hz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass traj_utils::TopicHz
  :super ros::object
  :slots ())

(setf (get traj_utils::TopicHz :md5sum-) "be220a7e84277b3c72a3145179becfe7")
(setf (get traj_utils::TopicHz :datatype-) "traj_utils/TopicHz")
(setf (get traj_utils::TopicHz :request) traj_utils::TopicHzRequest)
(setf (get traj_utils::TopicHz :response) traj_utils::TopicHzResponse)

(defmethod traj_utils::TopicHzRequest
  (:response () (instance traj_utils::TopicHzResponse :init)))

(setf (get traj_utils::TopicHzRequest :md5sum-) "be220a7e84277b3c72a3145179becfe7")
(setf (get traj_utils::TopicHzRequest :datatype-) "traj_utils/TopicHzRequest")
(setf (get traj_utils::TopicHzRequest :definition-)
      "int64 get
---
float64 vel_cmd_hz
float64 pose_cmd_hz
float64 angle_cmd_hz
float64 imu_hz
float64 image_hz
")

(setf (get traj_utils::TopicHzResponse :md5sum-) "be220a7e84277b3c72a3145179becfe7")
(setf (get traj_utils::TopicHzResponse :datatype-) "traj_utils/TopicHzResponse")
(setf (get traj_utils::TopicHzResponse :definition-)
      "int64 get
---
float64 vel_cmd_hz
float64 pose_cmd_hz
float64 angle_cmd_hz
float64 imu_hz
float64 image_hz
")



(provide :traj_utils/TopicHz "be220a7e84277b3c72a3145179becfe7")


