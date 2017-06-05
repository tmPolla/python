# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:23:08 2017

@author: MarosiPA
"""

# week 1 - problem set - Problem 3

#TASK SCRIPT
#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s 
#in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. 
#For example, if s = 'abcbcd', then your program should print
#
#Longest substring in alphabetical order is: abc

#s = 'azcbobobegghakl'
#s = 'abcbcd'
s = 'zyxwvutsrqponmlkjihgfedcba'

#print(ord('a'))
#print(s)

maxlen=0
maxlenTemp=0
result=""
resultTemp=""

for i in range(len(s)-1):
    j=i
    maxlenTemp=0
    resultTemp=""
    
    resultTemp = resultTemp+s[j]
    while ord(s[j])<=ord(s[j+1]):
        #print ("j(",j,"): ", s[j]," j+1 (",j+1,"): " ,s[j+1])
        resultTemp = resultTemp+s[j+1]
        #print ("resultTemp: ",resultTemp)
        maxlenTemp+=1
        if j+2>len(s)-1:
            break
        else:
            j+=1
        
    if maxlen<maxlenTemp:
        maxlen=maxlenTemp
        result = resultTemp
    if maxlen==0:
        result=s[0]
        
print ("Longest substring in alphabetical order is:", result)