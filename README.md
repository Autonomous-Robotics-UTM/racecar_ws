# Documentation:

## Setting up the car:

Electronic components used on cars:
- Jetson AGX Xavier
- Hokuyo Rangefinder
- Intel RealSense Depth Camera D435i
- Sparkfun IMU 9dof
- VESC 6 Plus Speed Controller

Overview: http://bwsi-racecar.com/

Assembly instructions: https://racecarj.com/pages/build-instructions

Add to your `.bashrc` file:

```
# CUDA settings
export PATH=/usr/local/cuda-10.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH

# ROS settings
export ROS_HOME=~/.ros
source /opt/ros/melodic/setup.bash
source ~/racecar_ws/devel/setup.bash

# change these according to your usage

# ethernet
#export ROS_MASTER_URI=http://localhost:11311
#export ROS_IP=142.1.44.127 192.168.55.1

# hokuyo without internet
#export ROS_MASTER_URI=http://localhost:11311
#export ROS_IP=192.168.0.15

# hokuyo with wifi
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=192.168.55.1
```

## Running the program on the car

### Setup

Before running any of the modes below, we must first connect a keyboard, mouse and screen to the cars and log in. After doing so, make sure that you are connected to the ROS network.

### Teleoperated Mode

To start driving the car with a gamepad, open a terminal and run the following code:

```
cd ~/racecar_ws/
. launch.sh
```

To drive the car with a Logitech DualAction controller, make sure to hold the left bumper. The left bumper acts as a dead man's switch, so the car will only take commands when it is pressed. When the left bumper is released, the car halts and stops responding. To drive the car, tilt the left joystick forwards and backwards. To steer the car, tilt the right joystick left and right.

### Teleoperated Mode for Image Collection

To collect labeled data, open up three terminals and run the following commands:

*Terminal 1*
```
cd ~/racecar_ws/
. launch.sh
```

*Terminal 2*
```
cd ~/racecar_ws/
. camera.sh
```

*Terminal 3*
```
cd ~/racecar_ws/
rosrun realsense2_camera record_data.py
```

Data will only be collected when the dead man's switch is pressed and the right bumper is held down. The RGB images are saved to `~/images/`, depth data is saved to `~/d_images/`, and labels are saved to `~/racecar/labels.txt/`.

### Autonomous Mode with Neural Network

To make the car drive autonomously, controlled by the neural network, run the following:

*Terminal 1*
```
cd ~/racecar_ws/
. launch.sh
```

*Terminal 2*
```
cd ~/racecar_ws/
. camera.sh
```

*Terminal 3*
```
cd ~/racecar_ws/
rosrun realsense2_camera neural_network.py
```
