import shutil
import os
import pandas as pd
import numpy as np

year = 2013
site = "SAA"
infile = f"D:/drift/{site}/{year}/"
saveit = f"D:/drift/{site}1/{year}/"

def doy_to_month(year, site, infile, saveit):
    dates = pd.date_range(f"{year}-1-1", 
                          f"{year}-12-31", 
                          freq = "1D")
    
    """
    Copy files from doy folder into month folder
    """
    for dt in dates:
        doy_str = dt.strftime("%j")
        mon_str = dt.strftime("%m")
        
        try:
            dst = os.path.join(saveit, mon_str)
            os.mkdir(dst)
        except:
            pass
        
        try:
            print("coping...", doy_str)
            src = os.path.join(infile, doy_str)
            _, _, files = next(os.walk(src))
            #files = [f for f in files if f.endswith(".DVL")]
            
            for filename in files:
                shutil.copy(os.path.join(src, filename), 
                            os.path.join(dst, filename))
        except:
            pass
        
        
def doy_to_year(year, site, infile, saveit):
    dates = pd.date_range(f"{year}-1-1", 
                          f"{year}-12-31", 
                          freq = "1D")
    