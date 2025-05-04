;; Auto-generated. Do not edit!


(when (boundp 'traj_utils::TakeoffGroup)
  (if (not (find-package "TRAJ_UTILS"))
    (make-package "TRAJ_UTILS"))
  (shadow 'TakeoffGroup (find-package "TRAJ_UTILS")))
(unless (find-package "TRAJ_UTILS::TAKEOFFGROUP")
  (make-package "TRAJ_UTILS::TAKEOFFGROUP"))
(unless (find-package "TRAJ_UTILS::TAKEOFFGROUPREQUEST")
  (make-package "TRAJ_UTILS::TAKEOFFGROUPREQUEST"))
(unless (find-package "TRAJ_UTILS::TAKEOFFGROUPRESPONSE")
  (make-package "TRAJ_UTILS::TAKEOFFGROUPRESPONSE"))

(in-package "ROS")





(defclass traj_utils::TakeoffGroupRequest
  :super ros::object
  :slots (_vehicle_names _waitOnLastTask ))

(defmethod traj_utils::TakeoffGroupRequest
  (:init
   (&key
    ((:vehicle_names __vehicle_names) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:waitOnLastTask __waitOnLastTask) nil)
    )
   (send-super :init)
   (setq _vehicle_names __vehicle_names)
   (setq _waitOnLastTask __waitOnLastTask)
   self)
  (:vehicle_names
   (&optional __vehicle_names)
   (if __vehicle_names (setq _vehicle_names __vehicle_names)) _vehicle_names)
  (:waitOnLastTask
   (&optional (__waitOnLastTask :null))
   (if (not (eq __waitOnLastTask :null)) (setq _waitOnLastTask __waitOnLastTask)) _waitOnLastTask)
  (:serialization-length
   ()
   (+
    ;; string[] _vehicle_names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _vehicle_names)) 4
    ;; bool _waitOnLastTask
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _vehicle_names
     (write-long (length _vehicle_names) s)
     (dolist (elem _vehicle_names)
       (write-long (length elem) s) (princ elem s)
       )
     ;; bool _waitOnLastTask
       (if _waitOnLastTask (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _vehicle_names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _vehicle_names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _vehicle_names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; bool _waitOnLastTask
     (setq _waitOnLastTask (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass traj_utils::TakeoffGroupResponse
  :super ros::object
  :slots (_success ))

(defmethod traj_utils::TakeoffGroupResponse
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

(defclass traj_utils::TakeoffGroup
  :super ros::object
  :slots ())

(setf (get traj_utils::TakeoffGroup :md5sum-) "1c93c56d4ef2aa094d01d2de52397e67")
(setf (get traj_utils::TakeoffGroup :datatype-) "traj_utils/TakeoffGroup")
(setf (get traj_utils::TakeoffGroup :request) traj_utils::TakeoffGroupRequest)
(setf (get traj_utils::TakeoffGroup :response) traj_utils::TakeoffGroupResponse)

(defmethod traj_utils::TakeoffGroupRequest
  (:response () (instance traj_utils::TakeoffGroupResponse :init)))

(setf (get traj_utils::TakeoffGroupRequest :md5sum-) "1c93c56d4ef2aa094d01d2de52397e67")
(setf (get traj_utils::TakeoffGroupRequest :datatype-) "traj_utils/TakeoffGroupRequest")
(setf (get traj_utils::TakeoffGroupRequest :definition-)
      "string[] vehicle_names
bool waitOnLastTask 
---
bool success
")

(setf (get traj_utils::TakeoffGroupResponse :md5sum-) "1c93c56d4ef2aa094d01d2de52397e67")
(setf (get traj_utils::TakeoffGroupResponse :datatype-) "traj_utils/TakeoffGroupResponse")
(setf (get traj_utils::TakeoffGroupResponse :definition-)
      "string[] vehicle_names
bool waitOnLastTask 
---
bool success
")



(provide :traj_utils/TakeoffGroup "1c93c56d4ef2aa094d01d2de52397e67")


