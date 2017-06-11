# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:18:56 2017

@author: MarosiPA
"""

# calculate factorial

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(4))