gnome-terminal -x ./launch.sh & \
gnome-terminal -x bash -c "./camera.sh; exec bash" & \
gnome-terminal -x bash -c "./data_collecter.sh; exec bash"