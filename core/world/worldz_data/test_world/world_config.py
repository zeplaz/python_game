#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:11:45 2021
_
@-created by :_zeplaz's


##########################
config for a test world

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN



_________________________________//
##################################
"""
import core.world.worlddata_types as wd_t 
import core.world.anima as anima_t  

name = 'test_world0A'

f16A0eng_Pos wd_t.Vector(100, 100)

spA1_Pos = wd_t.Vector(560, 300)

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

 
Background00_texture_path = 'world/worldz_data/backgound_resttest.png'

#test_world_backroung_01A = Background 
f16a01ENG_Anima01  = anima_t.Anima(f16A0eng_Pos,'F16_ENGINE_TEST',F16A01ENG_DS_STAT_00)  


f16a01ENG_Anima01.add_texture()
gen01_Anima01      = anima_t.Anima(spA1_Pos,'generator_',spA1_DS_STAT_00)  
spA1_Anima01       = anima_t.Anima(spA1_Pos,anima_t.Anima_Type.SPAWNER_,spA1_DS_STAT_00) 
pl01_Anima01       = anima_t.Anima(spPlayer01_Pos,anima_t.Anima_Type.PLAYER_01,PL01_DS_STAT_00)   
#anima_t.Anima(spA1_Pos,'SPWANER_',spA1_DS_STAT_00)   



spawner_A1     = anima_t.Spawner() 

spwaner_player = anima_t.Spawner()