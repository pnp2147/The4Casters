# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:09:30 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import collections

# for reference: f'{comb:020b}' turns int to bit string

def mode(x):
    """
    manual mode calculation because ofc the pandas and scipy versions don't work for
    what I want to do.

    Parameters
    ----------
    x : pandas series
        categorical variable.

    Returns
    -------
    tuple
        (most common occurence within series, count)

    """
    return collections.Counter(x).most_common(1)

def bitnot(n, numbits=20):
    return (1 << numbits) - 1 - n

def compare_wt(x, y):
    """
    returns the bitwise difference between two input bits

    Parameters
    ----------
    x : int
        weather bit string 1.
    y : int
        weather bit string 2.

    Returns
    -------
    int
        DESCRIPTION.

    """
    
    """diff = 0
    # make sure we don't make a negative int
    if x > y:
        diff = x - y
    else:
        diff = y - x"""
    
    return (x & bitnot(y)) | (bitnot(x) & y)
    
    
def persistance(ds_wt, col):
    """
    """
    sz = ds_wt.shape[0]
    
    wt_counter = {}
    
    for i in range(sz):
        # print("loop", i)
        if ds_wt[col].iloc[i] == []:
            continue
        wt_str = ds_wt[col].iloc[i][0][0]
        if wt_str == '':
            wt_str = 20 * '0'
        wt_bit = int(wt_str, base=2)
        # print(f"current {wt_bit:020b}")
        
        if wt_bit not in wt_counter.keys():
            wt_counter[wt_bit] = 1
        else:
            wt_counter[wt_bit] += 1
        
        
    wt_counter_final = {}
    
    # just converting the final list to a string instead of ints
    for key in wt_counter.keys():
        key_str = f'{key:020b}'
        wt_counter_final[key_str] = wt_counter[key]
    return wt_counter_final
            


df = pd.read_csv('C:/Users/mazur/Documents/School/2023-2024 Spring/Data Mining/Project/CSI420EDA/The4Casters/master_wt.csv')

df['DATE'] = pd.to_datetime(df['DATE'])
df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'])

code_station = {72528014733: 'Buffalo', 99999914768 : 'Rochester', 72529014768 : 'Rochester', 72519014771 : 'Syracuse', 99999914771 : 'Syracuse'}

wt = 'HourlyPresentWeatherType'

grps = df.groupby('STATION')

roc_df = grps.get_group('Rochester').set_index('DATE')[wt]
buf_df = grps.get_group('Buffalo').set_index('DATE')[wt]
syr_df = grps.get_group('Syracuse').set_index('DATE')[wt]

roc_days = roc_df.resample("D").apply({wt : (lambda x :  mode(x))})
buf_days = buf_df.resample("D").apply({wt : (lambda x :  mode(x))})
syr_days = syr_df.resample("D").apply({wt : (lambda x :  mode(x))})




wt_ind = {'FG' : 0, 'TS' : 1, 'PL' : 2, 'GR' : 3, 'GL' : 4, 'DU' : 5, 'HZ' : 6, 'BLSN' : 7, 'FC' : 8, 'WIND' : 9, 'BLPY' : 10, 'BR' : 11, 'DZ' : 12, 'FZDZ' : 13, 'RA' : 14, 'FZRA' : 15, 'SN' : 16, 'UP' : 17, 'MIFG' : 18, 'FZFG' : 19 }
wt_typ = list(wt_ind.keys())

per = persistance(roc_days, wt)


wt_list = []

for key_p in per.keys():
    str_cond = []
    for key_w in wt_ind.keys():
        if key_p[wt_ind[key_w]] == '1':
            str_cond.append(key_w)
    wt_list.append({'STATION' : 'Rochester', 'WeatherType' : str_cond, 'Occurrences' : per[key_p] })

per = persistance(buf_days, wt)

for key_p in per.keys():
    str_cond = []
    for key_w in wt_ind.keys():
        if key_p[wt_ind[key_w]] == '1':
            str_cond.append(key_w)
    wt_list.append({'STATION' : 'Buffalo', 'WeatherType' : str_cond, 'Occurrences' : per[key_p] })
    
per = persistance(buf_days, wt)

for key_p in per.keys():
    str_cond = []
    for key_w in wt_ind.keys():
        if key_p[wt_ind[key_w]] == '1':
            str_cond.append(key_w)
    wt_list.append({'STATION' : 'Syracuse', 'WeatherType' : str_cond, 'Occurrences' : per[key_p] })
    

wt_count = pd.DataFrame(wt_list)
print(wt_count)

