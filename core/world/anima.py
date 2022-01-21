#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
anima.py
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

from enum import Enum

####import os
import sys


#import core.parser as pars

import core.world.worlddata_types as wd_t

import core.physics.movments as mov
#import core.render as rend



class Anima_Type(Enum):
    FLOCK_AIR_01     = 1
    FLOCK_AIR_02     = 2
    GROUND_SAM_91    = 91
    GROUND_RADAR_61  = 61
    F16_ENGINE_TEST  = 72
    TEST_MULTI_CRAFT = 83
    PLAYER_01        = 101
    VIEW_LENZ_01     = 203
    GENERATOR_       = 304
    SPAWNER_         = 405

nima_types = {
        'FLOCK_AIR_01'    :1,
        'FLOCK_AIR_02'    :2,
        'GROUND_SAM_91'   :91,
        'GROUND_RADAR_61' :61,
        'F16_ENGINE_TEST' :72,
        'TEST_MULTI_CRAFT':83,
        'PLAYER_01'       :101,
        'VIEW_LENZ_01'    :203,
        'GENERATOR_'      :304,
        'SPAWNER_'        :405
        }

class Hitbox_region:
    def __init__(self,x,y,w,h):
        self.rect = wd_t.Rect(x,y,w,h)
        self.info = 'add_info:or params to hitregions'

class Damage_state:
    def __init__(this, hitbox_reg,hp):
        this.Hitbox_regions = hitbox_reg
        this.HP = hp


class Depolyable_game_enity(mov.phy_Character):
    def __init__(self,pos,behavour_steering):
        super().__init__(pos)
        steering_b = behavour_steering
        #self.pos = pos #wd_t.Vector(0, 0)
        self._damage_stat = None
    def update_steering(self):
      ster_out  =  self.steering_b.get_steering()

    @property
    def damage_stat(self):
       return self._damage_stat

    @damage_stat.setter
    def damage_stat(this, HB_reg, hp):
       this._damage_stat.hitbox_regions = HB_reg
       this._damage_stat.HP = hp


class Anima(Depolyable_game_enity):
    def __init__(self,ana_type, pos, dS):
        super().__init__(pos, dS)
        self.collision_radius:float = 0.0
        self.scale: float = 1.0

    def add_texture(self,base_texture, pos, r_type, *params):
       # self.texture = wd_t.Renderable_texture(base_texture, pos, r_type, params)


# for Que if que is nrgitve - this means "run infinently till disabeld or destroeyd"

class Spawner(Anima):
    def __init__(self, pos, Damg_stat):
        super('_Spawner', self).__init__(pos,Damg_stat)

        #ds lookup
        self.active     = False
        self.alive      = True
        self.que        = 0
        self.rate       = 1
        self.cooldown   = 100
        self.spwan_list = []

    def configure(self, **params):

        if params.has_key('rate'):
            self.rate     = params['rate']
        if params.has_key('cooldown'):
            self.cooldown = params['cooldown']
        if params.has_key('que'):
            self.que      = params['que']

    def __call__(self, dt):

        if self.active == False:
            return None
        #clean_spawnList()
        if self.que = 0:
            return 'EMPTY'
        if not self.cooldown_passed(dt):
            return 'UNCOOL'
        else:
            return #(que,spawn_list)

    def activate_spawner(self):
        self.active = True

    def deactivate_spawner(self):
        self.active = False

    def request_a_spawn(self):
        self.que += 1

    def add_spawnable(self, sge):
        self.spwan_list.append(sge)


    def clean_spawnList (self):
        for sp in self.spawn_list:
            if sp.alive is False:
                self.spwan_list.remove(sp)


    def cooldown_passed(self, tick):
        if self.cooldown%tick == 0:
            return True
        return False




#class anima_mgmt:
#    def __init__(this):


    #def update(self):


   # def bind_render_to_text_fac(render):
    #    this.texture_sprite_factory = wd_t.sdl2.ext.SpriteFactory(rend.render)

   # def create_animated_anima(this,type,name,spawn_point):
   #     aan  = Anima.animated_anima()

      #  animated_anima_list.append()

  #  def add_texture_for_compoent(this, type, name):


#class sprit_sheet:
 #   def __init__(this,path, row, column, w, h):

   # def select_sprite(this,x,y):
    #def




#entity_damage_stats.g
   # def load_image_texture(this,):

  #  def set_hit_box(this, points:Point_list):

 #   def get_hit_box(this)->Point_list:
     #   if this._points is None and this.image_texture


#class animated_anima(anima):
