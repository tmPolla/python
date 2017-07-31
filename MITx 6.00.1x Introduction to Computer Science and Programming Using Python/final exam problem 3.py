# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 08:16:45 2017

@author: Polla
Final Exam   Problem 3

def sum_digits(s):
    assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception.
    # Your code here
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    sum=0
    flag=False
    for char in s:
        try:
            sum+=int(char)
            flag=True
        except:
            ValueError
    
    if flag==True:
        return sum
    else:
        raise ValueError("no number")
                
    
    
#test case 1
print(sum_digits("a;35d4"))

#test case 2
print(sum_digits("ab"))