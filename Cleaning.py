# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:57:09 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math

def date_replace(d):
    date_time = d.split('T')
    date = date_time[0]
    time = date_time[1]
    year, month, day = [int(i) for i in date.split("-")]
    hour, minute, second = [int(i) for i in time.split(":")]
    
    return dt.datetime(year, month, day, hour, minute, second)

code_station = {72528014733: 'Buffalo', 99999914768 : 'Rochester', 72529014768 : 'Rochester', 72519014771 : 'Syracuse'}


df = pd.read_csv("newmaster_dropped.csv")

print(df.head())

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
        
# df.loc[size - 1, 'HourlyDryBulbTemperature'] = df.loc[size - 2, 'HourlyDryBulbTemperature']
print(df['HourlyDryBulbTemperature'].count())

print(df['HourlyDryBulbTemperature'])
    

df.to_csv("newmaster_dropped_v2.csv", index = False)
