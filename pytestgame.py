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
import aitests.collision as phy_eng 

stuffdats = ["losts", "lof", "stuff"]

class engine:
    def __init__(this):
        global  shutdown_sigma
        shutdown_sigma = False
        
    def loop(this):
        global shutdown_sigma
        
        while not (shutdown_sigma == True):
            for x in stuffdats:
                print(x)
            shutdown_sigma = True
        else:
            print('shutdown \n |-called closing..properly so far,,?,')
        
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
        meng  = engine() 
        meng.loop()
        
if __name__ == '__main__':
    sys.exit(test_code())