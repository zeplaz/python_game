#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:11:45 2021
_
@-created by :_zeplaz's


##########################
world

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

_________________________________//
##################################
"""
SPRITE_SCALING_BASE = 0.25
SPRIT_SCALING_F16_BASE = 0.2
SPRIT_SCALING_SAM_BASE = 0.5
SPRIT_SCALING_RADAR_BASE = 0.5
SPRIT_SCALING_WARHOG = 0.3


import worlddata_types as wd_types
import core.world.anima as Anima
import core.physics as phy


#rect = wd_types.rect

class Background:

    def __init__(this, name):

class zone_params:
    def __init__(this, in_rectsize, background):
        this.rect  = in_rectsize
        this.background =background

    def add_spawn_list():



class Zone:
    def __init__(this, params):
        this.paramz = params


class World_mgmt:
    def load_a_world(this, toload):
        world =World()
        return world

class World:
    def add_zone(this,name,params):
        newzone Zone(params)
        this.zone_map = {name,newzone}


    def __test__(this):
        



    #def draw_lists(this):
     #   this.air_list.draw()

    #air_hit_list = .check_for_collision_with_list()


    #for airunit in air_hit_list:
     #   airunit.update_damage()
