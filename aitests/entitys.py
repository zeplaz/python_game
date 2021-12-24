
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Sat Dec 18 23:23:00 2021
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

"""
#

SDL_EventType

"""
class Counter():
    count = 0
    @staticmethod #here
    def incrment(this):
        this.count +=1
        return count

class Next_ID(Counter):
    def __init__(this):
        super().increment()

class Next_ID():
    @staticmethod #here
    def __init__():
        global the_next_id
        newid = the_next_id
        the_next_id +=1
        return newid

class E_ID:
    def __init__(this):
        return Next_ID()

class Entity:
    def __init__(this, in_ghosty):
        this.is_ghost = in_ghosty

class Caracter(Entity):
    def __init__(this, in_pos, in_or, in_ghosty):
        Entity.__init__(in_ghosty)
        this.pos = in_pos
        this.orientaion = in_or

    def move_request_velocity(this, new_vel):
        this.pos = move_algurthm(new_vel)

    def move_request_force_plus(this, new_force):
        this.pos = move_algurthm(new_force)
