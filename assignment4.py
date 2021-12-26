#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:56:58 2021

@author: duyvu
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StockX-Data-Contest-2019-3.csv')
df['Release Date'] = pd.to_datetime(df['Release Date'])
df = df[df['Brand'] != 'Off-White']

df2 = pd.read_csv('multiTimeline.csv')
df2 = df2.drop(labels='Week').rename(columns={'Category: All categories': 'Search Counts compared to max value'})
df2.index = pd.to_datetime(df2.index)
df2 = pd.to_numeric(df2['Search Counts compared to max value'])

release_date = df['Release Date'].sort_values().unique()

plt.figure(figsize=(12,9))
for date in release_date:
    plt.axvline(x=date, ymin=0, ymax=100, lw=1, ls='--', c='r', label='Yeezy Release')
    
plt.plot(df2, label='Yeezy Search Trend', alpha=0.5)

handles, labels = plt.gca().get_legend_handles_labels()
i =1
while i<len(labels):
    if labels[i] in labels[:i]:
        del(labels[i])
        del(handles[i])
    else:
        i +=1

plt.legend(handles, labels, loc='best', prop={'size': 15})
plt.title('Correlation between every Yeezy Release\n and Yeezy Search Trend on Google in the US', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Value converted to 100 scale', fontsize=15)
plt.tick_params(bottom=False, left=False)