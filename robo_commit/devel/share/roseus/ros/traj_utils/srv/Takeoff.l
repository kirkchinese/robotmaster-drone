;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::Takeoff)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'Takeoff (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::TAKEOFF")
  (make-package "TRAJ_UTILS::TAKEOFF"))
(unless (find-package "TRAJ_UTILS::TAKEOFFREQUEST")
  (make-package "TRAJ_UTILS::TAKEOFFREQUEST"))
(unless (find-package "TRAJ_UTILS::TAKEOFFRESPONSE")
  (make-package "TRAJ_UTILS::TAKEOFFRESPONSE"))

(in-package "ROS")





(defclass traj_utils::TakeoffRequest
  :super ros::object
  :slots (_waitOnLastTask ))

(defmethod traj_utils::TakeoffRequest
  (:init
   (&key
    ((:waitOnLastTask __waitOnLastTask) nil)
    )
   (send-super :init)
   (setq _waitOnLastTask __waitOnLastTask)
   self)
  (:waitOnLastTask
   (&optional (__waitOnLastTask :null))
   (if (not (eq __waitOnLastTask :null)) (setq _waitOnLastTask __waitOnLastTask)) _waitOnLastTask)
  (:serialization-length
   ()
   (+
    ;; bool _waitOnLastTask
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _waitOnLastTask
       (if _waitOnLastTask (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _waitOnLastTask
     (setq _waitOnLastTask (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass traj_utils::TakeoffResponse
  :super ros::object
  :slots (_success ))

(defmethod traj_utils::TakeoffResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass traj_utils::Takeoff
  :super ros::object
  :slots ())

(setf (get traj_utils::Takeoff :md5sum-) "3a122444608b7d9984b24a10fba10ac1")
(setf (get traj_utils::Takeoff :datatype-) "traj_utils/Takeoff")
(setf (get traj_utils::Takeoff :request) traj_utils::TakeoffRequest)
(setf (get traj_utils::Takeoff :response) traj_utils::TakeoffResponse)

(defmethod traj_utils::TakeoffRequest
  (:response () (instance traj_utils::TakeoffResponse :init)))

(setf (get traj_utils::TakeoffRequest :md5sum-) "3a122444608b7d9984b24a10fba10ac1")
(setf (get traj_utils::TakeoffRequest :datatype-) "traj_utils/TakeoffRequest")
(setf (get traj_utils::TakeoffRequest :definition-)
      "bool waitOnLastTask 
---
bool success
")

(setf (get traj_utils::TakeoffResponse :md5sum-) "3a122444608b7d9984b24a10fba10ac1")
(setf (get traj_utils::TakeoffResponse :datatype-) "traj_utils/TakeoffResponse")
(setf (get traj_utils::TakeoffResponse :definition-)
      "bool waitOnLastTask 
---
bool success
")



(provide :traj_utils/Takeoff "3a122444608b7d9984b24a10fba10ac1")


