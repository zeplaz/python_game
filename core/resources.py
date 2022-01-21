#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************

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

"""
class TextureRenderSystem(wd_t.sdl2.ext.TextureSpriteRenderSystem):
    def __init__(self, renderer):
        super(TextureRenderSystem, self).__init__(renderer)
        self.renderer = renderer

    def render(self, components):
     #   tmp = self.renderer.color
        #self.renderer.color = BLACK
        self.renderer.clear()
        #self.renderer.color = tmp
        super(TextureRenderSystem, self).render(components)
"""

class Rez:
    def __init__(this, rpath, rend ):
        this.spsheet_parser   = pars.sprit_sheet_parser()
        this.game_data_parser = pars.game_data_parser()
        this.path_map = {}
        this.unit_map = {}
        this.sprit_sheet_map = {}
        this.texture_map = {}


        this.path_map["root_path"]  = rpath
        this.path_map["world_path"] = os.path.join(rpath, "/world")
        this.path_map["unit_data"]  = os.path.join(rpath, "/world/unit_data")
        this.path_map["animationz"] = os.path.join(rpath, "/world/animationz")
        #this.path_map["unit_data"]  = os.path.join(rpath, "/core/world/unit_data")

        this.texture_spirt_factory  = TextureRenderSystem(rend)
        this.texture_spirt_factory = wd_t.sdl2.ext.SpriteFactory(wd_t.sdl2.ext.TEXTURE, renderer=rend.renderer_SDL)

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

    @property
    def sprit_sheet_map(self):
        return self._sprit_sheet_map

    @sprit_sheet_map.setter
    def sprit_sheet_map(self,name,data):
        self._path_map[name] = data

    @sprit_sheet_map.getter
    def sprit_sheet_map(self,tofind):
        if tofind in self._sprit_sheet_map :
            return self._sprit_sheet_map[tofind]
        print("\n###ERROROR--> pathmap to find val not found. in class Rez  @path_map.getter")
        return None

    def create_sprit_sheet_texture(self, name):
        if name in self.sprit_sheet_map:
            return self.texture_spirt_factory.from_image(self.path_map["root_path"]+self.sprit_sheet_map[name]._sheet_meta.path_image)

        return None

    def add_sprit_sheet_cache(self, name, dirc, fname):
        self.sprit_sheet_map[name] = self.spsheet_parser.load_spirtsheet_data(dirc, fname)

    def create_raw_texture(self,fname):
        return self.texture_spirt_factory.from_image(self.path_map["root_path"]+fname)

    def add_path_with_name(this, p, pname):
        this.path_map[pname] = p


    def set_sprit_sheet_animations(this, name, spshet):

        this.unit_map[name] = spshet


            
    def create_add_texture(self, filepath,name, ttype):
        self.texture_map[name] =(ttype, self.texture_spirt_factory.from_image(self.path_map["root_path"] + filepath))


    def __test__(this):
        print("\n**********REZ_TEST*****((((((((((())))))))))))")

        this.spsheet_parser.__test__(this.path_map["root_path"])
        this.game_data_parser.__test__(this.path_map["root_path"])

        this.add_sprit_sheet_cache("f16Engine_test",this.path_map["root_path"]+
                                   this.path_map["animationz"]+"/f16/f16_engine","f16_engine_on_00")
        new_texture = this.create__sprit_sheet_testure("f16Engine_test")
        print("the created sprittexuter..",type(new_texture))
    #    this.spsheet_parser.

#class rez_mgmt:
    #def genrate_units(this):

    #def genrate_sprit_sheet()
    #def create_texture_spirt(this,filename): ->
       #     image_path = this.AnimaZ_RESOURCES_SDL.get_path(str(filename))
#import renderer as rend
