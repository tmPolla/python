# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:22:15 2017

@author: MarosiPA
"""

str1 = 'exterminate!' 
str2 = 'number one - the larch'

print(str1.isupper())

str2 = str2.capitalize()
print (str2)

print(str2.swapcase())

print(str2.find('n'))
print(str2.find('n'))
#print(str2.index('!'))
print(str2.find('!'))

str1 = str1.replace('e', '*')
print(str1)