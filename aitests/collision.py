
"""
//***********************************
collision.py

USAGE
_________________________________//
##################################
"""
from aitests import movments as mov

class Collision:
    def __init__(this,pos,norm):
        this.position = pos
        this.normal = norm 

        
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