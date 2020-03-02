#!/bin/bash

# vscode
cd
git clone https://github.com/JetsonHacksNano/installVSCode.git
cd installVSCode
./installVSCode.sh

# install ROS manually, because Jim's stuff is outdated
cd
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
sudo rosdep init
rosdep update

# setup ROS environment
grep -q -F 'source /opt/ros/melodic/setup.bash' ~/.bashrc || echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosinstall -y
grep -q -F ' ROS_MASTER_URI' ~/.bashrc ||  echo 'export ROS_MASTER_URI=http://localhost:11311' | tee -a ~/.bashrc
grep -q -F ' ROS_IP' ~/.bashrc ||  echo "export ROS_IP=$(hostname -I)" | tee -a ~/.bashrc
source ~/.bashrc

# clone Jim's stuff
cd
git clone https://github.com/RacecarJ/installRACECARJ.git
cd installRACECARJ/scripts

# fix outdated packages
sed -i 's/kinetic/melodic/g' setupCatkinWorkspace
sed -i 's/kinetic/melodic/g' installMITRACECARVESC6

# install Jim's stuff
./installRACECARUdev.sh
./setupCatkinWorkspace.sh racecar-ws
./installMITRACECARVESC6.sh

# remove unused camera library, setup peripherals
cd ~/racecar-ws/
rm -rf ./src/zed-ros-wrapper
sed -i 's/axis: 2/axis: 3/g' ./src/racecar/racecar/config/racecar-v2/joy_teleop.yaml
catkin-make
source devel/setup.bash
sudo chmod 777 /dev/ttyACM* /dev/input/js*
