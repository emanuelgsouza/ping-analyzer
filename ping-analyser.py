#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:00:48 2018

@author: emanuel
"""

import pandas as pd

getValuesFromLine = lambda line : line.split(' ')[5:8]

def getValFromColumn(val):
    name, val = tuple(val.split('='))
    if name in ['icmp_seq', 'ttl']:
        val = int(val)
    else:
        val = float(val)

    return (name, val)

getValuesFromColumn = lambda line : dict(list(map(getValFromColumn, line)))

with open('./ping.file.txt', 'r') as file:
    lines = list(filter(lambda x : '64 bytes' in x, list(file.readlines())))
    clearedLines = list(map(getValuesFromLine, lines))
    clearedColumns = list(map(getValuesFromColumn, clearedLines))
    
    # create a DataFrame from values
    df = pd.DataFrame(clearedColumns, columns = ['icmp_seq', 'ttl', 'time'])
    
    # save to CSV
    #df.to_csv('ping.csv', index = False)
    
    # show column types
    df.dtypes
    
    # describe
    df.describe()
    
    # show graphic
    df.plot.scatter(x='icmp_seq', y='time')
