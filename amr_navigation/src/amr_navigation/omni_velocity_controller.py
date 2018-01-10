#!/usr/bin/env python

PACKAGE = 'amr_navigation'
import rospy
from math import *
from velocity_controller import VelocityController, Velocity
from velocity_controller import get_shortest_angle, get_distance
from math import atan2, copysign

class OmniVelocityController(VelocityController):

    def __init__(self, l_max_vel, l_tolerance, a_max_vel, a_tolerance):
        self._l_max_vel = l_max_vel
        self._l_tolerance = l_tolerance
        self._a_max_vel = a_max_vel
        self._a_tolerance = a_tolerance

    def compute_velocity(self, actual_pose):
        dx = self._target_pose.x - actual_pose.x
        dy = self._target_pose.y - actual_pose.y

        linear_dist = get_distance(self._target_pose, actual_pose)
        angular_dist = get_shortest_angle(self._target_pose.theta, actual_pose.theta)
        change_taken_unit= (angular_dist)/linear_dist

        if (abs(linear_dist)<self._l_tolerance and abs(angular_dist)<self._a_tolerance):
            self._linear_complete = True
            self._angular_complete = True
            return Velocity()

        if (abs(linear_dist)>self._l_tolerance and abs(angular_dist)>self._a_tolerance):

            angular_dist = get_shortest_angle(atan2(dy, dx), actual_pose.theta)

            vel_x = cos(angular_dist)*self._l_max_vel
            vel_y = sin(angular_dist)*self._l_max_vel
            vel_z = self._a_max_vel*change_taken_unit

            return Velocity(vel_x, vel_y, vel_z)

        else:
            self._linear_complete = True
            self._angular_complete = True
            return Velocity()

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
