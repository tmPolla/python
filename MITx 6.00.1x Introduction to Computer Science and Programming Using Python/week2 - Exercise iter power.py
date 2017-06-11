# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:21:01 2017

@author: MarosiPA

Write an iterative function iterPower(base, exp) 
that calculates the exponential baseexp by simply using 
successive multiplication. For example, iterPower(base, exp) 
should compute baseexp by multiplying base times itself exp times. 
Write such a function below.

This function should take in two values - 
base can be a float or an integer; exp will be an 
integer ≥ 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==0:
        return 1
    else:
        return base*recurPower(base,exp-1)

print(recurPower(base=2, exp=3))



def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    res=base
    if exp==0:
        return 1
    else:
        for i in range(exp-1):
            res=res*base
        
        return res


print(iterPower(base=2, exp=3))