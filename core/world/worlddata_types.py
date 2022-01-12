#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
worlddata_types.py
##########################

##########################
|*  ->
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN

_________________________________//
##################################
"""

import numpy as np
import ctypes
#from typing import List, NamedTuple, Tuple, Union, Sequence
import sdl2
#Vector = Union[Tuple[float,float], List[float],np.array([float,float])]

#Vector_list = Sequence[Vector]


sheet_data_map = []

RGBA8888 = 'RGBA8888'

class Vector():

    def __init__(self,x,y):
        self._xy = np.array([x,y])

    def __getitem__(self, index):
       # print ('\n REcT::__getitem__', type(items), items)
       return self._xy[index]
    def magnitude():
        return np.sqrt(self._xy.dot(self._xy))

    def __mul__(self, other):
        #self._xy[0]*= other._xy[0]
    #    self.Y     *= other.Y
        return np.multiply(self._xy,other._xy)

    def __sub__(self, other):
        return np.subtract(self_xy,other._xy)

    def __add__(self, other):
        return np.add(self_xy,other._xy)

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

class sprit_meta:
    def __init__(this,path_image,s_size,scale_k,formate):
        this.path_image = path_image
        this.sheet_size = s_size
        this.scale_k = scale_k
        this.formate = formate

class sprit_frame_data :
    def __init__(this, name,fd,sprit_size):
        this.name = name
        this.sprit_size = sprit_size
        this.frame_dimetions = fd

class sprit_sheet:
    def __init__(this,fc,sp_data_list,spr_mt):
        this.frame_count = fc
        this._sheet_frame_list = sp_data_list
        this._sheet_meta = spr_mt


class sprit_sheet_comp:
    def __init__(self, fs):
        self.frame_size = fs
        self._current_frame(0,0, fs.X,fs.Y)


class create_compent():
    def __init__(self, name, *params):

        if name == 'sprit_sheet':
            for pr in params:
                self.frame_size = pr
                self._current_frame(0,0, pr.X,pr.Y)


        return self


class Layer:
    def __init__(self, rt, a):
       self.texture = rt
       self.alpha = a

class Background_texture:
    def __init__(self, *params):
        self.layers = []
        for pr in params:
            self.layers.append(pr)

class Renderable_texture:
    def __init__(self, texture, pos, r_type, *params):
        self.texture = texture
        self._pos = pos
        self.r_type = r_type
        self.texture_dimestion = self.sdl_querry_texture_dimesions(texture)
        self.componets = {}

        if r_type == 'sprit_sheet':
            for fs in params:
                self.frame_size = fs
                self._current_frame(0,0, fs.X,fs.Y)
            """
            for key, comp in comps.items():
                self.componets[key] =  create_compent(key,comp)
                """
        if r_type == 'base_texture':
            self.frame_size = self.texture_dimestion
            self._current_frame(0,0, self.frame_size.X,self.frame_size.Y)

        if r_type == 'background_texture':
           self.frame_size = self.texture_dimestion
           self._current_frame(0,0, self.frame_size.X,self.frame_size.Y)
           self.layers = []
           for pr in params:
               self.layers.append(pr)

    def sdl_querry_texture_dimesions(self, texture):
        w =  ctypes.c_int()
        h =  ctypes.c_int()
        sdl2.SDL_QueryTexture(texture,None,None,w,h)
        return sdl2.Rect(0,0,w,h)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, x,y):
        self._pos = Vector(x,y)

    @property
    def current_frame(self):
        return self._current_frame

    @current_frame.setter
    def current_frame(self,x,y,w,h):
        self._current_frame = sdl2.SDL_Rect(x,y,w,h)

    def set_current_frame(self,cf):
        self.current_frame = cf

"""
class Renderable_sheet_sprit(Renderable_texture):
        def __init__(self,tex,pos, fs):
            super().__init__(self,tex,pos,'sprit_sheet')

"""

class Frame_dimetions:
    def __init__(this,x,y,w,h):
        this.pos = np.array([x,y])
        this.size = np.array([w,h])

"""
    def __init__(this, name, frame, rotated, trimmed, sprit_source_size, source_size, duration):
        this.name = name
        this.frame = frame
        this.rotation = rotation
        this.trimmed = trimmed
        this. sprit_source_size = sprit_source_size
        this.source_size = source_size
        this.duration = duration
"""
