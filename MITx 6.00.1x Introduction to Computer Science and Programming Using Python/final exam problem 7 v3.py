# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:12:39 2017

@author: Polla
Final Exam   Problem 7
Incorrect (10.59/20 points)
"""

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    
    
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc=center_loc
        self.tents_list=list()
#        self.tents_list.append(self.center_loc)
        self.tents_list.append(tent_loc)

      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        flag_toadd=True
        for i in self.tents_list:
            loc_new=Location(new_tent_loc.x, new_tent_loc.y)
            loc_old=i
            dist=loc_new.dist_from(loc_old)
            if abs(dist)<0.5:
                flag_toadd=False
        if flag_toadd==True:
            self.tents_list.append(loc_new)
            return True
        else:
            return False
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        flag_of_error=False
        for i in self.tents_list:
            if i==tent_loc:
                self.tents_list.remove(i)
                flag_of_error=True
        if flag_of_error==False:
            raise ValueError
            
            
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        # Your code here
        result_list=list()
        for i in self.tents_list:
            result_list.append(str(i))
        return sorted(result_list)



        
#Test: 0
print("test 0")
c = MITCampus(Location(1,2))
print("True => ", c.add_tent(Location(1,2)))
print("False => ",c.add_tent(Location(0,0)))
print("True => ", c.add_tent(Location(2,3)))
print("False => ", c.add_tent(Location(2,3)))
print("['<0,0>', '<1,2>', '<2,3>'] => ", c.get_tents())
print("")

#Test: 1
print("Test: 1 => ['<0,0>']")
c = MITCampus(Location(-1,-2))
print(sorted(c.get_tents()))
print("")

#Test: 10
print("Test: 10 => False")
c = MITCampus(Location(1,2), Location(0,0))
c.add_tent(Location(10,10))
print(c.add_tent(Location(10,10)))
print("")

#Test: 11
print("Test: 11 => True")
c = MITCampus(Location(1,2), Location(0,0))
print(c.add_tent(Location(1,2)))
print("")

#Test: 12
print("Test: 12 => Done!")
c = MITCampus(Location(1,2), Location(0,0))
c.add_tent(Location(1,1))
try:
    c.remove_tent(Location(1,1))
except ValueError:
    print("ValueError received.")
else:
    print("Done!")
print("")

#Test: 13
print("Test: 13 => Done!")
c = MITCampus(Location(1,2), Location(0,0))
try:
    c.remove_tent(Location(1,1))
except ValueError:
    print("ValueError received.")
else:
    print("Done!")
print("")    


#Test: 2
print("Test: 2 => ['<10,20>']")
c = MITCampus(Location(1,2),Location(10,20))
print(sorted(c.get_tents()))
print("")

#Test: 3
print("Test: 3")
c = MITCampus(Location(1,2),Location(-1,-2))
print("True => ", c.add_tent(Location(1,2))) # this should actually work!
print("True => ", c.add_tent(Location(-1,-2)))
print("False => ", c.add_tent(Location(-1,-2)))
print("False => ", c.add_tent(Location(-1,-2)))
print("False => ", c.add_tent(Location(-1,-2)))
print("['<-1,-2>', '<1,2>']=> ", sorted(c.get_tents()))
print("")

#Test: 4
print("Test: 4")
c = MITCampus(Location(1,2), Location(0,1))
print("True => ", c.add_tent(Location(1,2)))
print("True => ", c.add_tent(Location(2,3)))
print("True => ", c.add_tent(Location(-1,-2)))
print("True => ", c.add_tent(Location(-2,-3)))
print("['<-1,-2>', '<-2,-3>', '<0,1>', '<1,2>', '<2,3>'] => ",sorted(c.get_tents()))
print("")

#Test: 5
print("Test: 5")
c = MITCampus(Location(1,2), Location(0,1))
c.add_tent(Location(-1,2))
c.add_tent(Location(1,-10))
c.add_tent(Location(1,10))
c.add_tent(Location(1,20))
c.add_tent(Location(1,40))
print("['<-1,2>', '<0,1>', '<1,-10>', '<1,10>', '<1,20>', '<1,40>'] =>", sorted(c.get_tents()))
print("")

#Test: 6
print("Test: 6")
c = MITCampus(Location(1,2), Location(3,1))
print("True => ", c.add_tent(Location(2.5,1)))
c = MITCampus(Location(1,2), Location(3,1))
print("True => ", c.add_tent(Location(2.49,1)))
c = MITCampus(Location(1,2), Location(3,1))
print("False => ", c.add_tent(Location(2.51,1)))
print("")

#Test: 7
print("Test: 7")
c = MITCampus(Location(1,2), Location(3,1))
c.add_tent(Location(1,1))
print("True => ", c.add_tent(Location(1.5,1)))
c = MITCampus(Location(1,2), Location(3,1))
c.add_tent(Location(1,1))
print("False => ", c.add_tent(Location(1.49,1)))
c = MITCampus(Location(1,2), Location(3,1))
c.add_tent(Location(1,1))
print("True => ", c.add_tent(Location(1.51,1)))
print("")

#Test: 8
print("Test: 8")
c = MITCampus(Location(1,2), Location(1,0))
c.add_tent(Location(0,1))
print("True => ",c.add_tent(Location(0,0)))
print("")

#Test: 9
print("Test: 9")
c = MITCampus(Location(1,2), Location(0,0))
print("False => ", c.add_tent(Location(0,0)))