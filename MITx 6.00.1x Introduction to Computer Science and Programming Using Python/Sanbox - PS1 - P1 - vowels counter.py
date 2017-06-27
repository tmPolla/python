# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:44:51 2017

@author: MarosiPA

Sandbox   Problem Set 1   Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

#Test 0
s = 'azcbobobegghakl'

vowels=['a', 'e', 'i', 'o', 'u']

count=0
for letter in s:
    if letter in vowels: count+=1

print (count)