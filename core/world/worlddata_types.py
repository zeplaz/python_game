#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:11:45 2021
_
@-created by :_zeplaz's


##########################
worlddata_types

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN



_________________________________//
##################################
"""
import numpy as np
from typing import List, NamedTuple, Tuple, Union, Sequence
import sdl2.ext
#Vector = Union[Tuple[float,float], List[float],np.array([float,float])]

#Vector_list = Sequence[Vector]


sheet_data_map = []

RGBA8888 = 'RGBA8888'

class Rect():
    def __init__(self,x,y,w,h):
        self.vertz = np.array([x,y,w,h])

        @property
        def vertz(self):
            return self._vertz

        @vertz.setter
        def vertz(self, value):
            self._vertz = value

class sprit_meta:
    def __init__(this,path_image,s_size,scale_k,formate):
        this.path_image = path_image
        this.sheet_size = s_size
        this.scale_k = scale_k
        this.formate = formate

class sprit_sheet_data :
    def __init__(this, name,fc,fd,sprit_size):
        this.name = name
        this.frame_count = fc
        this.sprit_size = sprit_size
        this.frame_dimetions = fd

class sprit_sheet:
    def __init__(this,spr_mt, sp_data):
        this._sheet_data = sp_data
        this._sheet_meta = spr_mt




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
