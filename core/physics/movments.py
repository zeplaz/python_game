#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
%(date)s
_
@-created by :_zeplaz's


##########################

movments.py

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

_________________________________//
##################################
"""

class Kinematic:
    def __init__(this):
        this.somthing
    def update(this,steering_out,max_sp,dt):
            this.pos += velocity*dt
            this.orienation = rotation*time
            steering_out.linear*time
            steering_out.angular*time
             



class Postion :
    def __init__(this,in_x, in_y, in_z):
        this.x = in_x
        this.y = in_y
        this.z = in_z

class Orienation :
    def __init__(this, in_angle):
        this.angle = in_angle

##___________________ALIGN_

class Align:
    def __init__(this):
        this.something

class Look_where_your_going(Align):
    def __init__(this):
        super().__init__()

class Face(Align):
    def __init(this):
        super().__init__()

##________###30##_ALIGN__FIN_____

####___________Seek_Flee_______
class Seek_Flee:
    def __init__(this):
        this.something

class Wander(Seek_Flee):
    def __init__(this):
        super().__init__()

class Pursue_Evade(Seek_Flee):
    def __init__(this):
        super().__init__()
class Path_following(Seek_Flee):
    def __init__(this):
        super().__init__()
###CLASS COLLISION AVOIDANCE IS IN THIS CHAIN BUT LOCAKED IN OWN MODUAL--collision.pu


###___Seek_Flee__FIN_____

###___VELOCITY_MATCH_____

class Velocity_match:
    def __init__(this):
        this.somthing

class Arrive(Velocity_match):
    def __init__(this):
        this.somthing

##___VELOCITY_MATCH__FIN___

###___FORCE_FEILD_____
class Force_feild:
    def __init__(this):
        this.somthing

class Seperation(Force_feild):
    def __init__(this):
        this.somthing


##___FORCE_FEILD_____FIN___
