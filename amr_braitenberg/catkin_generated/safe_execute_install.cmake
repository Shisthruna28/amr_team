execute_process(COMMAND "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_braitenberg/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/supriya/catkin_ws/src/ws17-svadir2s/amr_braitenberg/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
