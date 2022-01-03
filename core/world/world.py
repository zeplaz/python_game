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


import core.world.worlddata_types as wd_t

import core.resources as rez
import core.world.anima as anima

import sdl2

#import core.world.anima as Anima
#import core.physics as phy


#rect = wd_types.rect

#class Background:

    #def __init__(this, name):



class Zone_params:
    def __init__(self, in_rectsize, background):
        self.rect  = in_rectsize
        self.background = background

    #def add_spawn_list():



class Zone:
    def __init__(self, zp):
       zone_params = zp
        #self.paramz = params


class World_mgmt:
    def load_a_world(this, toload):
        world =World()
        return world

class World:
    def add_zone(this,name,params):
        this.zone_map = {name,Zone(params)}

    def load(self):


class world_mgmt:
    def __init__(self,rpath,rend):
        self.world_map = {}
        self.world_resources = rez.Rez(rpath,rend)

    def create_world(self, name, *params):



        self.current_world[name]

    def load_world(self, name):
        if name in self.world_map:
            self.current_world = self.world_map[name]
            return
        print("\n### ERRORworld_mgmt::_world not found:", name)
        return

    def __test__(self, path,rend):

        test_world = World()

      #  sdl2.c
       # background_zp1_base =
        zp1 = Zone_params(wd_t.Rect(x, y, 800, 800), background)

        test_world.add_zone("testzone_A01", params)

        world_map['test_world01',test_world]

        current_world = test_world




    #def draw_lists(this):
     #   this.air_list.draw()

    #air_hit_list = .check_for_collision_with_list()


    #for airunit in air_hit_list:
     #   airunit.update_damage()
