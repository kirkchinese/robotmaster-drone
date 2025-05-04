# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "traj_utils: 7 messages, 8 services")

set(MSG_I_FLAGS "-Itraj_utils:/home/misaka/drone/yy_useable/src/planner/traj_utils/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(traj_utils_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" "geometry_msgs/Point:traj_utils/Bspline"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" "geometry_msgs/Vector3:geometry_msgs/Twist"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" "geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" "geometry_msgs/Vector3:std_msgs/Header"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" "traj_utils/Circle:std_msgs/Header:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" ""
)

get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" NAME_WE)
add_custom_target(_traj_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "traj_utils" "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_msg_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg"
  "${MSG_I_FLAGS}"
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)

### Generating Services
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)
_generate_srv_cpp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
)

### Generating Module File
_generate_module_cpp(traj_utils
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(traj_utils_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(traj_utils_generate_messages traj_utils_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_cpp _traj_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(traj_utils_gencpp)
add_dependencies(traj_utils_gencpp traj_utils_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS traj_utils_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_msg_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg"
  "${MSG_I_FLAGS}"
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)

### Generating Services
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)
_generate_srv_eus(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
)

### Generating Module File
_generate_module_eus(traj_utils
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(traj_utils_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(traj_utils_generate_messages traj_utils_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_eus _traj_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(traj_utils_geneus)
add_dependencies(traj_utils_geneus traj_utils_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS traj_utils_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_msg_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg"
  "${MSG_I_FLAGS}"
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)

### Generating Services
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)
_generate_srv_lisp(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
)

### Generating Module File
_generate_module_lisp(traj_utils
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(traj_utils_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(traj_utils_generate_messages traj_utils_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_lisp _traj_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(traj_utils_genlisp)
add_dependencies(traj_utils_genlisp traj_utils_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS traj_utils_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_msg_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg"
  "${MSG_I_FLAGS}"
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)

### Generating Services
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)
_generate_srv_nodejs(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
)

### Generating Module File
_generate_module_nodejs(traj_utils
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(traj_utils_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(traj_utils_generate_messages traj_utils_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_nodejs _traj_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(traj_utils_gennodejs)
add_dependencies(traj_utils_gennodejs traj_utils_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS traj_utils_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_msg_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg"
  "${MSG_I_FLAGS}"
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)

### Generating Services
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)
_generate_srv_py(traj_utils
  "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
)

### Generating Module File
_generate_module_py(traj_utils
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(traj_utils_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(traj_utils_generate_messages traj_utils_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv" NAME_WE)
add_dependencies(traj_utils_generate_messages_py _traj_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(traj_utils_genpy)
add_dependencies(traj_utils_genpy traj_utils_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS traj_utils_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/traj_utils
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(traj_utils_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(traj_utils_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/traj_utils
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(traj_utils_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(traj_utils_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/traj_utils
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(traj_utils_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(traj_utils_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/traj_utils
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(traj_utils_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(traj_utils_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/traj_utils
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(traj_utils_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(traj_utils_generate_messages_py geometry_msgs_generate_messages_py)
endif()
