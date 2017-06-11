# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:24:45 2017

@author: MarosiPA
"""

#week2 - 3 part - Exercise: guess my number

#valid answer 
#h high
#l low
#c correct

print("Please think of a number between 0 and 100!")

answer="init"
guess=0
max=100
min=0

print("lets do it")

while answer!= "c":
    guess=(min+max)/2
    print ("Is your secret number ",guess," ?")
    while answer!="h" or answer!="l" or answer!="c":
        answer=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        print ("your answer was:",answer)

print("done")
        