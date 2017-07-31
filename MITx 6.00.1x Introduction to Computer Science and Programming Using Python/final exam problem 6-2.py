# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 17:42:30 2017

@author: Polla
Final Exam   Problem 6-2
"""

#Do not override any methods of Container
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        count=0
        for k,v in self.vals.items():
            if k==e:
                count+=v
        return count

    def __add__(self, other):
        for k,v in other.vals.items():
            try:
                self.vals[k] += v 
            except:
                self.vals[k] = 1
        return self                

        
##test case 1
a = Bag()
a.insert(4)
a.insert(4)
a.insert(3)
print("A bag: ", a)
b = Bag()
b.insert(4)
print("B bag: ", b)
print("The sum of them", a+b)