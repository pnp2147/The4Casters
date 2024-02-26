# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:41:28 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math
from scipy.stats import zscore

df = pd.read_csv('C:/Users/mazur/Documents/School/2023-2024 Spring/Data Mining/Project/CSI420EDA/The4Casters/master_wt.csv')

df['DATE'] = pd.to_datetime(df['DATE'])
df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'])

code_station = {72528014733: 'Buffalo', 99999914768 : 'Rochester', 72529014768 : 'Rochester', 72519014771 : 'Syracuse', 99999914771 : 'Syracuse'}

db_temp = 'HourlyDryBulbTemperature'

gb = df[['DATE', 'STATION', 'HourlyDryBulbTemperature']].groupby('STATION')

roc = gb.get_group('Rochester')
buf = gb.get_group('Buffalo')
syr = gb.get_group('Syracuse')

roc[db_temp] = zscore(roc[db_temp])
buf[db_temp] = zscore(buf[db_temp])
syr[db_temp] = zscore(syr[db_temp])

mask_roc = abs(roc[db_temp]) > 3
mask_buf = abs(buf[db_temp]) > 3
mask_syr = abs(syr[db_temp]) > 3

roc_outliers = roc[mask_roc]
buf_outliers = buf[mask_buf]
syr_outliers = syr[mask_syr]

outliers = pd.concat([roc_outliers, buf_outliers, syr_outliers])

outliers.to_csv('Outliers.csv', index=False)

# roc_mean = roc[db_temp].mean()
# buf_mean = buf[db_temp].mean()
# syr_mean = syr[db_temp].mean()
# roc_s = roc[db_temp].std()
# buf_s = buf[db_temp].std()
# syr_s = syr[db_temp].std()


