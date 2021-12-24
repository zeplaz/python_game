#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 01:04:25 2021

@author: matthew
"""

import core.engine as Eng


def main():
   # pygame.init()
#caputre argments.
    def_start = False
    eng = Eng.Engine(def_start)

    eng.__run__()
    eng.shutown()

    return 0

#while run:
   # sdl_updater()

if __name__ == "__main__":
    sys.exit(main())
