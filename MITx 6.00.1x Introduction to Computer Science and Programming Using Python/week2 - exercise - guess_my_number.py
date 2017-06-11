# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:24:45 2017

@author: MarosiPA
"""

#week2 - 3 part - Exercise: guess my number
#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
#your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
#
#When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:
#
#Is your secret number 91?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
#Sorry, I did not understand your input.
#Is your secret number 91?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c



#valid answer 
#h high
#l low
#c correct

print("Please think of a number between 0 and 100!")

answer="i"
guess=0
max=100
min=0

#print("lets do it")

while answer!= "c":
    guess=int((min+max)/2)
    print ("Is your secret number ",guess," ?")
    #while (answer!="h" and answer!="l" and answer!="c")==True:
    answer=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    #print ("your answer was:",answer)
    if (answer!="h" and answer!="l" and answer!="c")==True:
        print ("Sorry, I did not understand your input.")
            
    #print("here comes the checking")
    if answer=="c":
        print("Game over. Your secret number was: ",guess)
        break
    elif answer=="h":
            max=guess
    elif answer=="l":
        min=guess
    answer="i"
        
#print("done")
        