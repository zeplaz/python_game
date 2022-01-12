#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
movments.py
##########################

##########################
|*  ->
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN
ian ai for games, book was used in creating this

_________________________________//
##################################
"""




class Kinematic:
    def __init__(this):
        pass

    def update(this,steering_out,max_sp,dt):
            this.pos += velocity*dt
            this.orienation = rotation*dt
            steering_out.linear*dt
            steering_out.angular*dt


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
        pass

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
        pass

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
        pass

class Arrive(Velocity_match):
    def __init__(this):
        pass

##___VELOCITY_MATCH__FIN___

###___FORCE_FEILD_____
class Force_feild:
    def __init__(this):
        pass

class Seperation(Force_feild):
    def __init__(this):
        pass


##___FORCE_FEILD_____FIN___
