# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:06:25 2022

@author: LuizF
"""

import shutil
import glob
import os

infile = "G:\\My Drive\\Others\\PsyTrance\\AllThem\\"

def rename_multiple_files(infile):
    
    _, _, files = next(os.walk(infile))

    for track in files:

        rename = track.replace('y2meta.com - ', '').replace(' (128 kbps)', '')

        os.rename(infile + track, infile + rename)
        print(f'{rename} was renamed')
        
def create_folder(dst_path, FolderName):
    '''
    artist = FolderName
    '''
    try:
        # Use function mkdir for create a new folder 
        # and sum with directory that you want to save
        os.mkdir(dst_path + FolderName)
        #conditions for the folder created 
    except OSError:
        print(f"Creation of the directory {FolderName} failed")
    else:
        print(f"Successfully created the directory {FolderName}")


        
        
_, _, files = next(os.walk(infile))

for track in files:
    args = track.split(' - ')
    
    if len(args) > 2:
        artist = args[0]
        trackid = args[1]
    else:
        # Just the trackif 
        artist = args[0]

    dst_path = "G:\\My Drive\\Others\\PsyTrance\\"
    
    #The new folder will be have same name of artist 
    create_folder(dst_path, artist)
    try:
        shutil.copy(infile + track, f'{dst_path}{artist}\\{track}' )
        print('Copied')
    except:
        print(f'{track} not was copied')        