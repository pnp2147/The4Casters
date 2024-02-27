# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:35:48 2024

@author: mazur
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import collections
from matplotlib.ticker import PercentFormatter

# for reference: f'{comb:020b}' turns int to bit string

df_wt = pd.read_csv('wt_freq.csv')

grouped = df_wt.groupby('STATION')

for name, group in grouped:
    wt_sorted = group.sort_values(by='Occurrences', ascending = False)
    wt_sorted["percent"] = wt_sorted['Occurrences'].cumsum()/wt_sorted['Occurrences'].sum()*100

    fig, ax = plt.subplots()
    ax.bar(wt_sorted['WeatherType'], wt_sorted["Occurrences"], color="C0")
    ax2 = ax.twinx()
    ax2.plot(wt_sorted['WeatherType'], wt_sorted['percent'], color="C1", marker="D", ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())

    ax.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_xlabel('WeatherType')
    ax.set_ylabel('Occurrences')
    fig.suptitle(name + ' Overall Weather Frequency')
    plt.show()