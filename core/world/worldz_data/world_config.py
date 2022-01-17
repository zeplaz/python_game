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



class world_config:
    def __call__(self, *args, **kwargs):
        w =  world.World()
        w.add_zone(kwargs['zones'])
        return w


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

    """
    ##################################
    Behavour_steering_defaults
    ##################################
    """



Base_aline_parm_pak_01 = {
        'max_ang_accel':12,
        'max_rot':45,
        'radius_dest_arrive':15,
        'slow_radius':30}






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

"""
|*started Fixed locations
"""

sp_A1_Pos        = wd_t.Vector(560, 300)
sp_A1_HRegon_00    = anima_t.Hitbox_region(-5,-7,4,5)
sp_A1_HPR_00       = 4
sp_A1_DS_STAT_00   = anima_t.Damage_state(spA1_HRegon_00,spA1_HPR_00)


"""
 give player a start location or, create the player spwaner.
 required parmaters are hitbox_region, HP. which will initalze damge_state and the anima type
"""

# Default player start info

sp_Player01_Pos  = wd_t.Vector(30, 75)

PL01_HR_00        = anima_t.Hitbox_region(-3,-2,3,1)
PL01_HPR_00       = 5
PL01_DS_STAT_00   = anima_t.Damage_state(PL01_HR_00,PL01_HPR_00)
spA1_Anima01       = anima_t.Anima(spA1_Pos,anima_t.Anima_Type.SPAWNER_,spA1_DS_STAT_00)

# f16 engine test starting info

f16A01ENG_Pos_00       = wd_t.Vector(100, 100)
F16A01ENG_HR_00        = anima_t.Hitbox_region(-3,-2,3,1)
F16A01ENG_HPR_00       = 5
F16A01ENG_DS_STAT_00   = anima_t.Damage_state(F16A01ENG_HR_00,F16A01ENG_HPR_00)
f16a01ENG_Anima01  = anima_t.Anima(f16A0eng_Pos,'F16_ENGINE_TEST',F16A01ENG_DS_STAT_00)



spawner_A1     = anima_t.Spawner()
spwaner_player = anima_t.Spawner()

"""
f16A0_01_Pos       = wd_t.Vector(3,2)
f16a01ENG_Anima01.add_texture()



gen01_Anima01      = anima_t.Anima(spA1_Pos,'generator_',spA1_DS_STAT_00)
pl01_Anima01       = anima_t.Anima(spPlayer01_Pos,anima_t.Anima_Type.PLAYER_01,PL01_DS_STAT_00)
#anima_t.Anima(spA1_Pos,'SPWANER_',spA1_DS_STAT_00)

"""
