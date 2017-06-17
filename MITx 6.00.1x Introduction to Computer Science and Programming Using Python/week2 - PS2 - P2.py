# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:38:51 2017

@author: MarosiPA

week2 - Problem set 2 - Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly 
payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according 
to the balance at the end of the month (after the payment 
for that month is made). The monthly payment must be a multiple 
of $10 and is the same for all months. Notice that it is possible 
for the balance to become negative using this payment scheme, which 
is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

import time
start = time.time()


# balance => b
# annualInterestRate => air
# Monthly interest rate => ir
# Monthly unpaid balance => ub
# Minimum fixed monthly payment => mfp
# Updated balance each month =>up_b



##Test Case 1: Lowest Payment: 310
#balance = 3329
#annualInterestRate = 0.2

#Test Case 2: Lowest Payment: 440
balance = 4773
annualInterestRate = 0.2

##Test Case 3: Lowest Payment: 360
#balance = 3926
#annualInterestRate = 0.2

###Test Case 4: Lowest Payment: 29157.09
#balance = 320000
#annualInterestRate = 0.2

numberOfMonths = 12
air=annualInterestRate
b0=balance

#Monthly interest rate = (Annual interest rate) / 12.0
def calc_interest_rate(air):
    ir = air/numberOfMonths
    return ir

#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
def calc_unpaid_balance(b,mfp):
    ub=b-mfp
    return ub

#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
def calc_balance(ub, ir):
    b = ub+(ub*ir)
    return b

ir=calc_interest_rate(air)
#print (ir)

mfp=0
while True:
    for ind in range(numberOfMonths):
        
        print(ind+1, " months:")
    
        ub=calc_unpaid_balance(b0,mfp)
        b=calc_balance(ub, ir)
    
        print(ub)
        print(b)
    
        b0=b
        print("")
    if b0<=0: break
    mfp+=10
    b0=balance
    print(mfp)
#    if mfp==460: break

print("Lowest Payment:", round(mfp,2))

print ('It took', time.time()-start, 'seconds.')