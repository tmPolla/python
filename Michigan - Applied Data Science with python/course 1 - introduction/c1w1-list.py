# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:59:16 2017

@author: Polla
Michigan - Applied DS Course 1 week 1
"""

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

#times_tables() == [???]
times_tables() == [j*i for i in range(10) for j in range(10)]


lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

#answer = [???]
#correct_answer == answer

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids