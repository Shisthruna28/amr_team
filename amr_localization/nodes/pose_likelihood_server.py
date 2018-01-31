#!/usr/bin/env python

PACKAGE = 'amr_localization'
NODE = 'pose_likelihood_server'

import roslib
roslib.load_manifest(PACKAGE)
import rospy
import tf
import numpy as np
import math

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped, Pose2D
from amr_srvs.srv import GetMultiplePoseLikelihood, GetMultiplePoseLikelihoodResponse, GetNearestOccupiedPointOnBeam, GetNearestOccupiedPointOnBeamRequest, SwitchRanger


class PoseLikelihoodServerNode:
    """
    This is a port of the AMR Python PoseLikelihoodServerNode
    """

    def __init__(self):
        self.no_of_beams=12
        self.actual_readings = []
        self.angle_max = 0.0
        self.angle_min= 0.0
        self.angle_increment=0.0
        self.likelihood = []

        rospy.init_node(NODE)

        # Wait until SwitchRanger service (and hence stage node) becomes available.
        rospy.loginfo('Waiting for the /switch_ranger service to be advertised...');
        rospy.wait_for_service('/switch_ranger')
        try:
            switch_ranger = rospy.ServiceProxy('/switch_ranger', SwitchRanger)
            # Make sure that the hokuyo laser is available and enable them (aka switch on range scanner)
            switch_ranger('scan_front', True)
        except rospy.ServiceException, e:
            rospy.logerror("Service call failed: %s"%e)

        """
            Expose GetMultiplePoseLikelihood Service here,
            subscribe for /scan_front,
            create client for /occupancy_query_server/get_nearest_occupied_point_on_beam service

            http://wiki.ros.org/ROS/Tutorials/WritingServiceClient(python)
        """

        self._tf = tf.TransformListener()
        #create pose_likelihood server
        poselikelihood_server = rospy.Service('/pose_likelihood_server/get_pose_likelihood',GetMultiplePoseLikelihood,self.pose_callback)
        #subscribe to laser
        self.laser_sub = rospy.Subscriber('/scan_front',LaserScan,self.laser_callback,queue_size=50)


        rospy.wait_for_service('/occupancy_query_server/get_nearest_occupied_point_on_beam')
        try:
            self.occupancy_query_client = rospy.ServiceProxy('/occupancy_query_server/get_nearest_occupied_point_on_beam', GetNearestOccupiedPointOnBeam)
        except rospy.ServiceException, e:
            rospy.logerror("Occupied points server failed: %s"%e)

        rospy.loginfo('Started [pose_likelihood_server] node.')

    """Callback function: laser_callback
    Function to get the readings of the laser. The angle_upper, angle_lower and angle_step parameters are used to compute the orientation of each beam."""

    def laser_callback(self,data):
        self.no_of_beams = len(data.ranges)
        self.actual_readings = []

        for i in range(self.no_of_beams):
            self.actual_readings.append(data.ranges[i])

        self.angle_max = data.angle_max
        self.angle_min = data.angle_min
        self.range_max = data.range_max
        self.angle_increment = data.angle_increment


    def pose_callback(self, response):

        #poses from the cient
        poses_value = response.poses
        likelihood_values=[]

        for i in range(len(poses_value)):
            #creating the service request
            occupancy_query_request = GetNearestOccupiedPointOnBeamRequest()

            #parameters for probability calculation
            #increasing sigma value decreases the likelihood values and very few likely points are seen in RViz
            sigma_value = 0.4
            weight_of_beam = 0.0
            bad_match = 0
            total_weight = 1.0
            pose = self.transform_pose(poses_value[i])
            occupancy_query_request.beams = pose
            occupancy_query_request.threshold = 2
            #request to client to get distances
            occupancy_query_client_request= self.occupancy_query_client(occupancy_query_request)
            for j in range(len(self.actual_readings)):
                distance_simulated = occupancy_query_client_request.distances[j]
                #Thresholding
                if(distance_simulated < 0.0):
                    distance_simulated = 0.0
                elif(distance_simulated > self.range_max):
                    distance_simulated = self.range_max
                actual_distance = self.actual_readings[j]
                distance_diff = abs(actual_distance-distance_simulated)

                if(distance_diff <= 1.8*sigma_value):
                    # Calculate likelihood for the given distance values
                    weight_of_beam = (1.0 / (sigma_value*math.sqrt(2*math.pi))) * math.exp((-math.pow(distance_simulated - actual_distance, 2.0)) / (2 * math.pow(sigma_value, 2.0)))
                    total_weight *= weight_of_beam
                else :
                    bad_match = bad_match+1
            if bad_match < 4:
                total_weight = total_weight
            else :
                total_weight = 0.0
            likelihood_values.append(total_weight)
        likelihood_response = GetMultiplePoseLikelihoodResponse(likelihood_values)
        return likelihood_response



    def transform_pose(self, robot_pose):
        #Transform lasers to robot frame
        try:
            time = self._tf.getLatestCommonTime("/base_link","/base_laser_front_link")
            position, quaternion = self._tf.lookupTransform("/base_link","/base_laser_front_link",time)
            yaw = tf.transformations.euler_from_quaternion(quaternion)[2]
            x, y, yaw = position[0], position[1], yaw
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rospy.logerror("Error tf")
        beam_pose_array=[]
        # Individual Laser beams transformed to robot's frame
        for s in range(self.no_of_beams):
            individual_beam_pose = Pose2D()
            individual_beam_pose.x = robot_pose.pose.position.x + x
            individual_beam_pose.y = robot_pose.pose.position.y + y
            #shift between each laser beam
            individual_beam_orientations = self.angle_min + (s*self.angle_increment)
            #Laser Frames relative to robot's frame
            robot_pose_orientations = (robot_pose.pose.orientation.x,robot_pose.pose.orientation.y,robot_pose.pose.orientation.z,robot_pose.pose.orientation.w)
            #convert to euler
            euler = tf.transformations.euler_from_quaternion(robot_pose_orientations)
            #adding the angle contributed by laser_frame,robot_frame and shift in each laser frame
            individual_beam_pose.theta =  yaw + euler[2] + individual_beam_orientations
            #appending each individual beam pose
            beam_pose_array.append(individual_beam_pose)
        return beam_pose_array
