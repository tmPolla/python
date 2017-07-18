# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:32:52 2017

@author: MarosiPA
Week 5: Object Oriented Programming   9. Classes and Inheritance   Exercise 3
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

#Task 1
w1 = Weird(X, Y)
print(w1.getX())

#task 2
print(w1.getY())

#Task 3
w2 = Wild(X, Y)
print(w2.getX())

#Task 5
w3 = Wild(17, 18)
print(w3.getX())

#Task 7
w4 = Wild(X, 18)
print(w4.getX())

#Task 9
X = w4.getX() + w3.getX() + w2.getX()
print(X)

#Task 11
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)