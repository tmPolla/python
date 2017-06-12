# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:45:06 2017

@author: MarosiPA

Exercise: is in

We can use the idea of bisection search to determine if a character 
is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're 
looking for (the "test character"). If they are the same, we are done - we've 
found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the 
middle character. If so, we need only consider the lower half of the string; 
otherwise, we only consider the upper half of the string. (Note that you can 
compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea 
recursively to test if char is in aStr. char will be a single character 
and aStr will be a string that is in alphabetical order. The function should 
return a boolean value.

As you design the function, think very carefully about what the base cases 
should be.
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #in case of empty string return False
    if len(aStr)==0:
        return False
    
    halfindex=round(len(aStr)/2)
    halfway=aStr[halfindex]
    #in case of matching
    if halfway==char:
        return True
    #in case of out of the string
    elif len(aStr)==1:
        return False
    #in case of new call
    else:
        if ord(char) < ord(halfway):
            newaStr=aStr[:halfindex]
            return isIn(char, newaStr)
        else:
            newaStr=aStr[halfindex:]
            return isIn(char, newaStr)
            
        
    


print('isIn(char="d", aStr="abcdefg")=True'," ", isIn(char="d", aStr="abcdefg"))
print("isIn('u', 'dfiiqtu')=True"," ",isIn('u', 'dfiiqtu'))
print("isIn('a', '')=False"," ",isIn('a', ''))