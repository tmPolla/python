# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:34:02 2017

@author: MarosiPA

week3 - 1 - Exercise: odd tuples
Write a procedure called oddTuples, which takes a tuple as input, 
and returns a new tuple as output, where every other element 
of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the 
tuple ('I', 'a', 'tuple').
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    k=0
    resultList=[]
    for i in aTup:
        if k%2==0:
            resultList.append(i)
        k+=1
    return tuple(resultList)

testTup=('I', 'am', 'a', 'test', 'tuple')
#result ('I', 'a', 'tuple')

print (oddTuples(aTup=testTup))