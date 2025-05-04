cmake_minimum_required(VERSION 3.0.2)
project(pid_controller)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  geometry_msgs
  nav_msgs
  airsim_ros
)

find_package(Eigen3 REQUIRED)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES pid_controller
  CATKIN_DEPENDS roscpp std_msgs geometry_msgs nav_msgs airsim_ros
)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIRS}
)

add_library(pid_controller 
  src/PIDController.cpp
)

add_executable(pid_node src/pid_node.cpp)
target_link_libraries(pid_node
  ${catkin_LIBRARIES}
  pid_controller
)

install(TARGETS pid_controller pid_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)