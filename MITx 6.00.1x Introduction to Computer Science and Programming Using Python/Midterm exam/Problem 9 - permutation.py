# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:05:07 2017

@author: MarosiPA
Midterm Exam   Midterm Exam   Problem 9

Write a Python function that takes in two lists and calculates whether they are 
permutations of each other. The lists can contain both integers and strings. 
We define a permutation as follows:

the lists have the same number of elements
list elements appear the same number of times in both lists
If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting 
of the following elements:

the element occuring the most times
how many times that element occurs
the type of the element that occurs the most times
If both lists are empty return the tuple (None, None, None). If more than one 
element occurs the most number of times, you can return any of them.

For example,

if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then 
is_list_permutation returns (1, 3, <class 'int'>) because the integer 1 
occurs the most, 3 times, and the type of 1 is an integer (note that the 
third element in the tuple is not a string).
Paste your entire function, including the definition, in the box below. 
Do not leave any debugging print statements.
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    dict_L1=dict()
    dict_L2=dict()
    result_tup=()
    
    for key in L1:
        try:
            dict_L1[key]+=1
        except KeyError:
            dict_L1[key]=1
    
    for key in L2:
        try:
            dict_L2[key]+=1
        except KeyError:
            dict_L2[key]=1
    
#    print(dict_L1)
#    print(dict_L2)
    
    if dict_L1==dict_L2 and dict_L1=={}:
        return (None, None, None)
    
    elif dict_L1==dict_L2:
#        print("True")
        max_value=0
        for k,v in dict_L1.items():
            if max_value<v:
                max_value=v
                max_key=k
        result_tup=(max_key, max_value, type(max_key))
        return result_tup
    else:
        return False
                       
                       

##############################################################################

#Test case 1    
L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
print(is_list_permutation(L1, L2))
print("")


#Test case 2
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))
print("")


#Test case 3
L1 = []
L2 = []
print(is_list_permutation(L1, L2))
print("")