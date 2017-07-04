# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:31:44 2017

@author: MarosiPA

Midterm Exam   Midterm Exam   Problem 1
"""

#Problem 1-1
x = "pi"
y = "pie"

print(x)
print(y)

x, y = y, x

print(x)
print(y)

#Problem 1-2
#For any value of x, all calls to f are guaranteed to never terminate.
def f(x):
    while x > 3:
        f(x+1)
        
        
#Problem 1-5
#The following code will enter an infinite loop for all 
#values of i and j.
#while i >= 0:
#    while j >= 0:
#        print(i, j)

t=()
t=(2,"one", [1,2,3])
print(t)