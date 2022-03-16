# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:44:01 2021

@author: LuizF
"""


import pandas as pd
import numpy as np

infile = "C:\\Users\\LuizF\\OneDrive\\Documentos\\"

df = pd.read_csv(infile+ "sites.txt", delimiter=(';'), index_col=("acc"))

df = df.dropna()

df = df.astype(str)

df = df.applymap(lambda x: str(x.replace('.',',')))

print(df.to_latex(index = True))

