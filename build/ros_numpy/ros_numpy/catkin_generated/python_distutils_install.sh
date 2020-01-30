#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/model3/new/racecar_ws/src/ros_numpy/ros_numpy"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/model3/new/racecar_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/model3/new/racecar_ws/install/lib/python2.7/dist-packages:/home/model3/new/racecar_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/model3/new/racecar_ws/build" \
    "/usr/bin/python2" \
    "/home/model3/new/racecar_ws/src/ros_numpy/ros_numpy/setup.py" \
    build --build-base "/home/model3/new/racecar_ws/build/ros_numpy/ros_numpy" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/model3/new/racecar_ws/install" --install-scripts="/home/model3/new/racecar_ws/install/bin"
