#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
//***********************************
collision.py

USAGE
_________________________________//
##################################
"""
from aitests import movments as mov

X_POS = 0
Y_POS = 1
W_POS = 2
H_POS = 3

class collision_system:
    
    def rect_test(rect, pos):
        x2, y2 = rect[X_POS]+rect[W_POS], rect[Y_POS]+rect[H_POS] 
        if (rect[X_POS] < pos[X_POS] and pos[X_POS] <x2):
            if (rect[Y_POS] < pos[Y_POS] and pos[Y_POS] < y2):
                return True 
        return False

class Collision:
    def __init__(this,pos,norm):
        this.position = pos
        this.normal = norm 

  """      
class Collision_Detector():
    def __init__(this):
        this.setup
    
    def get_collision(this, position, move_ammount) -> Collision:
        this.runrutine
        
class Collision_Avoidance(mov.Seek_Flee) :
    def __init__(this, in_caracter,in_max_acceleration, b_sphere):
        this.caracter = in_caracter
        this.max_acceleration = in_max_acceleration

        this.goals =[]
        this.radius = b_sphere
class Obstacle_Avoidance(mov.Seek_Flee):
    def __init__(this, in_):
        super().__init__()
 """       