# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:34:05 2017

@author: MarosiPA

Week 3: Structured Types   6. Dictionaries   Exercise: biggest

We want to write some simple procedures that work on dictionaries to return 
information.

This time, write a procedure, called biggest, which returns the key corresponding 
to the entry with the largest number of values associated with it. If there is more than one 
such entry, return any one of the matching keys.
"""


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')




def biggest(aDict):
    max=0
    maxKey=''
    for k, v in aDict.items():
#        print (k)
#        print (v)
        if max<len(v):
            maxKey=k
            max=len(v)
    return maxKey
    
print(biggest(animals))


#Test case 2
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))