# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:04:52 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math

df = pd.read_csv("Master_locations.csv")

roc_db = df.loc[df['STATION'] == "Rochester", ['HourlyDryBulbTemperature']].astype('float64')
syr_db = df.loc[df['STATION'] == "Syracuse", ['HourlyDryBulbTemperature']].astype('float64')
buf_db = df.loc[df['STATION'] == "Buffalo", ['HourlyDryBulbTemperature']].astype('float64')

# print(roc_db)

roc_ct, roc_bin = np.histogram(roc_db, bins = 15)
# roc_ct = np.divide(roc_ct, np.sum(roc_ct))
    
syr_ct, syr_bin = np.histogram(syr_db, bins = 15)
# syr_ct = np.divide(syr_ct, np.sum(syr_ct))
    
buf_ct, buf_bin = np.histogram(buf_db, bins =15)
# buf_ct = np.divide(buf_ct, np.sum(buf_ct))

plt.stairs(roc_ct, roc_bin)
plt.stairs(syr_ct, syr_bin)
plt.stairs(buf_ct, buf_bin)
plt.legend(["Rochester", "Syracuse", "Buffalo"])
plt.xlabel("Temperature (degF)")
plt.ylabel("Normalized Frequency")
plt.show()


# print(df.columns.values.tolist())

# print(df)