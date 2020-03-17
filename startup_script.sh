#!/bin/bash
# This file is run automatically on startup in cron.
tmux new-session -d -c ~/racecar_ws/ -s ros roslaunch racecar teleop.launch
sleep 1
tmux new-window ./camera.sh
tmux new-window ./data_collecter.sh
