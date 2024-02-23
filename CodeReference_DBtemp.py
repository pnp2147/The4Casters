# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 19:28:22 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math

df = pd.read_csv("master_date.csv")
stations = pd.read_csv("StationCodes.csv")

df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'], errors='coerce')
size = df.shape[0]
print(df['HourlyDryBulbTemperature'])
print(df['HourlyDryBulbTemperature'].count())
for i in range(1, size-1):
    val = df['HourlyDryBulbTemperature'].iloc[i]
    if math.isnan(val) :
        a = 1
        # print("whoops we got ourselves some trouble: ", val)
        while a < 100:
            try:
                last_i = df['HourlyDryBulbTemperature'].iloc[i - a]
                next_i = df['HourlyDryBulbTemperature'].iloc[i + a]
                interp = (next_i + last_i) / 2
                if math.isnan(interp):
                    raise Exception()
                df.loc[i, 'HourlyDryBulbTemperature'] = interp
                # print(interp)
                # print(last_i)
                # print(next_i)
                break
            except:
                a += 1
                # print("increasing loop size to:", a)
                continue
        
df.loc[size - 1, 'HourlyDryBulbTemperature'] = df.loc[size - 2, 'HourlyDryBulbTemperature']
print(df['HourlyDryBulbTemperature'].count())

print(df['HourlyDryBulbTemperature'])
    

df.to_csv("master_DBtemp_fixed.csv", index = False)