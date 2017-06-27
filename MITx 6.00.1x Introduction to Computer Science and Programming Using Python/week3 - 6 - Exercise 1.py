# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:10:41 2017

@author: MarosiPA

Week 3: Structured Types   6. Dictionaries   Exercise 1
"""

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'

#1 Task
print(animals)

#2 Task
animals['c']

#3 Task
animals['donkey']

#4 Task
len(animals)

#5 Task
animals['a'] = 'anteater'
animals['a']

#6 Task
len(animals['a'])

#7 Task
'baboon' in animals

#8 Task
'donkey' in animals.values()

#9 Task
'b' in animals

#10 Task
animals.keys()

#11 Task
del animals['b']
len(animals)

#12 Task
animals.values()



       
#del animals['b']