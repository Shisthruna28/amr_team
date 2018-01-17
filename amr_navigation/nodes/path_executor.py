#!/usr/bin/env python

PACKAGE = 'amr_navigation'
NODE = 'path_executor'

import roslib
roslib.load_manifest(PACKAGE)
import rospy

from actionlib import SimpleActionClient, SimpleActionServer
from nav_msgs.msg import Path
from amr_msgs.msg import MoveToAction, MoveToGoal, ExecutePathAction, \
                         ExecutePathFeedback, ExecutePathResult, ExecutePathGoal


class PathExecutor:
    _feedback = ExecutePathFeedback()
    _result = ExecutePathResult()
    def __init__(self, name):
        rospy.loginfo("Creating an action server")
        # Client for move_to server
        self._move_to_client = SimpleActionClient('/bug2/move_to', MoveToAction)
        # Action server for Executepathaction
        self._action_name = "_as"
        self._as = SimpleActionServer('/path_executor/execute_path', ExecutePathAction, \
                                        execute_cb=self.execute_cb, auto_start=False)
        self._as.start()
        # variable for preemption
        self.flag = True
        self.success = True

    def execute_cb(self, goal):
        print "------in execute callback----------"
        # Jumps into callback function on client request
        self._move_to_client.wait_for_server()
        rospy.loginfo(goal.path.poses)
        self.move = MoveToGoal()
        # Sending all the poses to move_to
    	for i in range(len(goal.path.poses)):
            if i == 2:
                self.success = True
            else:
                self.success = False
    	    self._pose = goal.path.poses[i]
            self.move.target_pose = self._pose
            self._move_to_client.send_goal(self.move, done_cb=self.move_to_done_cb)
            self._move_to_client.wait_for_result()
        rospy.spin()

        # setting preemption of server
    	while self.flag :
    		if self._as.is_preempt_requested():
    			rospy.loginfo('%s: Preempted' % self._action_name)
    			self._as.set_preempted()
    			break

    def move_to_done_cb(self, state, result):
        print "------in move_to_done callback----------"
    	if(state == 3):
            self._result.visited.append(True)
            self._feedback.reached = True
            self._feedback.pose = self._pose
        elif(state == 4):
    		self._feedback.reached = False
        rospy.loginfo(self._result)
    	self._as.publish_feedback(self._feedback)
    	if self.success == True:
            print "All goals are considered"
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node(NODE)
    pe = PathExecutor(rospy.get_name())
    rospy.spin()
