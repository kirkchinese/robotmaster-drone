# Install script for directory: /home/misaka/drone/mytestbase/src/airsim_ros

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/misaka/drone/mytestbase/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/airsim_ros/msg" TYPE FILE FILES
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/GimbalAngleEulerCmd.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/GimbalAngleQuatCmd.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/GPSYaw.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/VelCmd.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/VelCmdGroup.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/CarControls.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/CarState.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/Altimeter.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/Environment.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/PoseCmd.msg"
    "/home/misaka/drone/mytestbase/src/airsim_ros/msg/RotorPWM.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/airsim_ros/srv" TYPE FILE FILES
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/SetGPSPosition.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/Takeoff.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/TakeoffGroup.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/Land.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/LandGroup.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/Reset.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/SetLocalPosition.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/DebugSphere.srv"
    "/home/misaka/drone/mytestbase/src/airsim_ros/srv/TriggerPort.srv"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/airsim_ros/cmake" TYPE FILE FILES "/home/misaka/drone/mytestbase/build/airsim_ros/catkin_generated/installspace/airsim_ros-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/misaka/drone/mytestbase/devel/include/airsim_ros")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/misaka/drone/mytestbase/devel/share/roseus/ros/airsim_ros")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/misaka/drone/mytestbase/devel/share/common-lisp/ros/airsim_ros")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/misaka/drone/mytestbase/devel/share/gennodejs/ros/airsim_ros")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/misaka/drone/mytestbase/devel/lib/python3/dist-packages/airsim_ros")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/misaka/drone/mytestbase/devel/lib/python3/dist-packages/airsim_ros")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/misaka/drone/mytestbase/build/airsim_ros/catkin_generated/installspace/airsim_ros.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/airsim_ros/cmake" TYPE FILE FILES "/home/misaka/drone/mytestbase/build/airsim_ros/catkin_generated/installspace/airsim_ros-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/airsim_ros/cmake" TYPE FILE FILES
    "/home/misaka/drone/mytestbase/build/airsim_ros/catkin_generated/installspace/airsim_rosConfig.cmake"
    "/home/misaka/drone/mytestbase/build/airsim_ros/catkin_generated/installspace/airsim_rosConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/airsim_ros" TYPE FILE FILES "/home/misaka/drone/mytestbase/src/airsim_ros/package.xml")
endif()

