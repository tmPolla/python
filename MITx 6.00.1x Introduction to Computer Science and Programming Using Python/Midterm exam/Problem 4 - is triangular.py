# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:06:52 2017

@author: MarosiPA
Midterm Exam   Midterm Exam   Problem 4

Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation 
of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
 corresponding to 1, 3, 6, 10, etc., are triangular numbers.

Paste your entire function, including the definition, in the box below. 
Do not leave any debugging print statements.
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triang=0
    counter=1
    while True:
        triang=triang+counter
        counter+=1
#        print (triang)
        if triang>=k:
            break
    if triang==k:
        return True
    else:
        return False
    
print("2", is_triangular(2))
print("3", is_triangular(3))
print("10", is_triangular(10))