;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::Reset)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'Reset (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::RESET")
  (make-package "TRAJ_UTILS::RESET"))
(unless (find-package "TRAJ_UTILS::RESETREQUEST")
  (make-package "TRAJ_UTILS::RESETREQUEST"))
(unless (find-package "TRAJ_UTILS::RESETRESPONSE")
  (make-package "TRAJ_UTILS::RESETRESPONSE"))

(in-package "ROS")





(defclass traj_utils::ResetRequest
  :super ros::object
  :slots ())

(defmethod traj_utils::ResetRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass traj_utils::ResetResponse
  :super ros::object
  :slots (_success ))

(defmethod traj_utils::ResetResponse
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

(defclass traj_utils::Reset
  :super ros::object
  :slots ())

(setf (get traj_utils::Reset :md5sum-) "358e233cde0c8a8bcfea4ce193f8fc15")
(setf (get traj_utils::Reset :datatype-) "traj_utils/Reset")
(setf (get traj_utils::Reset :request) traj_utils::ResetRequest)
(setf (get traj_utils::Reset :response) traj_utils::ResetResponse)

(defmethod traj_utils::ResetRequest
  (:response () (instance traj_utils::ResetResponse :init)))

(setf (get traj_utils::ResetRequest :md5sum-) "358e233cde0c8a8bcfea4ce193f8fc15")
(setf (get traj_utils::ResetRequest :datatype-) "traj_utils/ResetRequest")
(setf (get traj_utils::ResetRequest :definition-)
      "---
bool success
")

(setf (get traj_utils::ResetResponse :md5sum-) "358e233cde0c8a8bcfea4ce193f8fc15")
(setf (get traj_utils::ResetResponse :datatype-) "traj_utils/ResetResponse")
(setf (get traj_utils::ResetResponse :definition-)
      "---
bool success
")



(provide :traj_utils/Reset "358e233cde0c8a8bcfea4ce193f8fc15")


