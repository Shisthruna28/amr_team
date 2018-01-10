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

echo_and_run cd "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_braitenberg"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/opt/ros/indigo/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/opt/ros/indigo/lib/python2.7/dist-packages:/home/supriya/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/supriya" \
    "/usr/bin/python" \
    "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_braitenberg/setup.py" \
    build --build-base "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_braitenberg" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/opt/ros/indigo" --install-scripts="/opt/ros/indigo/bin"
