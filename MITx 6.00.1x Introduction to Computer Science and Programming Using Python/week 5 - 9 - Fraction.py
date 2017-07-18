# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:06:17 2017

@author: MarosiPA
Week 5: Object Oriented Programming   9. Classes and Inheritance   Video: Classes Examples
"""

class fraction(object):
    def __init__(self,numer, denom):
        self.numer=numer
        self.denom=denom
    
    def __str__(self):
        return str(self.numer)+'/'+str(self.denom)
    
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    def __add__(self, other):
        numerNew=other.getDenom()*self.getNumer()\
                               +other.getNumer()*self.getDenom()
        denomNew=other.getDenom()*self.getDenom()
        return fraction(numerNew, denomNew)
    
    def __sub__(self, other):
        numerNew=other.getDenom()*self.getNumer()\
                               -other.getNumer()*self.getDenom()
        denomNew=other.getDenom()*self.getDenom()
        return fraction(numerNew, denomNew)
    
    def convert(self):
        return self.getNumer()/self.getDenom
    
    
#usage
oneHalf=fraction(1,2)
twoThrids=fraction(2,3)

print(oneHalf)
print(twoThrids)
print("")

new=oneHalf+twoThrids
print(new)

secondNew=twoThrids-oneHalf
print(secondNew)