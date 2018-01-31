#!/usr/bin/env python



PACKAGE = 'amr_localization'

NODE = 'particle_filter'



import roslib

roslib.load_manifest(PACKAGE)

import rospy

import math

import random

import numpy as np

from amr_localization.motion_model import MotionModel

from amr_localization.pose import Pose

from amr_localization.particle import Particle

from amr_localization.random_particle_generator import RandomParticleGenerator



class ParticleFilter:



    def __init__(self, map_min_x, map_max_x, map_min_y, map_max_y, weigh_particles_callback):

        self.weigh_particles_callback = weigh_particles_callback

        self.particle_set_size = 100

        self.random_particles_size = 10

        self.motion_model = MotionModel(0.02, 0.01)

        self.random_particle_generator = RandomParticleGenerator(map_min_x, map_max_x, map_min_y, map_max_y)



        self.particles = []

        for i in range(self.particle_set_size):

            self.particles.append(self.random_particle_generator.generate_particle())



        self.pose_estimate = Pose()



    def update(self, x, y, yaw):

        #set parameters for motion

        self.particle_updates = []

        self.motion_model.setMotion(x,y,yaw)



        #calculate weights after motion

        for i in range(self.particle_set_size):

            # for i in range(self.random_particles_size):

            # new_particle = Particle()

            self.particles[i].pose = self.motion_model.sample(self.particles[i].pose)





        # self.particle_updates.sort(reverse=True,key=lambda particle_updates: particle_updates.weight)

        weights = self.weigh_particles_callback(self.particles)

        weight_sum = 0.0

        for i in range(self.particle_set_size):

            self.particles[i].weight = weights[i]

            weight_sum += self.particles[i].weight



        weight_pmf = []

        if(weight_sum<1e-5):

            weight_sum=0.001

        self.particles.sort(reverse=True,key=lambda particles: particles.weight)

        for i in range(self.particle_set_size):

            self.particles[i].weight = weights[i]/weight_sum



            weight_pmf.append(self.particles[i].weight)



        resampling_size = self.particle_set_size - self.random_particles_size

        self.particles = self.resampling(self.particles,resampling_size,weights)



        for i in range(self.random_particles_size):

            self.particles.append(self.random_particle_generator.generate_particle())



    def resampling(self, particle_set, resampling_size,weight_pmf):

        cdf = np.cumsum(weight_pmf)

        samples=[]

        for i in range(resampling_size):

            r = np.random.rand()

            # idx = np.where(cdf > r)[0][0]

            a=np.random.randint(0,len(particle_set)-1)

            samples.append(self.particles[a])



        return samples













        '''

        ============================== YOUR CODE HERE ==============================

         Instructions: do one complete update of the particle filter. It should

                       generate new particle set based on the given motion

                       parameters and the old particle set, compute the weights of

                       the particles, resample the set, and update the private

                       member field that holds the current best pose estimate

                       (self.pose_estimate). Note that the motion parameters provided

                       to this function are in robot's reference frame.



         Hint: Check motion_model.py for documentation and example how to use it

               for the particle pose update.

               x, y, yaw -- are the odometry update of the robot's pose (increments)





         Remark: to compute the weight of particles, use the weigh_particles_callback member

                 field:



                     weights = self.weigh_particles_callback(particles_list)



         Remark: to generate a comletely random particle use the provided

                 random_particle_generator object:



                     particle = self.random_particle_generator.generate_particle()



         Finally  the best pose estimate and assign it to the corresponding member field

         for visualization:

                     self.pose_estimate = selected_particle.pose

        ============================================================================

        '''







    def get_particles(self):

        return self.particles



    def get_pose_estimate(self):

        return self.pose_estimate



    def set_external_pose_estimate(self, pose):

        self.random_particle_generator.set_bias(pose, 0.5, 500)
