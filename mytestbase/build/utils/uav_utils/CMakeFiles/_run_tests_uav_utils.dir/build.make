# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.30

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Produce verbose output by default.
VERBOSE = 1

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/misaka/.local/lib/python3.8/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/misaka/.local/lib/python3.8/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/misaka/drone/mytestbase/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/misaka/drone/mytestbase/build

# Utility rule file for _run_tests_uav_utils.

# Include any custom commands dependencies for this target.
include utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/compiler_depend.make

# Include the progress variables for this target.
include utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/progress.make

_run_tests_uav_utils: utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/build.make
.PHONY : _run_tests_uav_utils

# Rule to build all files generated by this target.
utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/build: _run_tests_uav_utils
.PHONY : utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/build

utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/clean:
	cd /home/misaka/drone/mytestbase/build/utils/uav_utils && $(CMAKE_COMMAND) -P CMakeFiles/_run_tests_uav_utils.dir/cmake_clean.cmake
.PHONY : utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/clean

utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/depend:
	cd /home/misaka/drone/mytestbase/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/misaka/drone/mytestbase/src /home/misaka/drone/mytestbase/src/utils/uav_utils /home/misaka/drone/mytestbase/build /home/misaka/drone/mytestbase/build/utils/uav_utils /home/misaka/drone/mytestbase/build/utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : utils/uav_utils/CMakeFiles/_run_tests_uav_utils.dir/depend

