#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:36:20 2021
_
@-created by :_zeplaz's


##########################
rez.py

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

##################################
"""


import core.parser as pars
import core.world.worlddata_types as wd_t
import os

class Rez:
    def __init__(this, rpath, rend ):
        this.spsheet_parser   = pars.sprit_sheet_parser()
        this.game_data_parser = pars.game_data_parser()
        this.path_map = {}
        this.unit_map = {}
        this.path_map["root_path"]  = rpath
        this.path_map["world_path"] = os.path.join(rpath, "/core/world")
        this.path_map["unit_data"]  = os.path.join(rpath, "/core/world/unit_data")
        this.path_map["animationz"] = os.path.join(rpath, "/core/world/animationz")
        this.path_map["unit_data"]  = os.path.join(rpath, "/core/world/unit_data")

        this.texture_spirt_factory  = wd_t.sdl2.ext.SpriteFactory(wd_t.sdl2.ext.TEXTURE, renderer = rend)
   
        this.AnimaZ_RESOURCES_SDL = wd_t.sdl2.ext.Resources(__file__, rpath+"/world/animationz")

        @property
        def path_map(self):
            return self._path_map

        @path_map.setter
        def path_map(self,name,data):
            self._path_map[name] = data

        @path_map.getter
        def path_map(self,tofind):
            if tofind in self._path_map :
                return self._path_map[tofind]
            print("\n###ERROROR--> pathmap to find val not found. in class Rez  @path_map.getter")
            return None


    def add_path_with_name(this, p, pname):
        this.path_map[pname] = p

    def set_sprit_sheet_animations(this, name, spshet):

        this.unit_map[name] = spshet

# Create sprite factory to create surfaces with later
    # Determine path to image to use as texture
    def __test__(this):
        print("\n**********REZ_TEST*****((((((((((())))))))))))")
        
        this.spsheet_parser.__test__(this.path_map["root_path"])
        this.game_data_parser.__test__(this.path_map["root_path"])

#class rez_mgmt:
    #def genrate_units(this):

    #def genrate_sprit_sheet()
    #def create_texture_spirt(this,filename): ->
       #     image_path = this.AnimaZ_RESOURCES_SDL.get_path(str(filename))

#import renderer as rend
