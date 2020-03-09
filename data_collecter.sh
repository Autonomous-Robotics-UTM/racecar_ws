source devel/setup.bash

# to use depth information, use below line comment out others
rosrun realsense2_camera record_data.py depth:=true

# to use regular images, use below line comment out others
#rosrun realsense2_camera record_data.py
