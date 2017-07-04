# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:21:21 2017

@author: MarosiPA

Midterm Exam   Midterm Exam   Problem 7

Problem 7
20.0 points possible (graded)
Write a function called dict_invert that takes in a dictionary with 
immutable values and returns the inverse of the dictionary. 
The inverse of a dictionary d is another dictionary whose keys are 
the unique dictionary values in d. The value for a key in the inverse 
dictionary is a sorted list (increasing order) of all keys in d that 
have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    result_d=dict()

    
    for k, v in d.items():
        try:
            result_d[v].append(k)
        except KeyError:
            result_d[v]=[k]
    
    for k, v in result_d.items():
        result_d[k]=sorted(v)
    
    return result_d
    
    
    
d = {1:10, 2:20, 3:30}    
print("d = {1:10, 2:20, 3:30} => {10: [1], 20: [2], 30: [3]} => ", dict_invert(d))
print("")

d = {1:10, 2:20, 3:30, 4:30}  
print("d = {1:10, 2:20, 3:30, 4:30} => {10: [1], 20: [2], 30: [3, 4]} => ", dict_invert(d))
print("")

d = {4:True, 2:True, 0:True}  
print("d = {4:True, 2:True, 0:True} => {True: [0, 2, 4]} => ", dict_invert(d))
print("")

d = {8: 6, 2: 6, 4: 6, 6: 6}
print("d = {8: 6, 2: 6, 4: 6, 6: 6} => {6: [2, 4, 6, 8]} => ", dict_invert(d))
print("")