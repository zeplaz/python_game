#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************


##########################

render.py
##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN



_________________________________//
##################################
"""
import OpenGL

import ctypes
import sdl2.ext
import sdl2



#
import core.world.worlddata_types as wd_t


CLEAR_COLOUR_RGB = sdl2.ext.Color(79,98,155)
DEF_WIN_WIDTH = 800
DEF_WIN_HIGHT = 800
mainname = 'SDL_TEST'
#POINTER(SDL_Window) window
#window = None

#sdl2.video.SDL_WINDOW_SHOWN

class Frame_dimetions:
    def __init__(this,x,y,w,h):
        this.pos = np.array([x,y])
        this.size = np.array([w,h])

class Layer:
    def __init__(self, rt, a):
       self.texture = rt
       self.alpha = a

class renderable:
    def __init__(self, texture, r_type):
        self.texture = texture
        self.r_type = r_type

    def __call__(self, renderer_SDL, pos):
        frame_des = sdl2.SDL_Rect(pos.X,pos.Y, pos.X+self.frame_size.X, pos.Y + self._frame_size.Y)
        sdl2.SDL_RenderCopy(renderer_SDL, self.texture,self.current_frame,frame_des)

    def sdl_querry_texture_dimesions(self, texture):
        w =  ctypes.c_int()
        h =  ctypes.c_int()
        sdl2.SDL_QueryTexture(texture,None,None,w,h)
        return sdl2.Rect(0,0,w,h)


class  Renderable_Background_texture(renderable):
    def __init__(self,texture, r_type, *params):
        super().__init__(texture, r_type)
        if r_type == 'background_texture':
            self.frame_size = self.texture_dimestion
            self._current_frame(0,0, self.frame_size.X,self.frame_size.Y)

            self.layers = []
            for pr in params:
                self.layers.append(pr)


class Renderable_base_texture(renderable):

        if r_type == 'base_texture':
            self.frame_size = self.texture_dimestion
            self._current_frame(0,0, self.frame_size.X,self.frame_size.Y)
        else:
            print("###ERROR TEXTURE BEING CREATED IS BASE_TEXTURE R_TYPE IS WRONG")



"""
##todo:: get
the sprit sheet indexer to calutate whcih frame . but have the
more complex meaning for those frames delt with at the world level of an "spritsheet_animaited_entity"
"""
class framr_cal:
    def __call__(self,rect, index, col_max, row_max):

        if index = 0 :
            return rect

        w1 = rect.w*index
        if w1 > col_max:
            x1 = rect.x
            w1 = rect.w
            y1 += rect.y
            h1 += rect.h
        else:
            x1 = rect.x*index
            y1 = rect.y*index
            w1 = rect.w*index
            h1 = rect.h*index

        if y1 > row_max
            return None

        return  sdl2.SDL_Rect(x1,y1,w1,h1)


class Renderable_sprit_sheet(renderable):

        @property
        def current_frame(self):
            return self._current_frame

        @current_frame.setter

        def current_frame(self,x,y,w,h):
            self._current_frame = sdl2.SDL_Rect(x,y,w,h)

        def set_current_frame(self,cf):
            self.current_frame = cf




    def __call__(self,renderer_SDL, pos, *params):

        image_index= params[0]
        self.select_frame_from_index(image_index)

        super().__call__(renderer_SDL, pos)

    def __init__(self, texture,  r_type, *params):
        super().__init__(texture,  r_type)
        self.frame_index
        self.texture_dimestion = self.sdl_querry_texture_dimesions(texture)
        self.componets = {}

        if r_type == 'sprit_sheet':
            for fs in params:
                self.frame_size = fs
                self._current_frame(0,0, fs.X,fs.Y)
            """
            for key, comp in comps.items():
                self.componets[key] =  create_compent(key,comp)
                """









"""
class Renderable_sheet_sprit(Renderable_texture):
        def __init__(self,tex,pos, fs):
            super().__init__(self,tex,pos,'sprit_sheet')

"""




class render:
    def __init__(this):
        #global window
        this.renderer_SDL = None
        this.window =sdlext.Window(mainname, size=(DEF_WIN_WIDTH,
DEF_WIN_HIGHT), flags=sdl2.SDL_WINDOW_OPENGL|sdl2.SDL_WINDOW_RESIZABLE)
        this.create_sdlrender(this.window)

  #  def set_window_size(this):
        #this.window
    def draw(self,todraw):
        for rdr in todraw:
            print("draw")
            if(rdr.r_type == 'sprit_sheet'):
                sprit = rez.get_sprit_from_sprit_sheet(rdr);
                sprit.draw();

            if(rdr.r_type == 'static_spirt'):
                sprit = rez.get_static_spirt()

        self.renderer_SDL.present()


    def prep(this):
        #global renderer_SDL
        this.renderer_SDL.clear(CLEAR_COLOUR_RGB)
        this.window.refresh()

    def create_sdlrender(this,win):
       # global renderer_SDL
        this.renderer_SDL = sdl2.ext.Renderer(this.window,-1,None,sdl2.SDL_RENDERER_ACCELERATED)
        #sdl2.SDL_SetRenderDrawColor(renderer_SDL,u.ctypes.c_ubyte(75),u.ctypes.c_ubyte(185),u.ctypes.c_ubyte(185),u.ctypes.c_ubyte(255))

        this.renderer_SDL.clear(CLEAR_COLOUR_RGB)
        this.renderer_SDL.present()


    def shutdown(this):
        global running #,renderer_SDL
        print("shuttingdown render")
        sdl2.SDL_GL_DeleteContext
        sdl2.SDL_DestroyWindow
        sdl2.SDL_QuitSubSystem
        del this.window
        del this.renderer_SDL

        #sdl2.SDL_DestroyRenderer(renderer_SDL)
      #  sdlext.SDL_DestoryWindow(this.window)

"""
    def __init__(this, name, frame, rotated, trimmed, sprit_source_size, source_size, duration):
        this.name = name
        this.frame = frame
        this.rotation = rotation
        this.trimmed = trimmed
        this. sprit_source_size = sprit_source_size
        this.source_size = source_size
        this.duration = duration

        @property
        def pos(self):
            return self._pos

        @pos.setter
        def pos(self, x,y):
            self._pos = Vector2D(x,y)

"""
