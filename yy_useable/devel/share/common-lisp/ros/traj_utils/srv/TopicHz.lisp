; Auto-generated. Do not edit!


(cl:in-package traj_utils-srv)


;//! \htmlinclude TopicHz-request.msg.html

(cl:defclass <TopicHz-request> (roslisp-msg-protocol:ros-message)
  ((get
    :reader get
    :initarg :get
    :type cl:integer
    :initform 0))
)

(cl:defclass TopicHz-request (<TopicHz-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TopicHz-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TopicHz-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name traj_utils-srv:<TopicHz-request> is deprecated: use traj_utils-srv:TopicHz-request instead.")))

(cl:ensure-generic-function 'get-val :lambda-list '(m))
(cl:defmethod get-val ((m <TopicHz-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader traj_utils-srv:get-val is deprecated.  Use traj_utils-srv:get instead.")
  (get m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TopicHz-request>) ostream)
  "Serializes a message object of type '<TopicHz-request>"
  (cl:let* ((signed (cl:slot-value msg 'get)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TopicHz-request>) istream)
  "Deserializes a message object of type '<TopicHz-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'get) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TopicHz-request>)))
  "Returns string type for a service object of type '<TopicHz-request>"
  "traj_utils/TopicHzRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TopicHz-request)))
  "Returns string type for a service object of type 'TopicHz-request"
  "traj_utils/TopicHzRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TopicHz-request>)))
  "Returns md5sum for a message object of type '<TopicHz-request>"
  "be220a7e84277b3c72a3145179becfe7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TopicHz-request)))
  "Returns md5sum for a message object of type 'TopicHz-request"
  "be220a7e84277b3c72a3145179becfe7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TopicHz-request>)))
  "Returns full string definition for message of type '<TopicHz-request>"
  (cl:format cl:nil "int64 get~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TopicHz-request)))
  "Returns full string definition for message of type 'TopicHz-request"
  (cl:format cl:nil "int64 get~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TopicHz-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TopicHz-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TopicHz-request
    (cl:cons ':get (get msg))
))
;//! \htmlinclude TopicHz-response.msg.html

(cl:defclass <TopicHz-response> (roslisp-msg-protocol:ros-message)
  ((vel_cmd_hz
    :reader vel_cmd_hz
    :initarg :vel_cmd_hz
    :type cl:float
    :initform 0.0)
   (pose_cmd_hz
    :reader pose_cmd_hz
    :initarg :pose_cmd_hz
    :type cl:float
    :initform 0.0)
   (angle_cmd_hz
    :reader angle_cmd_hz
    :initarg :angle_cmd_hz
    :type cl:float
    :initform 0.0)
   (imu_hz
    :reader imu_hz
    :initarg :imu_hz
    :type cl:float
    :initform 0.0)
   (image_hz
    :reader image_hz
    :initarg :image_hz
    :type cl:float
    :initform 0.0))
)

(cl:defclass TopicHz-response (<TopicHz-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TopicHz-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TopicHz-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name traj_utils-srv:<TopicHz-response> is deprecated: use traj_utils-srv:TopicHz-response instead.")))

(cl:ensure-generic-function 'vel_cmd_hz-val :lambda-list '(m))
(cl:defmethod vel_cmd_hz-val ((m <TopicHz-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader traj_utils-srv:vel_cmd_hz-val is deprecated.  Use traj_utils-srv:vel_cmd_hz instead.")
  (vel_cmd_hz m))

(cl:ensure-generic-function 'pose_cmd_hz-val :lambda-list '(m))
(cl:defmethod pose_cmd_hz-val ((m <TopicHz-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader traj_utils-srv:pose_cmd_hz-val is deprecated.  Use traj_utils-srv:pose_cmd_hz instead.")
  (pose_cmd_hz m))

(cl:ensure-generic-function 'angle_cmd_hz-val :lambda-list '(m))
(cl:defmethod angle_cmd_hz-val ((m <TopicHz-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader traj_utils-srv:angle_cmd_hz-val is deprecated.  Use traj_utils-srv:angle_cmd_hz instead.")
  (angle_cmd_hz m))

(cl:ensure-generic-function 'imu_hz-val :lambda-list '(m))
(cl:defmethod imu_hz-val ((m <TopicHz-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader traj_utils-srv:imu_hz-val is deprecated.  Use traj_utils-srv:imu_hz instead.")
  (imu_hz m))

(cl:ensure-generic-function 'image_hz-val :lambda-list '(m))
(cl:defmethod image_hz-val ((m <TopicHz-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader traj_utils-srv:image_hz-val is deprecated.  Use traj_utils-srv:image_hz instead.")
  (image_hz m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TopicHz-response>) ostream)
  "Serializes a message object of type '<TopicHz-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'vel_cmd_hz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pose_cmd_hz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle_cmd_hz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'imu_hz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'image_hz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TopicHz-response>) istream)
  "Deserializes a message object of type '<TopicHz-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vel_cmd_hz) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pose_cmd_hz) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle_cmd_hz) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'imu_hz) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'image_hz) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TopicHz-response>)))
  "Returns string type for a service object of type '<TopicHz-response>"
  "traj_utils/TopicHzResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TopicHz-response)))
  "Returns string type for a service object of type 'TopicHz-response"
  "traj_utils/TopicHzResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TopicHz-response>)))
  "Returns md5sum for a message object of type '<TopicHz-response>"
  "be220a7e84277b3c72a3145179becfe7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TopicHz-response)))
  "Returns md5sum for a message object of type 'TopicHz-response"
  "be220a7e84277b3c72a3145179becfe7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TopicHz-response>)))
  "Returns full string definition for message of type '<TopicHz-response>"
  (cl:format cl:nil "float64 vel_cmd_hz~%float64 pose_cmd_hz~%float64 angle_cmd_hz~%float64 imu_hz~%float64 image_hz~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TopicHz-response)))
  "Returns full string definition for message of type 'TopicHz-response"
  (cl:format cl:nil "float64 vel_cmd_hz~%float64 pose_cmd_hz~%float64 angle_cmd_hz~%float64 imu_hz~%float64 image_hz~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TopicHz-response>))
  (cl:+ 0
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TopicHz-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TopicHz-response
    (cl:cons ':vel_cmd_hz (vel_cmd_hz msg))
    (cl:cons ':pose_cmd_hz (pose_cmd_hz msg))
    (cl:cons ':angle_cmd_hz (angle_cmd_hz msg))
    (cl:cons ':imu_hz (imu_hz msg))
    (cl:cons ':image_hz (image_hz msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TopicHz)))
  'TopicHz-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TopicHz)))
  'TopicHz-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TopicHz)))
  "Returns string type for a service object of type '<TopicHz>"
  "traj_utils/TopicHz")