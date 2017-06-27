# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:48:37 2017

@author: MarosiPA

Week 3: Structured Types   5. Tuples and Lists   Exercise 5
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve], -3.0))

#print(applyEachTo([inc, max, int], -3))

print(applyEachTo([inc, square, halve, abs], 3.0))

