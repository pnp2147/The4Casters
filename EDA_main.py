# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:55:33 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math

"""
Code for some column conversions
"""

def weather_decode(wt_str):
    """
    function to decode weather string to bit string

    Parameters
    ----------
    wt_str : String
        String of weather types obtained from original HourlyWeatherType column.

    Returns 
    -------
    Bit flag with index correlating to weather type (0 not present, 1 present).

    """
    wt_ind = {'FG' : 0, 'TS' : 1, 'PL' : 2, 'GR' : 3, 'GL' : 4, 'DU' : 5, 'HZ' : 6, 'BLSN' : 7, 'FC' : 8, 'WIND' : 9, 'BLPY' : 10, 'BR' : 11, 'DZ' : 12, 'FZDZ' : 13, 'RA' : 14, 'FZRA' : 15, 'SN' : 16, 'UP' : 17, 'MIFG' : 18, 'FZFG' : 19 }
    wt_typ = list(wt_ind.keys())
    
    if wt_str == "" :
        return None
    
    AU_AW_MW = wt_str.split("|")
    print(wt_str)
    print(AU_AW_MW)
    AU = AU_AW_MW[0]
    AW = AU_AW_MW[1]
    MW = AU_AW_MW[2]
    
    wt_bit = ""
    
    for i in len(wt_typ):
        current = wt_typ[i]
        flag = AU.contains(current) | AW.contains(current) | MW.contains(current)
        wt_bit += flag
        
    return wt_bit

code_station = {72528014733: 'Buffalo', 99999914768 : 'Rochester', 72529014768 : 'Rochester', 72519014771 : 'Syracuse', 99999914771 : 'Syracuse'}
wt = 'HourlyPresentWeatherType'


"""
Code below is just for dropping columns
"""

# df = pd.read_csv("Master.csv")
# cols = pd.read_csv("ColumnReference.csv")

# print(cols)

# droppers = cols["getting rid of"].tolist()

# print(droppers)

# df_refined = df.drop(columns = droppers)

# df_refined.to_csv("master_dropped")

df = pd.read_csv("C:/Users/mazur/Documents/School/2023-2024 Spring/Data Mining/Project/CSI420EDA/The4Casters/newmaster_dropped_v2.csv")

print(df[df["STATION"] == 99999914771])

df["STATION"] = df["STATION"].apply(lambda x: code_station[x])

df['DATE'] = pd.to_datetime(df['DATE'])

df[wt] = df[wt].apply(lambda x: weather_decode(str(x)))

print(df[wt])


