#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:36:20 2021
_
@-created by :_zeplaz's


##########################
utilityz.py

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

useful small genreal utiltiys for the engine
_________________________________//
##################################
"""
##xore modua

def c_str(string):
    return ctypes.c_char_p(string.encode('utf-8'))
