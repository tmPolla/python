# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:11:48 2017

@author: MarosiPA
Week 4: Good Programming Practices   7. Testing and Debugging   Exercise 7
def f(n):

   n: integer, n >= 0.

   if n == 0:
      return n
   else:
      return n * f(n-1)
When we call f(3) we expect the result 6, but we get 0.

When we call f(1) we expect the result 1, but we get 0.

When we call f(0) we expect the result 1, but we get 0.
"""

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
  
    
print(f(3))