#!/usr/bin/env python

PACKAGE = 'amr_mapping'

import sys
import math
import rospy
from exceptions import Exception
from amr_mapping.map_store_py import MapStore, MapStoreCone
from planar import Vec2

import random

class SonarMap:
    """
    Ported from C++ by Ivan Vishiakou
    Original description still applies:

    This class implements the sonar map algorithm as described in "Sonar-Based
    Real-World Mapping and Navigation" by Alberto Elfes, IEEE Journal Of
    Robotics And Automation, Vol. RA-3, No. 3, June 1987.

    Map coordinates vs. map cells

    The map works internaly on a discrete, integer-based grid, but exposes a
    more natural continuous coordinates interface. This allows an application
    to work with the map using its own units (in this documentation refered to
    as "meters"), without taking care of details of the map storage
    implementation.

    Each cell with integer coordinates (c_x, c_y) occupies the space from
    ((c_x - 0.5, c_y - 0.5) * resolution) exclusive to
    ((c_x - 0.5, c_y + 0.5) * resolution) inclusive.

    The value resolution is the length of a cells edge. All cells are considered
    to be squares.

    Note: if a variable name starts with the prefix "m_", then this variable
    contains a map coordinate. If the name starts with "c_" then this variable
    contains a cell coordinate. This convention applies both to the functions'
    arguments and internal/local variables.
    """


    def __init__(self, resolution, m_size_x, m_size_y):
        """
        This constructor creates a map of given dimensions.

        Args:
            resolution (float) : size of a cell, measured in meters, i.e. the length of
        the edge of a cell.
            m_size_x (float) : initial size of the map in x direction (meters).
            m_size_y (float) : initial size of the map in y direction (meters).
        """
        self._resolution = resolution
        self._c_size_x = int(round(m_size_x/resolution+2))|1
        self._c_size_y = int(round(m_size_y/resolution+2))|1
        self._m_size_x = resolution*self._c_size_x
        self._m_size_y = resolution*self._c_size_y
        self._m_min_x = -self._m_size_x/2.0
        self._m_min_y = -self._m_size_y/2.0

        self._map_combined = MapStore(self._c_size_x, self._c_size_y)
        self._map_free = MapStore(self._c_size_x, self._c_size_y)
        self._map_occupied = MapStore(self._c_size_x, self._c_size_y)
        self.r_min = 0.05
        self.probability_occ = []
        self.probability_empty =[]
        self.sum_occupied = None
        self.cone_valid = []



    def add_scan(self, m_sonar_x, m_sonar_y, sonar_theta, field_of_view,
                 max_range, registerd_range, uncertainty):
        """
        Update map using a sonar reading.

        Args:
            m_sonar_x (float) : x coordinate of the sonar in map coordinates.
            m_sonar_y (float) : y coordinate of the sonar in map coordinates.
            sonar_theta (float) : orientation of the sonar in map coordinates.
            fov (float) : opening angle of the sonar (radians).
            max_range (float) : maximum possible range of the sonar (meters).
            distance (float) : range reading returned from the sensor (meters).
            uncertainty (float) : the noise associated with the sensed distance,
        expressed as the standard deviation.
        """


        #============================== YOUR CODE HERE ==============================
        """
        Instructions: implement the routine that performs map update based on a
                      single sonar reading.

        Hint: use convertToCell( and convertToMap() functions to convert between
              map and cell coordinates.

        Hint: use MapStoreCone class to iterate over the cells covered
              by the sonar cone.

        Hint: you may use helper functions provided to you (euclidian_distance,
              angular_distance, clamp)

        Some snippets for your convenience.
        MapStoreCone creating:

        cone = MapStoreCone(c_sonar_pos_x, c_sonar_pos_y, sonar_theta,
                            field_of_view, c_cone_length)
            the last argument is cone length in cells (since all the linear sizes it operates
            are in terms of cells!)

        Iterating over cone cells:
        for cell in cone:
            #Do stuff
            # cell is a tuple (c_x, c_y)
            pass

        Reading/Setting cells of the map (MapStore):

        occ_val = self._map_occupied.get(*cell)         # cell = (c_x, c_y = )
        occ_val = self._map_occupied.get(c_x, c_y)      #

        self._map_occupied.set(c_x, c_y, new_occ_val)   # setting map cell value

        Hint: see the _convert_to_map(cell) function description. It can be used
              to check whether a cell is in bounds of the map. (You do not need to set/read
              cells that lie beyond the map grid)

              Alternatively you can use
              self._map_combined.is_in_x_range(c_x)     # returns boolean
              self._map_combined.is_in_y_range(c_y)     # returns boolean

        //============================================================================
        """

        cell_x,cell_y = self._convert_to_cell((m_sonar_x ,m_sonar_y))
        c_cone_length = int(max_range/self._resolution)

        max_x = m_sonar_x + registerd_range*math.cos(sonar_theta)
        max_y = m_sonar_y + registerd_range*math.sin(sonar_theta)

        cone = MapStoreCone(cell_x,cell_y, sonar_theta,
                             field_of_view, c_cone_length)
        self.probability_empty =[]
        self.probability_occ =[]
        self.cone_valid =[]
        for cell in cone :
            cell_position = cell
            if(self._map_combined.is_in_x_range(cell[0]) and self._map_combined.is_in_y_range(cell[1])):
                #converting to map space to calculate delta and theta values
                map_val_cell = self._convert_to_map(cell_position)

                delta_value = self.euclidian_distance(m_sonar_x,m_sonar_y,map_val_cell[0],map_val_cell[1])

                point_theta = math.atan2(( map_val_cell[1]-m_sonar_y ),(map_val_cell[0]-m_sonar_x))
                theta_value = self.angular_distance(point_theta,sonar_theta)

                #calculate probability for free sapce within the given delta range(distance uncertainty)
                point_erf = self._er_free(registerd_range,delta_value,uncertainty)
                #calculate the probability of the cell being the obstacle within the given sonar angle(angular uncertainty)
                point_ea = self._ea(field_of_view,theta_value)

                #  calculate probability for occupied sapce within the given delta range
                if registerd_range < max_range-0.05 : #handles open sonar readings
                    point_erocc = self._er_occ(registerd_range,delta_value,uncertainty)
                else:
                    point_erocc = 0.0

                if ((delta_value < registerd_range - uncertainty) and point_ea>0) :
                    #distance uncertainty
                    point_erf = self._er_free(registerd_range,delta_value,uncertainty)
                    #angular uncertainty
                    point_ea = self._ea(field_of_view,theta_value)

                    #Enhance empty values
                    prob_emp = point_ea * point_erf
                    emp_val = self._map_free.get(cell[0],cell[1])
                    emp_val_curr = prob_emp
                    new_emp_val = emp_val + emp_val_curr - emp_val*emp_val_curr

                    #checking and thresholding the probability range
                    if(new_emp_val)> 1.0:
                        new_emp_val = 1.0
                    elif new_emp_val < -1.0:
                        new_emp_val = -1.0
                    self._map_free.set(cell[0],cell[1],new_emp_val)
                else:
                    prob_emp = 0
                if(delta_value > (registerd_range - uncertainty) and (delta_value < registerd_range + uncertainty)):
                    prob_occ = (point_ea * point_erocc)*(1.0- prob_emp)
                else:
                    prob_occ = 0

                self.probability_empty.append(prob_emp)
                self.probability_occ.append(prob_occ)
                self.sum_occupied = sum(self.probability_occ)
                self.cone_valid.append(cell)



        for i,cell in (enumerate(self.cone_valid)):
            if(self._map_combined.is_in_x_range(cell[0]) and self._map_combined.is_in_x_range(cell[1])):

                occ_val = self._map_occupied.get(cell[0], cell[1])
                if self.sum_occupied < 1e-3:
                    new_occ_val = occ_val
                else:
                    #normalize with sum of occupied probabilities
                    occ_val_curr = self.probability_occ[i]/self.sum_occupied
                    new_occ_val = occ_val + occ_val_curr - occ_val*occ_val_curr
                    #checking and thresholding the probability range
                    if(new_occ_val)> 1.0:
                        new_occ_val = 1.0
                    elif new_occ_val < -1.0:
                        new_occ_val = -1.0

                #Enhance occupied values
                self._map_occupied.set(cell[0], cell[1], new_occ_val)

                com_val = self._map_combined.get(cell[0],cell[1])
                if (self._map_occupied.get(cell[0],cell[1])>self._map_free.get(cell[0],cell[1])):
                    self._map_combined.set(cell[0],cell[1], self._map_occupied.get(cell[0],cell[1]))
                else:
                    self._map_combined.set(cell[0],cell[1], -self._map_free.get(cell[0],cell[1]))







    def _er_free(self, sensed_distance, delta, uncertainty):
        """
        Calculate free-space probability.

        This function calculates the probability to be free for a point that is
        delta meters away from the sonar's origin when the sonar has measured a
        distance of sensed_distance with given uncertainty. This function only
        computes the radial component of the probability. To fully specify
        a point you need a distance and an angle and as such for the full
        probability you need the angular probability of the point to be the cause
        of the measured sensed_distance. This is calculated by _ea().
        The full probability is the product of the result from _ea() and from this
        function.

        Args:
            sensed_distance (float) : distance in meters measured by the sonar.
            delta (float) : distance from the sonar's origin for which the probability
        should be calculated.
            uncertainty (float) : uncertainty (variance) of measured distance.
        Returns:
            float : The probability to be free for a point delta meters away from
        the sonar's origin. The value is in the range 0.0 to 1.0.
        """

        #============================== YOUR CODE HERE ==============================
        #Instructions: compute the distance probability function for the "probably
        #              empty" region.
        e_f = 0.0
        if ((delta > sensed_distance - uncertainty) or (delta < self.r_min)):
            return 0.0
        else:
            e_f = 1.0 - pow(((delta - self.r_min)/(sensed_distance - uncertainty-self.r_min)),2)
            return e_f


    def _er_occ(self, sensed_distance, delta, uncertainty):
        """
        Calculate occupied-space probability.

        This function calculates the probability to be occupied for a point that
        is delta meters away from the sonar's origin when the sonar has
        measured a distance of sensed_distance with an uncertainty of
        uncertainty. This function only computes the radial component of
        the probability. To fully specify a point you need a distance and an angle
        and as such for the full probability you need the angular probability of
        the point to be the cause of the measured sensed_distance.
        This is calculated by _ea(). The full probability is the product of the
        result from _ea() and from this function.

        Args:
            sensed_distance (float) : distance in meters measured by the sonar.
            delta (float) : distance from the sonar's origin for which the probability
        should be calculated.
            uncertainty (float) : uncertainty (variance) of measured distance.

        Returns:
            float : The probability to be occupied for a point delta meters away
        from the sonar's origin. The value is in the range 0.0 to 1.0.
        """

        #============================== YOUR CODE HERE ==============================
        #Instructions: compute the distance probability function for the "probably
        #              occupied" region.
        o_r = 0.0
        if (delta > (sensed_distance + uncertainty) or (delta < sensed_distance - uncertainty)):
            return 0.0
        else:
            o_r = 1.0 - pow(((delta - sensed_distance)/uncertainty),2)
            return o_r




    def _ea(self, sonar_fov, theta):
        """
        Probability for a point in the sonar cone to be actually measured.

        This function calculates the probability of a point theta radians away
        from the center beam of a sonar cone of sonar_fov angular width, to be
        the cause of a sonar measurement.

        Args:
            sonar_fov (float) : the opening angle of the sonar cone in radians.
            theta (float) : the angular distance of a point from the center of the
        sonar cone, measured in radians. This value must lie within plus/minus
        sonar_fov / 2.

        Returns:
            float : Probability of a point in the sonar cone to be measured,
        value in range 0.0 to 1.0 as a funciton of angular distance to the
        central line of the sonar cone.
        """

        #============================== YOUR CODE HERE ==============================
        #Instructions: compute the angular probability function (it is same for both
        #              the "probably empty" and the "probably occupied" region.

        #Angular uncertainity
        e_a = 0.0
        if (theta > - sonar_fov/2 and theta < sonar_fov/2):
            e_a = 1.0 - pow(((2.0*theta)/(sonar_fov)),2)
            print '********' , e_a
            return e_a
        else:
            return 0.0


    def _convert_to_map(self, c_pos):
        """
        Converts cell coordinates to metric coordinates. Examples:
        m_pos = convert_to_map(c_pos)       #c_pos = (c_x, c_y)

        returns tuple (m_x, m_y) or None if cell coordinates out of bounds
        """
        c_x, c_y = c_pos
        if ( self._map_combined.is_in_x_range(c_x) and
             self._map_combined.is_in_y_range(c_y)      ):
            return (c_x*self._resolution, c_y*self._resolution)
        else:
            return None


    def _convert_to_cell(self, m_pos):
        """
        Converts metric coordinates cell coordinates. Examples:
        c_pos = convert_to_map(m_pos)       #m_pos = (m_x, m_y)

        returns tuple (c_x, c_y) or None if cell coordinates out of bounds
        """
        m_x, m_y = m_pos
        c_x, c_y = int(round(m_x / self._resolution)), int(round(m_y / self._resolution))
        if ( self._map_combined.is_in_x_range(c_x) and
             self._map_combined.is_in_y_range(c_y)      ):
            return (c_x, c_y)
        else:
            return None


    def get_grid_size_x(self):
        return self._c_size_x

    def get_grid_size_y(self):
        return self._c_size_y


    def get_min_x(self):
        return self._m_min_x

    def get_min_y(self):
        return self._m_min_y


    def get_resolution(self):
        return self._resolution

    def get_map_data(self):
        return self._map_combined.get_publish_data(-1.0, 1.0)

    def get_map_free_data(self):
        return self._map_free.get_publish_data(0.0, 1.0)

    def get_map_occupied_data(self):
        return self._map_occupied.get_publish_data(0.0, 1.0)


    @staticmethod
    def euclidian_distance(*args):
        """ Returns euclidian distance between two points:
        dist = euclidian_distance(pos1, pos2)
        dist = euclidian_distance(x1, y1, x2, y2)
        """
        try:
            if len(args) == 2:
                #tuples
                return math.sqrt((args[0][0]-args[1][0])**2+(args[0][1]-args[1][1])**2)
            elif len(args) == 4:
                #x's and y's:
                return math.sqrt((args[0]-args[2])**2+(args[1]-args[3])**2)
            else:
                raise Exception('Invalid arguments for euclidian_distance()')
        except Exception as e:
            print "Exception caught:", e.message


    @staticmethod
    def angular_distance(a1, a2):
        """Returns angular distance between two angles"""
        return math.atan2(math.sin(a1-a2), math.cos(a1-a2))


    @staticmethod
    def clamp(value, min_val, max_val):
        """Helper function to clamp a variable to a given range."""
        return max(min(value, max_val), min_val)
