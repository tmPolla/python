# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:06:33 2017

@author: MarosiPA

Fibonacci
"""

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(5))