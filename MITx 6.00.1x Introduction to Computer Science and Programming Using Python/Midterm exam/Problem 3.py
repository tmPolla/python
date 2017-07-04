# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:58:55 2017

@author: MarosiPA
Midterm Exam   Midterm Exam   Problem 3
"""

#Problem 3-1

stuff  = "iQ"
for thing in stuff:
    if thing == 'iQ':
        print("Found it")
        
#Problem 3-2
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(3))
print(Square(-3))
print(Square(0))
print(Square(2.0))
print(Square(1))