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



#from typing import List, NamedTuple, Tuple, Union, Sequence
import sdl2
#Vector = Union[Tuple[float,float], List[float],np.array([float,float])]

#Vector_list = Sequence[Vector]

class Zone:
    def __init__(self, **params):

        self.rect = params['rect_size']
        self.backgroundtex_name = params['background_tex_name']

        # self.paramz = params

class World:
    def __init__(self):
        self.entity_list = []
        self.zone_map    = {}


    def add_entity(self, enity):
        self.enity_list =  enity

    def add_zone(this, name, **params):
        this.zone_map[name] = Zone(params)

    def add_zones(self, *args):
        for zone in args:
            self.add_zone(zone.name, zone.params)


    def cleanup(self):
        print("cleaningupworld")
        self.enity_list.clear()
        self.zone_map.zone_map()




sheet_data_map = []

RGBA8888 = 'RGBA8888'

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


