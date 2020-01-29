execute_process(COMMAND "/home/model2/racecar-ws/build/ros_numpy/ros_numpy/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/model2/racecar-ws/build/ros_numpy/ros_numpy/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
