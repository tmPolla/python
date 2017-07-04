# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:14:05 2017

@author: MarosiPA
Midterm Exam   Midterm Exam   Problem 5

Write a Python function that takes in a string and prints out a 
version of this string that does not contain any vowels, according 
to the specification below. 
Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels 
will print Ths s grt!. If s = "a" then print_without_vowels will 
print the empty string .
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels=['a', 'e', 'i', 'o', 'u']
    result_L=[]
    if s=='':
        result_s=''
    for letter in s:
        if letter.lower() not in vowels:
            result_L.append(letter)
    result_s=''.join(result_L)
    print(result_s)
    
print("This is great!", print_without_vowels(s = "This is great!"))
print("a", print_without_vowels(s = "a"))
print('', print_without_vowels(''))
print(print_without_vowels('Here is a simple sentence that makes sense. BYE.'))
