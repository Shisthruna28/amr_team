#!/usr/bin/env python


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
#
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
# import urllib3.contrib.pyopenssl
# urllib3.contrib.pyopenssl.inject_into_urllib3()

PACKAGE = 'amr_bugs'
from planar import Point, Vec2
from planar.c import Line
from math import degrees

class BugBrain:

    TOLERANCE = 0.3

    def __init__(self, goal_x, goal_y, side):
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.Vec_goal = Vec2(self.goal_x,self.goal_y)
        self.angle_check = None
        self.Vec_hit = None
        self.Vec_n = None
        self.xhit = None
        self.yhit = None
        self.hitlist = []
        self.leavelist = []
        self.last_hit_dist = None
        self.curr_leave_dist = None
        self.leave_wall_count = 0
        self.started_away = 0




#In follow wall the initial vector to the goal is drawn from the hitting position. and the hit points are added in the list
    def follow_wall(self, x, y, theta):
        """
        This function is called when the state machine enters the wallfollower
        state.
        """
        self.wp_hitwall = Vec2(x,y)#for visualizng in Rviz the hit point
        self.xhit = x
        self.yhit = y
        self.wp_start= Point(x, y)
        self.hitlist.append((x,y))
        self.wp_goal = Point(self.goal_x, self.goal_y)
        self.ln_goal = Line.from_points([self.wp_start, self.wp_goal])
        self.Vec_hit = Vec2(x,y)
        self.Vec_n = self.Vec_goal-self.Vec_hit
        self.last_hit_dist = self.Vec_hit.distance_to(self.wp_goal)



#In leave wall a flag is set when the bot leaves the wall and follow line. In unreachable goal this is not set to figure infinite loop
    def leave_wall(self, x, y, theta):
        """
        This function is called when the state machine leaves the wallfollower
        state.
        """
        self.leave_wall_count = 1
        # compute and store necessary variables

#Unreachable goal is decided if the bot didnt leave the wall and reaches the hit point again.
    def is_goal_unreachable(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether the goal is unreachable.
        """
        if (abs(self.xhit - x)>0.5 or abs(self.yhit - y)>0.5) :
            self.started_away = 1
        if (abs(x- self.hitlist[0][0])<0.2 and abs(y- self.hitlist[0][1])<0.2 and self.leave_wall_count==0 and self.started_away==1):
            return True


#If the angle between vector(current position to gaol position) and global vector(from hit point to goal point) is 0 or around 180 leave the walll.
    def is_time_to_leave_wall(self, x, y, theta):
        """
        This function is regularly called from the wallfollower state to check
        the brain's belief about whether it is the right time (or place) to
        leave the wall and move straight to the goal.
        """
        v = Vec2(x, y)
        v1 = Vec2(self.goal_x, self.goal_y)
        v3 = v1 - v
        angle_diff = v3.angle_to(self.Vec_n)

        self.curr_leave_dist = v.distance_to(v1)
        if (abs(self.xhit - x)>0.5 or abs(self.yhit - y)>0.5) and (abs(angle_diff)<2 or (abs(angle_diff)<182 and abs(angle_diff)>178 )):
            if self.curr_leave_dist < self.last_hit_dist:
                return True





#==============================================================================
