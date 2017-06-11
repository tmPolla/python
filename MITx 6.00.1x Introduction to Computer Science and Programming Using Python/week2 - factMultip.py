# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:16:00 2017

@author: MarosiPA
"""



# calculate a*b

def fact_multip(a,b):
    if b==1:
        return a
    else:
        return a+fact_multip(a,b-1)

print (fact_multip(2,5))