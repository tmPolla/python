# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:31:46 2017

@author: MarosiPA

week 3 - 5 - Exercise: apply to each
"""

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
        

#[1, 4, 8, 9]

def own_abs(a):
    if a<0:
        return a*-1
    else:
        return a

#applyToEach(testList, own_abs)
#print(testList)



def add_one(a):
        return a+1

#applyToEach(testList, add_one)
#print(testList)



def plus_power(a):
    return a**2
    

applyToEach(testList, plus_power)
print(testList)