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
import os

##3rdparty moduals
#import OpenGL
import sdl2
#import sdl2.ext as sdlext
#import pygame

## sorce moduals
import core.render as rend
#import core.world.resources as rez
#import core.resources as rez
import core.worlds.world as world_m
# condtionals for opration

run = True
sigma_running = True
R_TESTS = False
#engine status
INITAL   = 1
CONFIG   = 3
IGNITION = 4
RUNNING  = 5
ERROR_HANDLED = 0
ERROR_FATAIL = -1
ERROR_UNKNOWN = -2


sigma_status = INITAL


class Engine:
    def __init__(this,start, withtests):
        global run, R_TESTS
        R_TESTS = withtests
        this.root_path = os.path.dirname(os.path.abspath(__file__))
        this._render = rend.render()
        this.worldmgmt = world_m.World_mgmt(this.root_path,this._render)
       
        if start is not None:
            run = start

        if run:
            this.__run__()

    def __test__(self):
        print("\n ****************ENGINE)((()__TEST__())()))*******\n")
      #  this.rez =  rez.Rez(this.root_path, this._render)
       # this.rez.__test__()
        
        self.worldmgmt.load_world('testworld_0A')
        

    def __run__(this):

        this.startup()

        if R_TESTS:
          this.__test__()

       #rend.window.show()

    def loop(this):
        global sigma_running, sigma_status
        sigma_status = RUNNING
        while sigma_running:
            this.sdl_event_poll()
            this.render_update()
            this.update_ai()
        else:
          print('shutdown \n |-called closing..properly so far,,?,')

    def update_ai(this):
        return

    def render_update(this):
        this._render.prep()
        
        #this._render.draw()

    def handle_sdl2window_event(this, event):
        global sigma_running
        print("handling sdl2_window events")
        if event == sdl2.SDL_WINDOWEVENT_CLOSE:
            sigma_running = False


    def sdl_event_poll(this):
        #if sdl2.SDL_PollEvent(event)!=0:
        global events, sigma_running
        events = sdl2.ext.get_events()
        for event in events :
            if event.type == sdl2.SDL_QUIT:
                sigma_running = False
                break;
            if event.type == sdl2.SDL_WINDOWEVENT :
                this.handle_sdl2window_event(event)


    def startup(this):
        print("startup")
        global events

        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        events = sdl2.ext.get_events()
        #rez = rez(this.root_path)

    def shutdown(this):
        print("shutdown engine called")
        #this.rez.shutdown()
        this._render.shutdown()
        sdl2.SDL_Quit

    
