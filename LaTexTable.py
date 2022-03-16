# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:23:41 2021

@author: LuizF
"""

import pandas as pd 
import numpy as np
from textwrap import wrap

infile = "C:\\Users\\LuizF\\OneDrive\\Documentos\\PlasmaBubbles.xlsx"

df = pd.read_excel(infile, sheet_name='ground')

del df['Unnamed: 7']

df = df.sort_values(by=['Ano'], ascending = False)

df = df.dropna()


def separe_elem(set_names):
    autor = set_names[0] 
    year = int(set_names[1])
    start = set_names[2]
    end = set_names[3]
    istr = ' \\\ '.join(wrap(set_names[4], 17)) 
    goal = ' \\\ '.join(wrap(set_names[5], 20)) 
    result = " \\\ ".join(wrap(set_names[6], 20))
    
    part_1 = f"\citeonline{{{autor}{year}}} & {start} & {end} &"
    part_2 = f" \makecell{{{istr}}} & \makecell{{{goal}}} & \makecell{{{result}}}\\\ "
    
    return part_1 + part_2


result = [separe_elem(list(df.iloc[i, :])) for i in range(len(df))]


final = " \n ".join(result)

word = "magnetômetro (FZ)"

print(len(word))
#print(separe_elem(list(df.iloc[0, :])))