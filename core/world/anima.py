#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:11:45 2021
_
@-created by :_zeplaz's


##########################


##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN



_________________________________//
##################################
"""
import os
from enum import Enum

import core.parser as pars
import core.world.worlddata_types as wd_t
import core.render as rend

class Anima_Type(Enum):
    FLOCK_AIR_01 = 1
    FLOCK_AIR_02 = 2
    GROUND_SAM_91 = 91
    GROUND_RADAR_61 = 61
    F16_ENGINE_TEST = 72
    TEST_MULTI_CRAFT = 83

anima_types = {
        'FLOCK_AIR_01':     1,
        'FLOCK_AIR_02':     2,
        'GROUND_SAM_91':   91,
        'GROUND_RADAR_61': 61,
        'F16_ENGINE_TEST': 72,
        'TEST_MULTI_CRAFT':83
        }

class anima_mgmt:
    #def __init__(this)

    def bind_render_to_text_fac(render):
        this.texture_sprite_factory = wd_t.sdl2.ext.SpriteFactory(rend.render)

    def create_animated_anima(this,type,name,spawn_point):
        aan  = Anima.animated_anima()

        animated_anima_list.append()

    def add_texture_for_compoent(this, type, name):


class sprit_sheet:
    def __init__(this,path, row, column, w, h):

    def select_sprite(this,x,y):
    #def






class damage_state:
    def __init__(this, hitbox_reg,anima_reg,hp):
        this.hitbox_regions = hitbox_reg
        this.HP = hp


class depolyable_game_enity:
    def __init__(this):
        this.damage_stat = None
        orign = wd_t.np.array([0.0,0.0])

   @property
   def entity_damage_stats(this):
       return this.damage_stat

   @entity_damage_stats.setter
   def entity_damage_stats(this, HB_reg, hp):
       this.damage_stat.hitbox_regions = HB_reg
       this.damage_stat.HP = hp

#entity_damage_stats.g
   # def load_image_texture(this,):

  #  def set_hit_box(this, points:Point_list):

 #   def get_hit_box(this)->Point_list:
     #   if this._points is None and this.image_texture

class anima(depolyable_game_enity):
    def __init__(this):
        this.collision_radius = None
        #filename: str = None,
        scale: float = 1.0,


class animated_anima(anima):
    def set_animation_frames(inspritsheet, cols, rows, col_w, row_h, s_col=0, s_row=0)
        inspritsheet.set_animation(cols, rows, col_w, row_h, s_col, s_row)


TextureSprite(**kwargs).set_animation(
        10, 1, 32, 32)


sdl2.ext.sprite.SpriteFactory(sprite_type=0, **kwargs)
