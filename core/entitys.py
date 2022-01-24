#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
entitiys.py
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

#untill the proper mvoment algurthsm are finshed. in physics, well just hanlde it here

core.physics.movments as mov

class Hitbox_region:
    def __init__(self,x,y,w,h):
        self.rect = wd_t.Rect(x,y,w,h)
        self.info = 'add_info:or params to hitregions'

class Damage_state:
    def __init__(this, hitbox_reg,hp):
        this.Hitbox_regions = hitbox_reg
        this.HP = hp


class move_override:
    def __call__(dt, **kwargs):

    if 'velocity' in kwargs:
        return kwargs['velocity']*dt
    if 'force' in kwargs:
        return kwargs['force']*dt
    if 'rotation' in kwargs:
        return kwargs['rotation']*dt

    return None

c
class Depolyable_game_enity(mov.phy_Character):
    def __init__(self,pos, ortaion,max_speed, is_ghost):
        super().__init__(pos,ortaion)
        if is_ghost == True
            self.is_ghost = True
        else:
            self.is_ghost = False

        self._damage_stat = None

        self.scale: float = 1.0
        self.steering_b = None

    @property
    def steering_behavour(self):
        if steering_b == None:
            return mov.Steering_out(0,0)
        return self.steering_b()

    @steering_behavour.setter
    def steering_behavour(self, sb):
        self.steering_b = sb

    @property
    def damage_stat(self):
       return self._damage_stat

    @damage_stat.setter
    def damage_stat(this, HB_reg, hp):
       this._damage_stat.hitbox_regions = HB_reg
       this._damage_stat.HP = hp


    def accept(self, vistor):
        return vistor.visit(self)


    def move_request_velocity(self, dt, new_vel):
        self.pos = move_override('velocity',dt, new_vel)

    def move_request_force_plus(this,dt, new_force):
        self.pos = move_override('force',dt, new_force)

    def move_request_rotation(self, dt, new_rotation ):
        self.orientaion  = move_override('rotation', dt, new_rotation)
