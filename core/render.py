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
import sdl2 
import core.utilityz as u 

CLEAR_COLOUR_RGB = sdl2.ext.Color(79,98,155)
DEF_WIN_WIDTH = 800
DEF_WIN_HIGHT = 800
mainname = 'SDL_TEST'
#POINTER(SDL_Window) window
#window = None
renderer_SDL = None
#sdl2.video.SDL_WINDOW_SHOWN 
class render:
    def __init__(this):
        #global window
        this.window =sdlext.Window(mainname, size=(DEF_WIN_WIDTH,
DEF_WIN_HIGHT), flags=sdl2.SDL_WINDOW_OPENGL|sdl2.SDL_WINDOW_RESIZABLE)
        this.create_sdlrender(this.window)
        
  #  def set_window_size(this):
        #this.window
    def update(this):
        global renderer_SDL
        this.window.refresh()
        renderer_SDL.clear(CLEAR_COLOUR_RGB)
        renderer_SDL.present()
    
    def create_sdlrender(this,win):
        global renderer_SDL
        renderer_SDL = sdl2.ext.Renderer(this.window,-1,None,sdl2.SDL_RENDERER_ACCELERATED)
        #sdl2.SDL_SetRenderDrawColor(renderer_SDL,u.ctypes.c_ubyte(75),u.ctypes.c_ubyte(185),u.ctypes.c_ubyte(185),u.ctypes.c_ubyte(255))
       
        renderer_SDL.clear(CLEAR_COLOUR_RGB)
        renderer_SDL.present()


    def shutdown(this):
        global renderer_SDL, running
        print("shuttingdown render")
        sdl2.SDL_GL_DeleteContext
        sdl2.SDL_DestroyWindow
        sdl2.SDL_QuitSubSystem
        del this.window
        del renderer_SDL
        #sdl2.SDL_DestroyRenderer(renderer_SDL)
      #  sdlext.SDL_DestoryWindow(this.window)
        
        
