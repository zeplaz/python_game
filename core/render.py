#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:36:20 2021
_
@-created by :_zeplaz's


##########################


##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN



_________________________________//
##################################
"""
import OpenGL
import sdl2.ext as sdlext


DEF_WIN_WIDTH = 800
DEF_WIN_HIGHT = 800
mainname = 'SDL_TEST'
#POINTER(SDL_Window) window
window = None
renderer = None

class render:
    def __init__(this):
        global window
        this.window =sdlext.Window(mainname, size=(640, 480), flags=sdl2.SDL_WINDOW_OPENGL)
        create_sdlrender(window)

    def create_sdlrender(win):
        global renderer
        renderer = sdl2.ext.Renderer(window,-1,0)
        sdl2.SetRenderDrawColor(renderer,ctypes.c_ubyte(75),ctypes.c_ubyte(185),ctypes.c_ubyte(185),ctypes.c_ubyte(255))
        renderer.clear(0)
        renderer.present()


    def shutdown():
        global window, renderer, running
        sdl2.SDL_DestroyRenderer(renderer)
        sdl2.SDL_DestoryWindow(window)
