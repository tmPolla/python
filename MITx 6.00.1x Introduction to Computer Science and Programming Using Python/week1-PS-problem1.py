# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:40:40 2017

@author: MarosiPA
"""

# week 1 - problem set - Problem 1

#TASK SCRIPT
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in 
#the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:

s = 'azcbobobegghakl'
count=0

for i in range(len(s)):
    if s[i] =='a' or s[i] =='e' or s[i] =='i' or s[i] =='o' or s[i] =='u' :
           count = count + 1
           
           
print ("Number of vowels:",count)