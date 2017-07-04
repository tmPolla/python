# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:32:21 2017

@author: MarosiPA
Midterm Exam   Midterm Exam   Problem 6


For example, if

largest_odd_times([2,2,4,4]) returns None
largest_odd_times([3,9,5,3,5,3]) returns 9

Paste your entire function, including the definition, 
in the box below. Do not leave any debugging print statements.
"""

def largest_odd(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    max_odd=0
    is_odd=False
    for i in L:
        if i%2==1 and max_odd<i:
            max_odd=i
            is_odd=True
    if is_odd==False:
        return None
    for i in L:
        if i==max_odd:
            return max_odd


def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    dict_odd={"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
#    print (dict_odd)
    for i in L:
        for k,v in dict_odd.items():
            if int(k)==int(i):
                dict_odd[k]+=1
#    print (dict_odd)
    
    max_odd_v=0
    max_odd_k=0
    is_odd=False
    # choosing
    for k,v in dict_odd.items():
        
        if v%2==1:
            if int(max_odd_k)<int(k):  
                is_odd=True
                max_odd_v=v
                max_odd_k=k            
    
    if is_odd==False:
        return None
    else:
        return int(max_odd_k)





print("2, 2 (None): ", largest_odd_times([2, 2]))
print("")

print ("2, 2, 4, 4 (None): ", largest_odd_times([2, 2, 4, 4]))
print("")

print("3, 2 (3):", largest_odd_times([3, 2]))
print("")

print("3, 3, 2, 0 (2): ", largest_odd_times([3, 3, 2, 0]))
print("")

print("3, 0, 5, 3, 5, 3 (3): ", largest_odd_times([3, 0, 5, 3, 5, 3]))
print("")

print("3, 9, 5, 3, 5, 3 (9): ", largest_odd_times([3, 9, 5, 3, 5, 3]))
print("")


print("6, 8, 6, 8, 6, 8, 6, 8, 6, 8 (8): ",largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8]))
print("")

print("2, 4, 5, 4, 5, 4, 2, 2 (4): ", largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]))

#print("2,2,4,4", largest_odd_times([2,2,4,4]))

#print("empty", largest_odd_times([]))