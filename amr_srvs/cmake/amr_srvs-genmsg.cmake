# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "amr_srvs: 0 messages, 9 services")

set(MSG_I_FLAGS "-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Iamr_msgs:/home/supriya/catkin_ws/src/ws17-svadir2s/amr_msgs/msg;-Iamr_msgs:/home/supriya/devel/share/amr_msgs/msg;-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Inav_msgs:/opt/ros/indigo/share/nav_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/indigo/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(amr_srvs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv" "geometry_msgs/Point:geometry_msgs/Pose2D"
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv" "geometry_msgs/Point:geometry_msgs/PoseStamped:geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv" ""
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv" "amr_msgs/Cone:geometry_msgs/Point:geometry_msgs/Pose2D"
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv" ""
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv" "geometry_msgs/Point:geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Pose2D:geometry_msgs/PoseStamped:nav_msgs/Path:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv" ""
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv" "geometry_msgs/Point:geometry_msgs/PoseStamped:geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv" NAME_WE)
add_custom_target(_amr_srvs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "amr_srvs" "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv"
  "${MSG_I_FLAGS}"
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_msgs/msg/Cone.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/nav_msgs/cmake/../msg/Path.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)
_generate_srv_cpp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
)

### Generating Module File
_generate_module_cpp(amr_srvs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(amr_srvs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(amr_srvs_generate_messages amr_srvs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_cpp _amr_srvs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(amr_srvs_gencpp)
add_dependencies(amr_srvs_gencpp amr_srvs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS amr_srvs_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv"
  "${MSG_I_FLAGS}"
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_msgs/msg/Cone.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/nav_msgs/cmake/../msg/Path.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)
_generate_srv_lisp(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
)

### Generating Module File
_generate_module_lisp(amr_srvs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(amr_srvs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(amr_srvs_generate_messages amr_srvs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_lisp _amr_srvs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(amr_srvs_genlisp)
add_dependencies(amr_srvs_genlisp amr_srvs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS amr_srvs_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv"
  "${MSG_I_FLAGS}"
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_msgs/msg/Cone.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose2D.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/nav_msgs/cmake/../msg/Path.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)
_generate_srv_py(amr_srvs
  "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
)

### Generating Module File
_generate_module_py(amr_srvs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(amr_srvs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(amr_srvs_generate_messages amr_srvs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointOnBeam.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetPoseLikelihood.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsPointFree.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetNearestOccupiedPointInCone.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/IsLineSegmentFree.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/PlanPath.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetRangers.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/GetMultiplePoseLikelihood.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/supriya/catkin_ws/src/ws17-svadir2s/amr_srvs/srv/SwitchRanger.srv" NAME_WE)
add_dependencies(amr_srvs_generate_messages_py _amr_srvs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(amr_srvs_genpy)
add_dependencies(amr_srvs_genpy amr_srvs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS amr_srvs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/amr_srvs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(amr_srvs_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(amr_srvs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET amr_msgs_generate_messages_cpp)
  add_dependencies(amr_srvs_generate_messages_cpp amr_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/amr_srvs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(amr_srvs_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(amr_srvs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET amr_msgs_generate_messages_lisp)
  add_dependencies(amr_srvs_generate_messages_lisp amr_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/amr_srvs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(amr_srvs_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(amr_srvs_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET amr_msgs_generate_messages_py)
  add_dependencies(amr_srvs_generate_messages_py amr_msgs_generate_messages_py)
endif()
