#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
%(date)s
_
@-created by :_zeplaz's


##########################

pytestgame.py

##########################
________________________________
@USSAGE 
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

// when run as main will run tests.
//otherwise holds engine class and high level system orginzation
_________________________________//
##################################
"""

#CLASSNAME.mro()  #@list
#CLASSNAME.__mr__#@tuple 
 
import sys
#import aitests.movments as mov 
#import aitests.collision as phy_eng 
#import core.render as rend
import core.engine as Eng
stuffdats = ["losts", "lof", "stuff"]


def test_code()-> int: 
    if len(sys.argv) > 1: 
        for data in sys.argv:
            print(data)
    else: 
        print("\n #-> defult run no cmdz enterd ___#\n")
    i = 1
    sd = False
    while not (sd == True):
 
        if sd == False: 
            print(i)
            i+= 1
            if i == 10 :
              sd = True
              i = 0 
    else:
        print("i is no longer less than 6""{}",sd)
       
        
if __name__ == '__main__':
    sys.exit(test_code())