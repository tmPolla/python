# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:24:44 2017

@author: Polla
Michigan - Applied DS Course 1 week 2
"""

import pandas as pd
animals=['Tieger', 'Bear', 'Moose']
print(animals)

print(pd.Series(animals))

print("")


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
print(s.index)

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])

s = pd.Series([100.00, 120.00, 101.00, 3.00])

total = 0
for item in s:
    total+=item
print(total)

import numpy as np

total = np.sum(s)
print(total)