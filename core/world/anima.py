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


from pygame.sprite import groupcollide
from pygame.sprite import spritecollide
from pygame.sprite import collidemask



class Anima_Type(Enum):
    FLOCK_AIR_01 = 01
    FLOCK_AIR_02 = 2
    GROUND_SAM_91 = 91
    GROUND_RADAR_61 = 61

    anima_types = {
        'FLOCK_AIR_01': 01,
        'FLOCK_AIR_02':  2,
        'GROUND_SAM_91':  91,
        'GROUND_RADAR_61': 61,
        }

class damage_state:
    def __init__(this, hitbox_reg,anima_reg,hp):
        this.Hitbox_regions = hitbox_reg
        this.anima_reggions = anima_reg
        this.HP = hp

class _rez:
    def __init__(this, rpath ):
        global renderer
        this.anima_path = Resources(os.path.join(rpath, "animator"))
        this.AnimaZ_RESOURCES_SDL = sdl2.ext.Resources(__file__, "animationz")
        this.sprit_texture_factory = sdl2.ext.SpriteFactory(renderer=renderer)

    def create_texture_spirt(this,filename): ->
            image_path = this.AnimaZ_RESOURCES_SDL.get_path(str(filename))

# Create sprite factory to create surfaces with later
    # Determine path to image to use as texture
    def __test__(this):
        bgimage = this.anima_path.get("background.jpg")


class depolyable_game_enity:
    def __init__(this):
        global renderer
    def load_image_texture(this,):
        
    def set_hit_box(this, points:Point_list):

    def get_hit_box(self)->Point_list:
        if this._points is None and this.image_texture

class anima:
    def __init__(self,cr):
        this.collision_radius = cr
        filename: str = None,
        scale: float =1,


    Bases: object

    A factory class for creating Sprite components.

    __init__(sprite_type=0, **kwargs)

        Creates a new SpriteFactory.

        The SpriteFactory can create TextureSprite or SoftwareSprite instances, depending on the sprite_type being passed to it, which can be SOFTWARE or TEXTURE. The additional kwargs are used as default arguments for creating sprites within the factory methods.



TextureSprite(**kwargs).set_animation(
        10, 1, 32, 32)


sdl2.ext.sprite.SpriteFactory(sprite_type=0, **kwargs)
