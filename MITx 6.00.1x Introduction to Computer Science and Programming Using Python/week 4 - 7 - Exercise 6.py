# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:17:32 2017

@author: MarosiPA

Week 4: Good Programming Practices   7. Testing and Debugging   Exercise 6
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        print("here comes the call")
        print(x, a)
#        rem(x-a, a)
        return rem(x-a, a)

        
        
print(rem(2, 5))
print(rem(5, 5))
print(rem(7, 5))