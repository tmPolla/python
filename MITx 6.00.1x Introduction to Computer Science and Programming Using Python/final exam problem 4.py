# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 08:27:44 2017

@author: Polla
Final Exam   Problem 4
def max_val(t): 
     t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
    # Your code here
"""

def make_simple_list(t): 
    result=[]
    for i in t:
        try:
            for j in i:
                result.append(j)
        except:
            result.append(i)
    return result

def max_val(t):
    flag=True
    newT=make_simple_list(t)
    while flag==True:
        flag=False
        for i in newT:
            if type(i) is tuple or type(i) is list:
                flag=True
        if flag==True:
            newT=make_simple_list(newT)
#    print(newT)
    
    maxint=0
    for i in newT:
        if maxint<i:
            maxint=i
    return maxint

    
#test case 1
print("test case 1")
print(max_val((5, (1,2), [[1],[2]])))

print("")

#test case 2
print("test case 2")
max_val((5, (1,2), [[1],[9]]))