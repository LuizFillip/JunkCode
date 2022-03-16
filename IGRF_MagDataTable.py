# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:18:39 2021

@author: LuizF
"""

import matplotlib.pyplot as plt
import pyIGRF
import pandas as pd
import numpy as np
import time
from datetime import datetime as dt

def toYearFraction(date):
    
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

def table_igrf(date = dt(2010, 1, 1)):
    RT = 6370
    longitudes = np.arange(-180, 180, 1)
    latitudes  = np.arange(-90, 90, 1)

    #2010 and 2021
    date_fraction = toYearFraction(date)

    data = []

    for lon in longitudes:
        for lat in latitudes:
            D,I,H,X,Y,Z,F = pyIGRF.igrf_value(lat, lon, 0, date_fraction)
            data.append([lon, lat, I])
            
    df = pd.DataFrame(data, columns = ['Lon', 'Lat', 'Dip'])
    
    return pd.pivot_table(df, values='Dip', index=['Lat'], columns=['Lon'])

table = table_igrf(date = dt(2021, 1, 1))

#save data
table.to_csv("igrf_data.txt", sep = ',')