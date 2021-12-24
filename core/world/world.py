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

import animator.anima as Anima



class world:
    def __init__(this):
        self.air_list = None

    def draw_lists(this)
        self.air_list.draw()

    air_hit_list = arcade.check_for_collision_with_list()


    for airunit in air_hit_list:
        airunit.update_damage()
