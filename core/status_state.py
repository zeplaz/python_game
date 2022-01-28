#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
stauts_state.py
##########################

listings of status codes and diffrent states codes used in 
statmechanics and mechines.

##########################
|*  -> 
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN


_________________________________//
##################################
"""
#status
INITAL   = 1
CONFIG   = 3
IGNITION = 4
RUNNING  = 5


#states
#worldstates
PAUSED  = 6 
LOADING = 7
ENDED   = 8
CREDITS = 9
INTRO   = 10
INLEVEL = 11 

#overlays_as_MENUS
MAIN_MENU      = 12
PAUSE_MENU     = 13
OPTIONS_MENU   = 15
SAVE_LOAD_MENU = 16
PLAYER_MENU    = 17
HELP_MENU      = 18
 
# errors for status state
ERROR_HANDLED = 0
ERROR_FATAIL = -1
ERROR_UNKNOWN = -2



