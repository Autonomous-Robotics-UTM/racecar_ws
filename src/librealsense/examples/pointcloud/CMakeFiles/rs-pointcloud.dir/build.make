# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/model2/racecar-ws/src/librealsense

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/model2/racecar-ws/src/librealsense

# Include any dependencies generated for this target.
include examples/pointcloud/CMakeFiles/rs-pointcloud.dir/depend.make

# Include the progress variables for this target.
include examples/pointcloud/CMakeFiles/rs-pointcloud.dir/progress.make

# Include the compile flags for this target's objects.
include examples/pointcloud/CMakeFiles/rs-pointcloud.dir/flags.make

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/flags.make
examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o: examples/pointcloud/rs-pointcloud.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/model2/racecar-ws/src/librealsense/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o"
	cd /home/model2/racecar-ws/src/librealsense/examples/pointcloud && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o -c /home/model2/racecar-ws/src/librealsense/examples/pointcloud/rs-pointcloud.cpp

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.i"
	cd /home/model2/racecar-ws/src/librealsense/examples/pointcloud && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/model2/racecar-ws/src/librealsense/examples/pointcloud/rs-pointcloud.cpp > CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.i

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.s"
	cd /home/model2/racecar-ws/src/librealsense/examples/pointcloud && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/model2/racecar-ws/src/librealsense/examples/pointcloud/rs-pointcloud.cpp -o CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.s

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.requires:

.PHONY : examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.requires

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.provides: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.requires
	$(MAKE) -f examples/pointcloud/CMakeFiles/rs-pointcloud.dir/build.make examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.provides.build
.PHONY : examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.provides

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.provides.build: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o


# Object files for target rs-pointcloud
rs__pointcloud_OBJECTS = \
"CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o"

# External object files for target rs-pointcloud
rs__pointcloud_EXTERNAL_OBJECTS =

examples/pointcloud/rs-pointcloud: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o
examples/pointcloud/rs-pointcloud: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/build.make
examples/pointcloud/rs-pointcloud: librealsense2.so.2.29.0
examples/pointcloud/rs-pointcloud: third-party/glfw/src/libglfw3.a
examples/pointcloud/rs-pointcloud: /usr/lib/aarch64-linux-gnu/libGL.so
examples/pointcloud/rs-pointcloud: /usr/lib/aarch64-linux-gnu/libGLU.so
examples/pointcloud/rs-pointcloud: /usr/lib/aarch64-linux-gnu/librt.so
examples/pointcloud/rs-pointcloud: /usr/lib/aarch64-linux-gnu/libm.so
examples/pointcloud/rs-pointcloud: /usr/lib/aarch64-linux-gnu/libX11.so
examples/pointcloud/rs-pointcloud: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/model2/racecar-ws/src/librealsense/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable rs-pointcloud"
	cd /home/model2/racecar-ws/src/librealsense/examples/pointcloud && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rs-pointcloud.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/pointcloud/CMakeFiles/rs-pointcloud.dir/build: examples/pointcloud/rs-pointcloud

.PHONY : examples/pointcloud/CMakeFiles/rs-pointcloud.dir/build

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/requires: examples/pointcloud/CMakeFiles/rs-pointcloud.dir/rs-pointcloud.cpp.o.requires

.PHONY : examples/pointcloud/CMakeFiles/rs-pointcloud.dir/requires

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/clean:
	cd /home/model2/racecar-ws/src/librealsense/examples/pointcloud && $(CMAKE_COMMAND) -P CMakeFiles/rs-pointcloud.dir/cmake_clean.cmake
.PHONY : examples/pointcloud/CMakeFiles/rs-pointcloud.dir/clean

examples/pointcloud/CMakeFiles/rs-pointcloud.dir/depend:
	cd /home/model2/racecar-ws/src/librealsense && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/model2/racecar-ws/src/librealsense /home/model2/racecar-ws/src/librealsense/examples/pointcloud /home/model2/racecar-ws/src/librealsense /home/model2/racecar-ws/src/librealsense/examples/pointcloud /home/model2/racecar-ws/src/librealsense/examples/pointcloud/CMakeFiles/rs-pointcloud.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/pointcloud/CMakeFiles/rs-pointcloud.dir/depend

