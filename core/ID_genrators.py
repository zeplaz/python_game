#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
ID_genrators.py
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
global the_next_id

import heapq

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

class World_ID:
    def __init__(this):
        return Next_ID()
