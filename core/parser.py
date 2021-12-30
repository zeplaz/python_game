#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*******************************
Thu Dec 23 01:36:20 2021
_
@-created by :_zeplaz's


##########################
utilityz.py

##########################
________________________________
@USSAGE
::vaild FOR:: MIT - UNLESS OTHERWISE OVERWTITEN

parsers for game data and metadates
including
jason_parser: for handling json files
->currently handlily spritsheet data files
 _________________________________//
##################################
"""

import json
import os
import core.world.worlddata_types as wd_t

META_POS  = 0
FRAMEZ_POS = 1

F_NAME_POS       = 0
F_DIMETIONS_POS  = 1
F_SPRIT_SIZE_POS = 2

M_IMAGE_PATH_POS  = 0
M_SHEET_SIZE_POS  = 1
M_SCALE_POS       = 2
M_FORMATE_POS     = 3

class jason_parser:
    def parse_jsonfile(this, dirctory, filename):
        suffix  = '.json'
        loadpath = os.path.join(dirctory,filename + suffix)
        jsonfile = this.load_file(loadpath)
        return jsonfile

    def load_file(this, file):
        with open(file) as f:
            raw_data = json.load(f)
            return raw_data

    def print_raw(this, in_data):
        print('\n ##-->RAW DATA FROM Json::\n', in_data)

    def print_use_key(this,key,sdict):
        print('\n##--->valz in:',key,"\n %-*:::",sdict[key])


class game_data_parser(jason_parser):

    def load_airunits_data (this,dirct,filename, type):
        jfile_dic = this.parse_jsonfile(dirct,filename)

        flist = list(jfile_dic.keys())
        for i in flist:
            print('\n |**********************|\n #->metaz::Ikey::', i)

        return jfile_dic["Air_Units"]



    def __test__(this, rootp):
        dir = rootp + '/world/unit_data'
        filename = 'json_unit_data'
        this.load_airunits_data(dir,filename,'Air_Units')

        #if (type == 'ENGINE_TEST_A'):



    #def create_game_object_config_file(this,jsonfile):


class sprit_sheet_parser(jason_parser):
    #def __init__(this):
       # super().__init__()
    #def create_sprit_sheet_data(this): ->
    def load_spirtsheet_data(this, dirct, filename):
        jfile_dic = this.parse_jsonfile(dirct,filename)

        framlist = this.split_frames(jfile_dic['frames'])
        sheet_meta = this.split_meta(jfile_dic['meta'])

        sheet_tuple = wd_t.sprit_sheet(sheet_meta,framlist)
        return sheet_tuple

    def split_meta(this, metaz):
        print('\n theobjecttype of metaz::', type(metaz), "\n***\n")
        flist     = list(metaz.keys())

        sheet_size_dict = metaz['size']
        sheet_size      = wd_t.np.array([sheet_size_dict['w'],sheet_size_dict['h']])
        scale_k         = metaz['scale']
        formate         = metaz['format']
        image_path      = metaz['image']

        sm = wd_t.sprit_meta(image_path,sheet_size,scale_k,formate)

        return sm

    def split_frames(this, framez):

        print('\n theobjecttype of framez::', type(framez), "\n***\n")
        #print('n/##+fullframe',framez)
        flist = list(framez.keys())
        spfame_list= []

        count = 0
        for i in flist:
        #    print('\n |**********************|\n #->framez::Ikey::', i)
            count +=1
            frame_data = framez[i]
            #inner_keys = list(frame_data.keys())
            frame_dimetions = frame_data['frame']
            f_d = wd_t.Rect(frame_dimetions['x'],frame_dimetions['y'],frame_dimetions['w'],frame_dimetions['h'])
            sprit_size_dict = frame_data['sourceSize']
            sprit_size = wd_t.np.array([sprit_size_dict['w'],sprit_size_dict['h']])


        spfame_list.append(wd_t.sprit_sheet_data(i,count,f_d,sprit_size))

        print('listlength::',len(spfame_list))
        return spfame_list
        #frame_list = []


    def __test__(this, rootp):

        dir = rootp + '/world/animationz/f16/f16_engine/'
        filename = 'f16_engine_on_00'
        sheet_tuple  = this.load_spirtsheet_data(dir, filename)

        dir = rootp + '/world/animationz/f16/f16_leftwing'
        filename = 'f16_leftwing_base_damage_00'
        sheet_tuple  = this.load_spirtsheet_data(dir, filename)

        print('\n*************sprit_SHeet_info*********************\n')

       # print("LEN:",len(sheet_tuple))
        print("TYPE:",type(sheet_tuple))
      # metadats = sheet_tuple[META_POS]
       # for x in metadats:
        #   print(type(x))
         #  print(x)
        #print('framelist::',len(framelist))
        #for i in framelist:
        #print(framelist)

       # this.print_raw(jsonfile)
        #Sthis.print_use_key('frames',jsonfile)
