#!/usr/bin/env python

PACKAGE = 'amr_navigation'
NODE = 'path_executor'

import roslib
roslib.load_manifest(PACKAGE)
import rospy

from actionlib import SimpleActionClient, SimpleActionServer
from nav_msgs.msg import Path
from amr_msgs.msg import MoveToAction, MoveToGoal, ExecutePathAction, \
                         ExecutePathFeedback, ExecutePathResult


class PathExecutor:

    def __init__(self,name):
        self._action_name = name
      	self._as = SimpleActionServer(self._action_name, ExecutePathAction, execute_cb=self.execute_cb, auto_start = False)
      	self._as.start()
    	rospy.loginfo("in action_server")

    def execute_cb(self, goal):
        pass

    def move_to_done_cb(self, state, result):
        pass


if __name__ == '__main__':
    rospy.init_node(NODE)
    pe = PathExecutor(rospy.get_name())
    rospy.spin()
