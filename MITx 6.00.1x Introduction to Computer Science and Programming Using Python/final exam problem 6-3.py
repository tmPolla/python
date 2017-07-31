# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 17:50:33 2017

@author: Polla
Final Exam   Problem 6-3
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


class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            self.vals[e] = 0
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        result_flag=False
        for k,v in self.vals.items():
            if k==e and v>0:
                result_flag=True
        
        return result_flag


##test case 1
#d1 = ASet()
#d1.insert(4)
#d1.insert(4)
#d1.remove(2)
#print("first remove:", d1)
#d1.remove(4)
#print("second remove:", d1)


#test case 2
d1 = ASet()
d1.insert(4)
print("First insert:", d1)
print(d1.is_in(4))

d1.insert(5)
print("Second insert:", d1)
print(d1.is_in(5))

d1.remove(5)
print("First remove:", d1)
print(d1.is_in(5))