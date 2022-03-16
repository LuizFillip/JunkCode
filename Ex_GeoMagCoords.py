# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:43:54 2021

@author: LuizF
"""

import pandas as pd
import numpy as np
from JunkCode.GeoMagCoords import *

infile = "C:\\Users\\LuizF\\OneDrive\\Documentos\\"

df = pd.read_excel(infile + "PlasmaBubbles.xlsx", sheet_name='sites')

output = []





for city, country in zip(df['site'].values, 
                         df['country'].values):
    try:
        lat_geo, lon_geo = get_coords(city, country)
        lat_mag, lon_mag = string_to_list(0, lat_geo, lon_geo)
        
        output.append([f"{city}, {country}", 
                           lat_geo, lon_geo, 
                           lat_mag, lon_mag])
    except:
        print(f"{city}, {country} doesn't work")
        output.append([f"{city}, {country}", 
                           np.nan, np.nan, 
                           np.nan, np.nan])


#def DataFrame(output, dataframe, comma = True):

df.index.name = "acc"
df.columns = ["name", "lat_geo", "lon_geo", 
              "lat_mag", "lon_mag"]

df = df.sort_values(by=['name'], ascending = True)

print(df)
df.to_csv(infile + "sites.txt", index = True, sep = ';')    
