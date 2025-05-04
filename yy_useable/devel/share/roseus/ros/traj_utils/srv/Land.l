;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::Land)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'Land (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::LAND")
  (make-package "TRAJ_UTILS::LAND"))
(unless (find-package "TRAJ_UTILS::LANDREQUEST")
  (make-package "TRAJ_UTILS::LANDREQUEST"))
(unless (find-package "TRAJ_UTILS::LANDRESPONSE")
  (make-package "TRAJ_UTILS::LANDRESPONSE"))

(in-package "ROS")





(defclass traj_utils::LandRequest
  :super ros::object
  :slots (_waitOnLastTask ))

(defmethod traj_utils::LandRequest
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

(defclass traj_utils::LandResponse
  :super ros::object
  :slots (_success ))

(defmethod traj_utils::LandResponse
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

(defclass traj_utils::Land
  :super ros::object
  :slots ())

(setf (get traj_utils::Land :md5sum-) "3a122444608b7d9984b24a10fba10ac1")
(setf (get traj_utils::Land :datatype-) "traj_utils/Land")
(setf (get traj_utils::Land :request) traj_utils::LandRequest)
(setf (get traj_utils::Land :response) traj_utils::LandResponse)

(defmethod traj_utils::LandRequest
  (:response () (instance traj_utils::LandResponse :init)))

(setf (get traj_utils::LandRequest :md5sum-) "3a122444608b7d9984b24a10fba10ac1")
(setf (get traj_utils::LandRequest :datatype-) "traj_utils/LandRequest")
(setf (get traj_utils::LandRequest :definition-)
      "bool waitOnLastTask 
---
bool success
")

(setf (get traj_utils::LandResponse :md5sum-) "3a122444608b7d9984b24a10fba10ac1")
(setf (get traj_utils::LandResponse :datatype-) "traj_utils/LandResponse")
(setf (get traj_utils::LandResponse :definition-)
      "bool waitOnLastTask 
---
bool success
")



(provide :traj_utils/Land "3a122444608b7d9984b24a10fba10ac1")


