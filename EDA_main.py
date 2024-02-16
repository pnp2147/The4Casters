# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:55:33 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt

"""
Code for some column conversions
"""

def date_replace(d):
    date_time = d.split('T')
    date = date_time[0]
    time = date_time[1]
    year, month, day = [int(i) for i in date.split("-")]
    hour, minute, second = [int(i) for i in time.split(":")]
    
    return dt.datetime(year, month, day, hour, minute, second)


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

# df = pd.read_csv("master_dropped.csv", index_col = 0)
stations = pd.read_csv("StationCodes.csv")

# Here we are making the dictionary for the station codes

code_station = {}

for ind in stations.index:
    code_station[stations['Station'][ind]] = stations['Location'][ind]
    
    
print(code_station)

# print(df.columns.values.tolist())

# print(df)
