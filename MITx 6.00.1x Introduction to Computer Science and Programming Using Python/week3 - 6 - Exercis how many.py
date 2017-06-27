# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:23:29 2017

@author: MarosiPA

Week 3: Structured Types   6. Dictionaries   Exercise: how many
We want to write some simple procedures that work on dictionaries to return information.

"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count=0
    for anim in aDict.values():
        for anim2 in anim:
            count+=1
#           print (anim2)
    return count

print(how_many(animals))