#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: matthew
"""
"""
##########################
Main
##########################

##########################
|*  ->currently::config for a test world
|* engine is instanced  and __run__() of the engine is called. 
. output errors, depend on debug mode. 
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN
:::::::::::::::::::::::::::::::::::::::::::::::::


|/**command line commands**\|
start     == (will cause engine to execute __run__ in the init)
R_tests   == (will set the engine to run all default tests) 

#||goto-->
core.engine:: 
the inputs to determine engine startup configurations 

_________________________________//
##################################
"""
import sys

import core.engine as Eng


def main():
   # pygame.init()
#caputre argments.
    def_start = False
    run_tests = True
   
    eng = Eng.Engine(def_start,run_tests)
     
    eng.__run__()
    eng.loop()
    
    eng.shutdown()
    
    print("###30##")
    return 0

#while run:
   # sdl_updater()

if __name__ == "__main__":
    sys.exit(main())