"""
============================== YOUR CODE HERE ==============================
Instructions:   implemenent the pose likelihood server node including a
                constructor which should create all needed servers, clients,
                and subscribers, and appropriate callback functions.
                GetNearestOccupiedPointOnBeam service allows to query
                multiple beams in one service request. Use this feature to
                simulate all the laser beams with one service call, otherwise
                the time spent on communication with the server will be too
                long.

Hint: refer to the sources of the previous assignments or to the ROS
      tutorials to see examples of how to create servers, clients, and
      subscribers.

Hint: in the laser callback it is enough to just store the incoming laser
      readings in a class member variable so that they could be accessed
      later while processing a service request.

Hint: the GetNearestOccupiedPointOnBeam service may return arbitrary large
      distance, do not forget to clamp it to [0..max_range] interval.


Look at the tf library capabilities, you might need it to find transform
from the /base_link to /base_laser_front_link.
Here's an example how to use the transform lookup:

    time = self._tf.getLatestCommonTime(frame_id, other_frame_id)
    position, quaternion = self._tf.lookupTransform(frame_id,
                                                    other_frame_id,
                                                    time)
    yaw = tf.transformations.euler_from_quaternion(quaternion)[2]
    x, y, yaw = position[0], position[1], yaw

You might need other functions for transforming routine, you can find
a brief api description
http://mirror.umd.edu/roswiki/doc/diamondback/api/tf/html/python/tf_python.html
"""



if __name__ == '__main__':
    w = PoseLikelihoodServerNode()
    rospy.spin()
