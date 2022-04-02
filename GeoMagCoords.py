# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:12:59 2021

@author: LuizF

In this Python code, the user can extract, with "requests" library,
the coordinates (latitude and longitude) from city's name and country 
and convert to geomagnetic coordinates, after organize into Pandas's dataframe

"""

import numpy as np
import requests
import spacepy.coordinates as coord
from spacepy.time import Ticktock
import pandas as pd
import sys

def get_coords(city, country):
    
    """
    Function for get latitude and longitude
    from name of city and country. Use 'Request' library
    for scrapy these informations
    -----
    Example
    -------
    get_coords(city = 'Campina Grande', 
               country = 'Brazil')
    >>> (-7.22, -35.88)
    """

    url_site = "https://nominatim.openstreetmap.org/?" 
    
    addressdetails = f"addressdetails=1&q={city}+{country}&format=json&limit=1"
    
    response = requests.get(url_site + addressdetails).json()
    
    lat = float(response[0]["lat"])
    lon = float(response[0]["lon"])
    return round(lat, 2), round(lon, 2) 
 
        

def geo_to_mag(alt, lat, lon):
    #call with altitude in kilometers and lat/lon in degrees 
    
    Re = 6371.0 #mean Earth radius in kilometers
    
    #setup the geographic coordinate object with altitude in earth radii 
    cvals = coord.Coords([float(alt + Re)/Re, 
                          float(lat), float(lon)], 
                         'GEO', 'sph', ['Re','deg','deg'])
    
    #set time epoch for coordinates:
    cvals.ticks = Ticktock(['2021-01-01T12:00:00'], 'ISO')
    
    #return the magnetic coords in the same units as the geographic:
    return cvals.convert('MAG','sph')

def string_to_list(alt, lat, lon):
    
    """
    Convert the results from 'geo_to_mag' functions
    from numeric tuple
    
    """

    first = str(geo_to_mag(alt, lat, lon))
    
    start = first.find('[[')
    end = first.find(']]')
    last = first[start + 2:end].split(', ')
    
    list_as_numeric = [float(num) for num in last]
    
    lat_mag = list_as_numeric[1]
    lon_mag = list_as_numeric[2]
    return round(lat_mag, 2), round(lon_mag, 2)


def main(cities, countries):
    '''
    Example
    Enter with a list of sites and their country   
    '''

    output = []

    for city, country in zip(cities, 
                             countries):
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
    
    df = pd.DataFrame(output)
    # In case of dataframe is the output
    #df.index.name = "acc"
    #df.columns = ["name", "lat_geo", "lon_geo", 
                  #"lat_mag", "lon_mag"]
    
    #df = df.sort_values(by=['name'], ascending = True)
    
    return df

