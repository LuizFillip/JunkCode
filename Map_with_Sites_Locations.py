# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 09:52:12 2021

@author: LuizF
"""


import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd 
import sys
import numpy as np
#from JunkCode.GeoMagCoords import *

sites = ["Kwajalein, Ilhas Marshall", 
         "Pohnpei, Federated States of Micronesia", 
         "Cebu, Philippines", 
         "Manila, Philippines",
         "Ho Chi Minh City, Vietnam", 
         "Bac Lieu, Vietnam", 
         "Chumphon, Thailand", 
         "Kototabang, Indonesia", 
         "Kodaikanal, India", 
         "Fortaleza, Brasil", 
         "São Luís, Brasil", 
         "Cachimbo, Brasil", 
         "Huancayo, Peru", 
         "Jicarmarca, Peru"]



sites = [['Kwajalein, Ilhas Marshall', 9.13, 167.57], 
         ['Pohnpei, Federated States of Micronesia', 6.89, 158.24], 
         ['Cebu, Philippines', 10.29, 123.9],
         ['Manila, Philippines', 14.59, 120.98], 
         ['Ho Chi Minh City, Vietnam', 10.77, 106.7], 
         ['Bac Lieu, Vietnam', 9.35, 105.51], 
         ['Chumphon, Thailand', 10.38, 99.01], 
         ['Kototabang, Indonesia', -0.2, 100.3], 
         ['Kodaikanal, India', 10.27, 77.51], 
         ['Fortaleza, Brasil', -3.73, -38.52], 
         ['São Luís, Brasil', -2.56, -44.24], 
         ['Cachimbo, Brasil', -5.91, -44.3], 
         ['Huancayo, Peru', -12.08, -75.21], 
         ['Jicarmarca, Peru', -11.98, -76.94]]



fig, ax = plt.subplots(figsize = (10, 10),
                       subplot_kw={'projection': ccrs.PlateCarree()})

ax.stock_img()

lat_step = 15
lon_step = 30
ax.set_xticks(np.arange(-180, 180 + lon_step, lon_step), 
              crs=ccrs.PlateCarree())
ax.set_yticks(np.arange(-90, 90 + lat_step, lat_step), 
              crs=ccrs.PlateCarree())
'''
states_provinces = cfeature.NaturalEarthFeature(
            category='cultural',
            name='admin_1_states_provinces_lines',
            scale='50m',
            facecolor='none')
ax.set_global()

#Setting color for lines of states and countries
color = 'black'
ax.add_feature(cfeature.COASTLINE, lw = 1, edgecolor= color)
ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor=color)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(states_provinces, edgecolor=color)
'''


for site in sites:
    lat = site[1]
    lon = site[2]
    name = site[0].split(', ')[0]
    
    ax.scatter(lon, lat, s = 20, color = 'red', 
            transform = ccrs.PlateCarree(), label = name)
    
    ax.annotate(name, xy=(lon, lat),  xycoords='data',
            xytext=(lon - 100, lat + 10), textcoords='offset points',
            arrowprops=dict(facecolor='black', arrowstyle="->"), 
            horizontalalignment='right', verticalalignment='top',
            transform = ccrs.Geodetic())

ax.axhline(0, color= 'k', linestyle = '--', lw =1)
