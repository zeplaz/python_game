#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
import math

"""
##########################
movments.py
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


def map_to_pi_range(a):
    while a > np.pi:
        a -=2* np.pi
    while a <  -np.pi:
        a += 2* np.pi
    return a

class Steering_out:
    def    __init__(self, lin, ang):
        self.linear  =lin
        self.angular =ang


class Placement:
    def __init__(self, in_o, in_p):
        self.orientation = in_o
        self.pos = in_p

def new_orientation(cur_pos ,vel):
    if vel.magnatude() > 0:
        return  math.atan(-cur_pos.X,cur_pos.y)
    else:
        return None


class Kinematic:
    def __init__(this, p, o, v, r):
        this.pos        = p
        this.orientation = o
        this.velocity   = v
        this.rotation   = r


    def update(self,steering_out,max_sp,dt):
        self.pos += self.velocity * dt
        self.orientation += self.rotation * dt

        self.velocity += steering_out.linear * dt
        self.rotation += steering_out.angular * dt

        if self.velocity.magnatued() > max_sp:
            self.velocity.normalize()
            self.velocity *= max_sp


class phy_Character(Kinematic):
    def __init__(slef,in_p,in_o ):
        super().__init__(in_p, in_o, 0 ,0)

class phy_Destination_Objective():
    def __init__(self):
        pass


class Orientation :
    def __init__(this, in_angle):
        this.angle = in_angle



'''
#########################################################
VECTORS!
#######################################################3
'''
class Vector2D():

    def __init__(self,x,y):
        self._xy = np.array([x,y])

    def __getitem__(self, index):
       # print ('\n REcT::__getitem__', type(items), items)
       return self._xy[index]

    def magnitude(self):
        return np.sqrt(self._xy.dot(self._xy))

    def normalize(self):
        mag = self.magnitude()
        self.X = self.X/mag
        self.Y = self.Y/mag

    def normalize_return(self):
        mag = self.magnitude()
        X = self.X / mag
        Y = self.Y / mag

        return Vector2D(X,Y)

    def absolute(self):
        return np.absolute(self._xy)

    def __mul__(self, other):
        return np.multiply(self._xy,other._xy)

    def __sub__(self, other):
        return np.subtract(self._xy,other._xy)

    def __add__(self, other):
        return np.add(self._xy,other._xy)

    def __truediv__(self,other):
       return np.true_divide(self, other)

    def __floordiv__(self, other):
        return np.floor_divide(self,other)

    def __LT__(self, other):
         return np.sqrt(self._xy.dot(self._xy)) <  np.sqrt(other._xy.dot(other._xy))

    def __GT__(self,other):
        return np.sqrt(self._xy.dot(self._xy)) >  np.sqrt(other._xy.dot(other._xy))

    def __IMUL__(self,other):
        self._zy = self._xy * other._xy

    @property
    def xy(self):
        #print("\n\n*** in RECT @property:: val type", type(self._vertz))
        return self._xy

    @xy.setter
    def xy(self, value):
        #print("\n\n*** in RECT SETTER:: val type", type(value))
        self._xy = value

    @property
    def X(self):
        return self._xy[0]

    @X.setter
    def X(self, x):
        self._xy[0] = x

    @property
    def Y(self):
        return self._xy[1]

    @Y.setter
    def Y(self,y):
        self._xy[1] = y






class Rect():
    def __init__(self,x,y,w,h):
        self._vertz = np.array([x,y,w,h])
      #  print("\n\n*** in RECT __init__:: self.vertz", type(self._vertz))
       # print("value in x: ", self._vertz[0])

    def __getitem__(self, index):
       # print ('\n REcT::__getitem__', type(items), items)
       return self._vertz[index]
    @property
    def vertz(self):
        #print("\n\n*** in RECT @property:: val type", type(self._vertz))
        return self._vertz

    @vertz.setter
    def vertz(self, value):
        #print("\n\n*** in RECT SETTER:: val type", type(value))
        self._vertz = value




##_____________
##___________________ALIGN_



class Align:

    def __call__(self,char_k, D_o ):
        self.character = char_k
        self.destination_obktive = D_o
        return self.get_steering()

    def __init__(self,**alin_params ):

        self.max_angular_acceleration = alin_params['max_ang_accel']
        self.max_rotation      =        alin_params['max_rot']
        self.radius_dest_arrive=        alin_params['radius_dest_arrive']
        self.slow_radius       =        alin_params['slow_radius']
        self.time_to_dest  =           0.1

    def get_steering(self):
        rotation = self.destination_obktive.orientation - self.character.orientation
        rotation = map_to_pi_range(rotation)

        rotation_size =  np.absolute(rotation)


class Look_where_your_going(Align):
    def __init__(this):
        super().__init__()

class Face(Align):
    def __init(this):
        super().__init__()

##________###30##_ALIGN__FIN_____

####___________Seek_Flee_______

class Seek_Flee:
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
    def __init__(this):
        super().__init__()

class Pursue_Evade(Seek_Flee):
    def __init__(this):
        super().__init__()
class Path_following(Seek_Flee):
    def __init__(this):
        super().__init__()
###CLASS COLLISION AVOIDANCE IS IN THIS CHAIN BUT LOCAKED IN OWN MODUAL--collision.pu


###___Seek_Flee__FIN_____

###___VELOCITY_MATCH_____

class Velocity_match:
    def __init__(this):
        pass

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
