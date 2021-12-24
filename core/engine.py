#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:36:20 2021
_
@-created by :_zeplaz's


##########################
engine.py

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

contains the main engine for the game
utilzing opengl, sdl2 and ai systems from ian

_________________________________//
##################################
"""
##xore moduals
import sys
import ctypes

##3rdparty moduals
import OpenGL
import sdl2
import sdl2.ext as sdlext
#import pygame

## sorce moduals
import render as rend

# condtionals for opration
run = True
sigma_running = True

#engine status
INITAL   = 01
CONFIG   = 03
IGNITION = 04
RUNNING  = 05
ERROR_HANDLED = 0
ERROR_FATAIL = -1
ERROR_UNKNOWN = -2


sigma_status = INITAL

class Engine:
    def __init__(this,start):
        global run
        if (start is not None)
            run = start

        this.root_path = os.path.dirname(os.path.abspath(__file__))

        if run
            this._run__()

    def __run__(this):

       this.startup()
       rend.window.show()

    def loop(this):
        global sigma_running, sigma_status
        sigma_status = RUNNING
        while sigma_running:
            this.sdl_updater()
            this.render_update()
            this.update_ai()


    def render_update():
        this.rend.window.refresh()


    def sdl_event_poll(this):
        global events, sigma_running
        events = sdl2.ext.get_events()
        for event in events :
            if event.type == sdl2.SDL_QUIT:
                sigma_running = False
    #if sdl2.SDL_PollEvent(event)!=0:
    ##

    def sdl_updater():
        sdl2.SDL_RenderPresent(this.renderer_SDL)
        sdl_event_poll()


    def startup():
        print("startup")
        global events

        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        events = sdl2.ext.get_events()
        rez = _rez(this.root_path)

    def shutdown():
        this.rez.shutdown()
        this.rend.shutdown()

        sdl2.SDL_Quit
        exit()
