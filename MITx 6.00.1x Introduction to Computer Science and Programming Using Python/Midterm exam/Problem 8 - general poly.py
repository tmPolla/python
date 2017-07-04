# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:58:20 2017

@author: MarosiPA

Midterm Exam   Midterm Exam   Problem 8

Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 
because 1∗103+2∗102+3∗101+4∗100.
"""




def general_poly_v1 (L):    
    k=len(L)
    base=10
    result=0
    for i in L:
        result=result+i*(base**(k-1))
        k-=1
    return result
        
 
    
""" L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
def general_poly (L):
    
    def f1(L, base):
        k=len(L)-1
        result=0
        for i in L:
            result=result+i*(base**k)
            k-=1
        return result
    
    def f2(base, l=L):
        return f1(l, base)
    
    return f2

       
print ("1, 2, 3, 4 => 1234 => ",general_poly_v1([1, 2, 3, 4]))


print ("1, 2, 3, 4 => 1234 => ",general_poly([1, 2, 3, 4])(10))