# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:07:47 2017

@author: MarosiPA
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s^2/tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of 
the regular polygon. The function returns the sum, rounded to 4 
decimal places.
"""

import math

#perimeter of the polygon
def perimeter(n,s):
    return s*n
    
#area of the polygon 
def area(n,s):
    pi=math.pi
    return (0.25*n*(math.pow(s,2)))/(math.tan(pi/n))

#calculate the polysum after the requirement above    
def polysum(s,n):
    result=(math.pow(perimeter(s,n),2))+area(s,n)
    return round(result,4)


#test cases
  
print("polysum(93, 59)=32502109.9914"," ",polysum(93, 59))

print("polysum(36, 3)=12589.8342"," ",polysum(36, 3))


