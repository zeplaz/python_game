#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
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
import math

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



