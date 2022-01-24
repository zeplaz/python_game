#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
steering_behavours.py
##########################

##########################
|*  ->
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN
ian ai for games, book was used in creating this

_________________________________//
##################################
"""
import numpy as np
import core.physics.maths as l_maths

import core.physics.movments as mov
##_____________

"""
###############################################
DICTIONARY_MAP PREFABS:
###############################################
"""

alin_params["max_ang_accel":0,"max_rot":0,"radius_dest_arrive":0, "slow_radius":0 ]
BWeights = {"threat_index": 0.0,"distance": 0.0,"panic_index": 0.0}

"""
###############################################
"""

class behavour_weights:
    def __init__():
        global BWeights
        self._weights = BWeights

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, indexname, val):
        self._weights[indexname] = val

    def set_threat_index(self, ti):
        self._weights['threat_index'] = ti

    def set_distance_index(self, di):
        self._weights['distance'] = d

    def set_panic_index(self, p_i):
        weights['panic_index'] = p_i


class genrate_steering_prority():

    def dist_panic_cal(pan_i, d):

        if pan_i > d:
            return 0.8

        if pan_i < d:
            return 0.3


class streering_heap:
    def __init__(self):
        self.steering_que = []
        heapq.heapify(steering_que)

    def push(self, in_steering):
        heapq.heappush(self.steering_que, in_steering)

    def pop(self):
        return heapq.pop(self.steering_que)

    def pop_and_return(self):
        temp = heappq.pop(self.steering_que)

class Steering_behavour:

     def __lt__(self, nxt):
        return self._priority < nxt._priority

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, val):
        self._priority = val
         
#class wait:

class contune(Steering_behavour):
#    def __init__(self):
    def __call__(self, char_k):
            self.character = char_k
            #mov.Steering_out(0,0)
            return self.get_steering()

    def get_steering(self):
        self.character.velocity
        self.character.rotation

class Velocity_match(Steering_behavour):
    def __init__(self, max_accel):
        self.max_acceleration = max_accel

    def __call__(self, char_k, destination_obktive,ttd):
        self.character = char_k
        self.dest_o = destination_obktive
        self.ttd = ttd
        return self.get_steering()

    def get_sreering(self):
        linear = self.dest_o.velocity - self.character.velocity
        linear /= self.ttd

        if linear.magnatued() > self.max_acceleration:
           linear.normalize()
           linear *= self.max_acceleration

        return mov.Steering_out(linear,0)
##___________________ALIGN_



class Align(Steering_behavour):

    def __call__(self,char_k, D_o,  time_to_dest):
        self.character = char_k
        self.destination_obktive = D_o
        self.ttd = time_to_dest

        return self.get_steering()

    def __init__(self,**alin_params ):
        if alin_params == None
            global alin_params

        self.max_angular_acceleration = alin_params['max_ang_accel']
        self.max_rotation      =        alin_params['max_rot']
        self.radius_dest_arrive=        alin_params['radius_dest_arrive']
        self.slow_radius       =        alin_params['slow_radius']


    def get_steering(self):
        rotation = self.destination_obktive.orientation - self.character.orientation
        rotation = mov.map_to_pi_range(rotation)

        rotation_size =  np.absolute(rotation)

        if rotation_size < self.radius_dest_arrive:
            return None
        if rotation_size > self.slow_radius:
            dest_rotation = self.max_rotation
        else:
            dest_rotation = self.max_rotation*rotation_size/self.slow_radius

        dest_rotation *= rotation/rotation_size

        angular  = dest_rotation - self.character.rotation
        angular /= self.ttd

        angular_acceleration = abs(angular)

        if self.max_angular_acceleration < angular_acceleration:
            angular /= angular_acceleration
            angular*= self.max_angular_acceleration

        return Steering_out(0,angular)


class Look_where_your_going(Align):
    def __init__(this):
        super().__init__()

class Face(Align):
    def __init(this):
        super().__init__()

##________###30##_ALIGN__FIN_____

####___________Seek_Flee_______

class Seek_Flee(Steering_behavour):
    def __call__(self,char_Kin, Ds_O , accel_override)  -> Steering_out:
        self.character = char_Kin
        self.destination_obktive = Ds_O

        if accel_override is None:
            return self.get_steering()
        else :
            return self.get_steering(accel_override)

    def __init__(self, max_accel):
        self.max_acceleration = max_accel


    def get_steering(self, accel_override) -> Steering_out:
        out_linear  = self.destination_obktive.pos - self.character.pos
        out_linear.normalize()
        if accel_override is not None :
            out_linear*= accel_override

        out_linear *= self.max_acceleration
        out_angular = 0
        return Steering_out(out_linear, out_angular)




class Wander(Seek_Flee):
    def __init__(self,max_accel):
        super().__init__(max_accel)

class Pursue_Evade():
    def __init__(self):
        pass

class Path_following(Seek_Flee):
    def __init__(slef,max_accel):
        super().__init__(max_accel)
        pass
###CLASS COLLISION AVOIDANCE IS IN THIS CHAIN BUT LOCAKED IN OWN MODUAL--collision.pu


###___Seek_Flee__FIN_____

###___VELOCITY_MATCH_____


class Arrive(Velocity_match):
    def __init__(this):
        pass

##___VELOCITY_MATCH__FIN___

###___FORCE_FEILD_____
class Force_feild:
    def __init__(this):
        pass

class Seperation(Force_feild):
    def __init__(this):
        pass


##___FORCE_FEILD_____FIN___
