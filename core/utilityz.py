#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
anima.py
##########################

##########################
|*  ->
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN

useful small general utiltiys for the engine
_________________________________//
##################################

"""


##xore modua
import ctypes

def c_str(string):
    return ctypes.c_char_p(string.encode('utf-8'))
