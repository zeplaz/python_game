#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
world_mgmt.py
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

import core.ID_genrators as ID_gen
import core.world.worldz_data.world_config as w_config

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
        self.enity_list.append(enity)

    def add_zone(this, name, **params):
        this.zone_map[name] = Zone(params)

    def add_zones(self, *args):
        for zone in args:
            self.add_zone(zone.name, zone.params)

    def cleanup(self):
        print("cleaningupworld")
        self.enity_list.clear()
        self.zone_map.zone_map()

class world_mgmt:
    def __init__(self):
        self._flag_load_next_world = False
        self.current_world         = None
        self.next_world            = None
        self.world_map             = {}
        self.world_configurer      = w_config.world_config()

    def add_entity_to_world(self, enity):
            enity.worldID = ID_gen.World_ID()
            self.current_world.add_entity(enity)

    def update_enitys(self, dt):
        for ent in enity_list:
            ent.k_update(ent.steering_behavour(),ent.max_speed,dt)



    @property
    def next_world_flag(self):
        return self._flag_load_next_world

    @next_world_flag.setter
    def load_next_world(self):
        self._flag_load_next_world = True

    def create_world(self, name, *params):

        if name in self.world_map:
            return self.world_map[name]
        else :
            self.world_map[name] = self.world_configurer(params)

    def load_world(self, name):
        if name in self.world_map:
            self.next_world_flag == True
            self.next_world = self.world_map[name]

        else:
            self.next_world_flag = False
            print("\n### ->ERRORworld_mgmt::_world not found in world_map:", name)
            print("\n ##ERROR:: the world must exist to be loaded  first run create_world(name,*params),",
                  "\n fyi:you will remain in current world\n")

        return

    def update_spawners(self):
        for sp in self.spawners

    def add_anima_to_world(self, anima):
        pass

    def add_spawnlist_to_world(self,spawn_list):

            for anima_ in spawn_list:
                if anima_.alive is True:
                    self.add_anima_to_world(anima_)

    def add_new_spawner_to_world(self, *params):


    def update_realms(self):
        if self.next_world_flag == True:
            self.current_world.cleanup()
            self.current_world = self.next_world



        # self.current_world = self.next_world
        # get the new world to load
        # instanste the world. and return it.
        # name = self.load_world(next_world)
        # self.current_world = self.world_map[name]

    def __test__(self, path, rend, testname):

        #test_world = World(testname)
        print("testing,,moved ot congiurte.?")
        #  sdl2.c
        # background_zp1_base =
        #zp1 = Zone_params(wd_t.Rect(x, y, 800, 800), )

     #   test_world.add_zone("testzone_A01", params)

       # self.world_map['test_world01', test_world]

       # current_world = test_world

      #  self.world_resources = rez.Rez(path, rend)
    # def draw_lists(this):
    #   this.air_list.draw()

    # air_hit_list = .check_for_collision_with_list()

    # for airunit in air_hit_list:
    #   airunit.update_damage()


# rect = wd_types.rect

# class Background:

# def __init__(this, name):

    # def add_spawn_list():
