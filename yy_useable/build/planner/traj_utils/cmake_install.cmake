# Install script for directory: /home/misaka/drone/yy_useable/src/planner/traj_utils

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/misaka/drone/yy_useable/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/traj_utils/msg" TYPE FILE FILES
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Bspline.msg"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/DataDisp.msg"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/MultiBsplines.msg"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/VelCmd.msg"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/Circle.msg"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/TreePoses.msg"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/msg/CirclePoses.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/traj_utils/srv" TYPE FILE FILES
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetGPSPosition.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Takeoff.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TakeoffGroup.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Land.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/LandGroup.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/Reset.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/SetLocalPosition.srv"
    "/home/misaka/drone/yy_useable/src/planner/traj_utils/srv/TopicHz.srv"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/traj_utils/cmake" TYPE FILE FILES "/home/misaka/drone/yy_useable/build/planner/traj_utils/catkin_generated/installspace/traj_utils-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/misaka/drone/yy_useable/devel/include/traj_utils")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/misaka/drone/yy_useable/devel/share/roseus/ros/traj_utils")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/misaka/drone/yy_useable/devel/share/common-lisp/ros/traj_utils")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/misaka/drone/yy_useable/devel/share/gennodejs/ros/traj_utils")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/misaka/drone/yy_useable/devel/lib/python3/dist-packages/traj_utils")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/misaka/drone/yy_useable/devel/lib/python3/dist-packages/traj_utils")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/misaka/drone/yy_useable/build/planner/traj_utils/catkin_generated/installspace/traj_utils.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/traj_utils/cmake" TYPE FILE FILES "/home/misaka/drone/yy_useable/build/planner/traj_utils/catkin_generated/installspace/traj_utils-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/traj_utils/cmake" TYPE FILE FILES
    "/home/misaka/drone/yy_useable/build/planner/traj_utils/catkin_generated/installspace/traj_utilsConfig.cmake"
    "/home/misaka/drone/yy_useable/build/planner/traj_utils/catkin_generated/installspace/traj_utilsConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/traj_utils" TYPE FILE FILES "/home/misaka/drone/yy_useable/src/planner/traj_utils/package.xml")
endif()

