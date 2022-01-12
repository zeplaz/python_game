#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*************************_
"""
"""

##########################
world_config.py
##########################

SETUP TO PARSE WORLD DATA from some external editor or what not. for now
world _congig takes in a set of parmaters and returns a world.


##########################
|*  ->currently::config for a test world
##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

_________________________________//
##################################
"""

import core.world.anima as anima_t
import core.world.world as world
import core.resources as rez
import core.world.worlddata_types as wd_t
import sys



"""
|*==================================================================
|*                          LOCAL VARIABLES
|*==================================================================
"""

SPRITE_SCALING_BASE = 0.25
SPRIT_SCALING_F16_BASE = 0.2
SPRIT_SCALING_SAM_BASE = 0.5
SPRIT_SCALING_RADAR_BASE = 0.5
SPRIT_SCALING_WARHOG = 0.3

"""
|*==================================================================
"""




class Zone:
    def __init__(self, **params):

        self.rect = params['rect_size']
        self.backgroundtex_name = params['background_tex_name']

        # self.paramz = params

class World:
    def add_zone(this, name, **params):
        this.zone_map = {name, Zone(params)}

    def add_zones(self, *args):
        for zone in args:
            self.add_zone(zone.name, zone.params)
class world_config:
    def __call__(self, *args, **kwargs):

         w =  world.World()
         w.add_zone(kwargs['zones'])
        return w




"""
|*==================================================================
|*                          Test_World0A
|*              - hardcoded sample test configuration data for a world and its participants. 
|*    @ for world configure test.
|*==================================================================
"""

"""
|*==================================================================
|*                      PATHS AND CONSTANTS
|*==================================================================
"""


name = 'test_world0A'
sys.intern(name)


Background00_texture_path = 'world/worldz_data/background_resttest.png'

"""
|*==================================================================
|*                          ZONES AND WORLD
|*==================================================================
"""


f16A0eng_Pos    = wd_t.Vector(100, 100)

spA1_Pos        = wd_t.Vector(560, 300)

spPlayer01_Pos = wd_t.Vector(30, 75)

spA1_HRegon_00    = anima_t.Hitbox_region(-5,-7,4,5)
spA1_HPR_00       = 4
spA1_DS_STAT_00   = anima_t.Damage_state(spA1_HRegon_00,spA1_HPR_00)


PL01_HR_00        = anima_t.Hitbox_region(-3,-2,3,1)
PL01_HPR_00       = 5
PL01_DS_STAT_00   = anima_t.Damage_state(PL01_HR_00,PL01_HPR_00)

F16A01ENG_HR_00        = anima_t.Hitbox_region(-3,-2,3,1)
F16A01ENG_HPR_00       = 5
F16A01ENG_DS_STAT_00   = anima_t.Damage_state(F16A01ENG_HR_00,F16A01ENG_HPR_00)



#test_world_backroung_01A = Background



f16a01ENG_Anima01  = anima_t.Anima(f16A0eng_Pos,'F16_ENGINE_TEST',F16A01ENG_DS_STAT_00)

f16a01ENG_Anima01.add_texture()

gen01_Anima01      = anima_t.Anima(spA1_Pos,'generator_',spA1_DS_STAT_00)
spA1_Anima01       = anima_t.Anima(spA1_Pos,anima_t.Anima_Type.SPAWNER_,spA1_DS_STAT_00)
pl01_Anima01       = anima_t.Anima(spPlayer01_Pos,anima_t.Anima_Type.PLAYER_01,PL01_DS_STAT_00)
#anima_t.Anima(spA1_Pos,'SPWANER_',spA1_DS_STAT_00)



spawner_A1     = anima_t.Spawner()

spwaner_player = anima_t.Spawner()
