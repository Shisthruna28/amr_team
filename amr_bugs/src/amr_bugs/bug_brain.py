#!/usr/bin/env python
from planar import Point, Vec2
from planar.c import Line
from math import *

#=============================== YOUR CODE HERE ===============================
# Instructions: complete the currently empty BugBrain class. A new instance of
#               this class will be created for each new move_to command. The
#               constructor receives the goal specification and the mode of
#               wallfollowing (left (0) or right (1)) that is currently in use.
#               All the remaining functions receive the current position and
#               orientation of the robot.
#
# Hint: you can create a class member variable at any place in your code (not
#       only in __init__) by assigning a value to it, e.g.:
#
#           self.some_member_variable = 2012
#
# Hint: you could use the 'planar' library to avoid implementing geometrical
#       functions that check the distance between a point and a line, or any
#       other helper functions that you need. To use its classes add the
#       following import statements on top of the file:
#
#            from planar import Point, Vec2
#            from planar.c import Line
#            from math import degrees
# #
#       As discussed in the lab class, you will need to install the library by
#       executing `sudo pip install planar` in the terminal.
#
# Hint: all the member variables whose names start with 'wp_' (which stands for
#       'waypoint') will be automagically visualized in RViz as points of
#       different colors. Similarly, all the member variables whose names
#       start with 'ln_' (which stands for 'line') will be visualized as lines
#       in RViz. The only restriction is that the objects stored in these
#       variables should indeed be points and lines.
#       The valid points are:
#
#           self.wp_one = (1, 2)
#           self.wp_two = [1, 2]
#           self.wp_three = Point(x, y) # if you are using 'planar'
#
#       The valid lines are (assuming that p1 and p2 are valid points):
#
#           self.ln_one = (p1, p2)
#           self.ln_two = [p1, p2]
#           self.ln_three = Line.from_points([p1, p2]) # if you are using 'planar'

class BugBrain:

    TOLERANCE = 0.3

    def __init__(self, goal_x, goal_y, side):
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.side = side
        self.hit_points_list = []
        self.Vec_hit = None
        self.angle_vec = None
        self.last_hit_dist = None
        self.current_to_leave_dist = None
        self.unreach_points = None
        self.list_leaving_points = []
        self.x1 = None
        self.y1 = None
        self.leave_wall_list = []
        self.wp_leave_wall_points = None
        self.wp_goal_point = Point(self.goal_x, self.goal_y)
        self.count = 0
        self.flag = False
    def follow_wall(self, x, y, theta):
        """
        This function is called when the state machine enters the wallfollower
        state. """
        self.x = x
        self.y = y
        self.theta = theta
        self.wp_hit_point = Point(self.x, self.y) #creating a list for all the points it hits
        self.hit_points_list.append((x,y))
        self.ln_line_to_goal = Line.from_points([self.wp_hit_point, self.wp_goal_point]) # Draws a line from hit point to goal point
        self.Vec_hit = Point(x,y)
        self.angle_vec = self.wp_goal_point-self.Vec_hit
        print self.angle_vec
        self.last_hit_dist = self.Vec_hit.distance_to(self.wp_goal_point)
        self.count = self.count + 1

    def leave_wall(self, x, y, theta):
        """
        This function is called when the state machine leaves the wallfollower
        state.
        """
        self.flag  = True
        self.wp_leave_wall_points = Point(x,y)

    def is_goal_unreachable(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether the goal is unreachable.
        """
        # self.x_unreach = x
        # self.y_unreach = y
        # self.wp_current_pos = Point(x,y)
        # self.wp_hit_point.distance_to(self.wp_current_pos)
        # print self.wp_current_pos
        # if (self.flag == False):
        #     if(abs(self.wp_hit_point.distance_to(self.wp_current_pos))-abs(self.wp_goal_point.distance_to(self.wp_current_pos)) < 0.3):
        #         return True
        # return False

    def is_time_to_leave_wall(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether it is the right time (or place) to
        leave the wall and move straight to the goal.
        """
        self.x1 = x
        self.y1 = y
        self.theta = theta
        v1 = Vec2(x,y)
        goal_vec = self.wp_goal_point
        v3 = v1 - goal_vec
        #print v3
        angles_diff = v3.angle_to(self.angle_vec)
        #print angles_diff
        self.current_to_leave_dist = v1.distance_to(goal_vec)
        if (abs(self.x - self.x1)>0.5 or abs(self.y - self.y1)>0.5) and (abs(angles_diff)<2 or (abs(angles_diff)<182 and abs(angles_diff)>178 )):
            self.list_leaving_points.append((self.x1,self.y1))
            if self.current_to_leave_dist < self.last_hit_dist:
                return True
        return False

#==============================================================================
