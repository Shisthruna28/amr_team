#!/usr/bin/env python

PACKAGE = 'amr_navigation'

import math
from velocity_controller import VelocityController, Velocity
from velocity_controller import get_shortest_angle, get_distance

class OmniVelocityController(VelocityController):

    def __init__(self, l_max_vel, l_tolerance, a_max_vel, a_tolerance):
        self._l_max_vel = l_max_vel
        self._l_tolerance = l_tolerance
        self._a_max_vel = a_max_vel
        self._a_tolerance = a_tolerance

    def compute_velocity(self, actual_pose):
        # Displacement and orientation to the target in world frame:
        dx = self._target_pose.x - actual_pose.x
        dy = self._target_pose.y - actual_pose.y
        # Step 1: compute remaining distances
        linear_dist = get_distance(self._target_pose, actual_pose)
        angular_dist = get_shortest_angle(self._target_pose.theta, actual_pose.theta)
        #ratio for calculating the angles to be moved for unit distance to be covered which will
        #later be used to control the angular velocity.
        a_l = angular_dist/linear_dist
        #print angular_dist

        if (abs(linear_dist)<self._l_tolerance and  abs(angular_dist)<self._a_tolerance):
            self._linear_complete = True
            self._angular_complete = True
            return Velocity()

        if (abs(linear_dist)>self._l_tolerance or self._target_pose.theta != actual_pose.theta) :

            angular_dist = get_shortest_angle(math.atan2(dy, dx), actual_pose.theta)


            x_v = (math.cos(angular_dist)*self._l_max_vel)/(abs(angular_dist)+1)
            y_v = (math.sin(angular_dist)*self._l_max_vel)/(abs(angular_dist)+1)
            z_v_1 = self._a_max_vel*a_l
            print a_l
            if z_v_1 > self._a_max_vel:
                return Velocity(x_v,y_v,self._a_max_vel)


            else:
                return Velocity(x_v,y_v,z_v_1)

        else :
            return Velocity(0,0,0)

    """
    ========================= YOUR CODE HERE =========================

    Instructions: put here all the functions that are necessary to
    implement the VelocityController interface. You may
    use the DiffVelocityController as an example.

    Implement the constructor to accept all the necessry parameters
    and implement compute_velocity() method

    You are free to write any helper functions or classes you might
    need.

    ==================================================================

    """
