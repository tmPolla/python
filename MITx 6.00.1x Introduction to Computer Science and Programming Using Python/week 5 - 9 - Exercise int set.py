# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:47:06 2017

@author: MarosiPA

Week 5: Object Oriented Programming   9. Classes and Inheritance   Exercise: int set

Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements 
that appear in both sets. In other words,

s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. 
Think carefully - what should happen if s1 and s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of 
elements in s.
"""




class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self, other):
        newSet=intSet()
        for i in self.vals:
            if i in other.vals:
                newSet.insert(i)
        return newSet

    def __len__(self):
        return len(self.vals)


s1=intSet()
s1.insert(2)
s1.insert(3)
s1.insert(5)
print(s1)


s2=intSet()
s2.insert(1)
s2.insert(3)
s2.insert(5)
print(s2)

print("")

s3=intSet.intersect(s1,s2)
print(s3)

print(intSet.__len__(s1))











