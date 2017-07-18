# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:34:48 2017

@author: MarosiPA

Week 5: Object Oriented Programming   9. Classes and Inheritance   
Exercise: coordinate

Your task is to define the following two methods for the Coordinate class:

Add an __eq__ method that returns True if coordinates refer to same point 
in the plane (i.e., have the same x and y coordinate).

Define __repr__, a special method that returns a string that looks like a 
valid Python expression that could be used to recreate an object with the 
same value. In other words, eval(repr(c)) == c given the definition 
of __eq__ from part 1.
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
    
    def __repr__(self):
        return "Coordinate("+str(self.getX())+","+str(self.getY())+")"
        
        
a=Coordinate(1,2)
b=Coordinate(1,2)
c=Coordinate(2,3)

print(Coordinate.__eq__(a,b))
print(Coordinate.__repr__(a))
