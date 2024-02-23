# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:44:24 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math

code_station = {72528014733: 'Buffalo', 99999914768 : 'Rochester', 72529014768 : 'Rochester', 72519014771 : 'Syracuse', 99999914771 : 'Syracuse'}

df = pd.read_csv("newmaster_dropped_v2.csv")

# print(df[df["STATION"] == 99999914771])

df["STATION"] = df["STATION"].apply(lambda x: code_station[x])

df['DATE'] = pd.to_datetime(df['DATE'])
df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'])
# df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'])

# Here we are making the dictionary for the station codes

print(df.head())

# df.to_csv("master_DBtemp_fixed.csv", index = False)

bystat = df[['DATE', 'STATION', 'HourlyDryBulbTemperature']].groupby(['STATION'])

roc_db = bystat.get_group('Rochester')
syr_db = bystat.get_group('Syracuse')
buf_db = bystat.get_group('Buffalo')

roc_db = roc_db.set_index('DATE')
syr_db = syr_db.set_index('DATE')
buf_db = buf_db.set_index('DATE')

syr_db.sort_index(axis=0)

ind = roc_db.index

""" For checking date range data
for i in range(1,len(ind)):
    if (ind[i] - ind[i-1] ).days > 1:
        print(ind[i])
        print(ind[i-1])
"""
    

roc_rs = roc_db.resample("Y")["HourlyDryBulbTemperature"].mean().dropna(axis = 0)
syr_rs = syr_db.resample("Y")["HourlyDryBulbTemperature"].mean().dropna(axis = 0)
buf_rs = buf_db.resample("Y")["HourlyDryBulbTemperature"].mean().dropna(axis = 0)

roc_rs = roc_rs[(roc_rs > 40)]
syr_rs = syr_rs[(syr_rs > 40)]
buf_rs = buf_rs[(buf_rs > 40)]

# print(roc_db)

plt.plot(roc_rs.index.year, roc_rs)
plt.plot(syr_rs.index.year, syr_rs)
plt.plot(buf_rs.index.year, buf_rs)
plt.legend(["Rochester", "Syracuse", "Buffalo"])
plt.xlabel("Year")
plt.ylabel("Temperature (DegF)")
plt.ylim(0, 60)
plt.show()