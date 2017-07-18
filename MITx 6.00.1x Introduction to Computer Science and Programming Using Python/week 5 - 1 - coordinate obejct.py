# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:03:22 2017

@author: MarosiPA
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distance(self, other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    
    #this help to solve the print(c) otherwise this would be a mess
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    
c=Coordinate(3,4)
origin=Coordinate(0,0)
    
print(c.distance(origin))
print(Coordinate.distance(c,origin))
print(c)