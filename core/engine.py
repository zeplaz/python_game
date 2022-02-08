#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
engine.py
##########################

contains the main engine for the game
utilzing opengl, sdl2 and ai systems from ian

##########################
|*  -> currtntly; congigured to run R_test likly at build, but shutoff for client builds.
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN


_________________________________//
##################################
"""

# #xore moduals
import os

# #3rdparty moduals
# import OpenGL
import sdl2
import sdl2.ext

# import pygame

# # sorce moduals
import core.render as rend
import core.world.world as world_m


"""
|*==================================================================
|*                          LOCAL VARIABLES
|*          -conditionals for operation
|*==================================================================
"""

## a UI current pointeresk
run = True
restart = False

sigma_running = True

R_TESTS = False

# sdl input keys states
KEY_UP = 1
KEY_DOWN = 0


#Defult engine status state 
sigma_status = INITAL

"""
|*=================================================================
"""


# i = argvs.index(arg)
# arg == 1 or arg == 'ON' or arg == 'true' or arg == 'True'

class cmd_parser:
    def __call__(self,*argvs):

        L_cmdz_map = []
        for arg in argvs:
            if arg == 'start':
                    L_cmdz_map['start'] = True
            if arg == 'R_tests':
                L_cmdz_map['R_tests'] = True
        return L_cmdz_map

class Engine:
    def __init__(this, *argv):
        global run, R_TESTS
        cmd_pars = cmd_parser()

        Lcmdz_map =  cmd_pars(argv)

        this.root_path = os.path.dirname(os.path.abspath(__file__))
        this._render = rend.render()
        this.worldmgmt = world_m.World_mgmt()


        if Lcmdz_map['R_tests'] is not True:
            R_TESTS = True

        if Lcmdz_map['start'] is not True:
            run = True


    def __test__(self):
        print("\n ****************ENGINE)((()__TEST__())()))*******\n")

        #this.rez =  rez.Rez(this.root_path, this._render)
        #this.rez.__test__()
        self.worldmgmt.__test__(this.root_path ,this._render, 'testworld_0A')




    def __run__(this):
        global run
        this.startup()

        if R_TESTS:
          this.__test__()

        if run == True:
            this.loop()


    def loop(this):
        global sigma_running, sigma_status
        sigma_status = RUNNING

        while sigma_running:
            this.sdl_event_poll()
            this.update_realms()
            this.render_update()
            this.update_ai()
            this.step_physics()
        else:
          print('shutdown \n |-called closing..properly so far,,?,')

    def update_ai(this):
        return

    def step_phycis(self):
        return

    def render_update(this):
        this._render.prep()
        this.worldmgmt.draw()
        #this._render.draw()

    def update_realms(self):
        self.worldmgmt.update_realms()


    def handle_sdl2window_event(this, event):
        global sigma_running
        print("handling sdl2_window events")
        if event == sdl2.SDL_WINDOWEVENT_CLOSE:
            sigma_running = False


    def handle_active_event(self,event):
        print('an active event?')


    def onkeybord(self, updown, e_key):
        print('keypress',updown, "  ", e_key)

    def sdl_event_poll(this):
        #if sdl2.SDL_PollEvent(event)!=0:
        global events, sigma_running
        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                sigma_running = False
                break

            if event.type == sdl2.SDL_KEYDOWN:
                this.onkeybord(KEY_DOWN, event.key)
               # break

            if event.type == sdl2.SDL_KEYUP:
                this.onkeybord(KEY_UP, event.key)
              #  break

        #    if event.type == sdl2.:
         #       this.handle_sdl2window_event(event)
                #break
      #      if event.type == sdl2.SDL_VIDEORESIZE:
       #         this.handle_resize(event.resize)
        #        break

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
        sdl2.SDL_Quit()
