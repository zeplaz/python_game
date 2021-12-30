#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 01:04:25 2021

@author: matthew
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
