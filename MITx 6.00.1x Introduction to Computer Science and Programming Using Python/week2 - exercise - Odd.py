# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:10:16 2017

@author: MarosiPA
"""

#Exercise: odd
#
#Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.
#
#You should use the % (mod) operator, not if.
#
#This function takes in one number and returns a boolean.

def odd(x):
    return x%2==0
    
    
print(odd(-74))