# Install script for directory: /home/model2/racecar-ws/src/librealsense/examples

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
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

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/model2/racecar-ws/src/librealsense/examples/hello-realsense/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/software-device/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/capture/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/callback/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/save-to-disk/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/multicam/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/pointcloud/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/align/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/align-advanced/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/sensor-control/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/measure/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/C/depth/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/C/color/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/C/distance/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/post-processing/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/record-playback/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/motion/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/gl/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/pose/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/pose-predict/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/pose-and-image/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/trajectory/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/ar-basic/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/pose-apriltag/cmake_install.cmake")
  include("/home/model2/racecar-ws/src/librealsense/examples/tracking-and-depth/cmake_install.cmake")

endif()

