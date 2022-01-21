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
class move_algurthm:
    def __call__(**kwargs):

    if 'velocity' in kwargs:
        return kwargs['velocity']*dt
    if 'force' in kwargs:
        return kwargs['force']*dt
    if 'rotation' in kwargs:
        return kwargs['rotation']*dt

    return None


class Entity:
    def __init__(this, in_ghosty):
        this.is_ghost = in_ghosty

class Caracter(Entity):
    def __init__(this, in_pos, in_or, in_ghosty):
        Entity.__init__(in_ghosty)
        this.pos = in_pos
        this.orientaion = in_or

    def move_request_velocity(this, new_vel):
        this.pos = move_algurthm('velocity',new_vel)

    def move_request_force_plus(this, new_force):
        this.pos = move_algurthm('force',new_force)

    def orientaion_update():
        this.orientaion  = move_algurthm('orientation')
