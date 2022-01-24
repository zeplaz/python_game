#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
animator.py
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

import sdl2

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


"""
class animator_vistor:
    def  genrate_frames(total):
        frame_dict = []

        for i < total:
            frame_dict[i] = sdl2.SDL_Rect(x,y,w,h)
            i +=1

    def spirt_sheet_selector():
    #    total_frames
    #    displayable_list = []
"""
