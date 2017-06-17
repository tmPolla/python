# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:18:07 2017

@author: MarosiPA

week2 - PS2 - Problem 3 - Using Bisection Search to Make the Program Faster

You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment 
than we did in Problem 2 without running into the problem of slow code? 
We can make this program run faster using a technique introduced in lecture - 
bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly 
payment such that we can pay off the entire balance within a year. 
What is a reasonable lower bound for this payment value? $0 is the obvious anwer, 
but you can do better than that. If there was no interest, the debt can be paid off 
by monthly payments of one-twelfth of the original balance, so we must pay at least 
this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we 
paid off the entire balance at the end of the year. What we ultimately pay 
must be greater than what we would've paid in monthly installments, because 
the interest was compounded on the balance we didn't pay off each month. 
So a good upper bound for the monthly payment would be one-twelfth of the balance, 
after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info 
check out the Wikipedia page on bisection search) to find the smallest monthly 
payment to the cent (no more multiples of $10) such that we can pay off the debt 
within a year. Try it out with large inputs, and notice how fast it is 
(try the same large inputs in your solution to Problem 2 to compare!). 
Produce the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not run - 
your code only has 30 seconds to run on our servers.
"""

# balance => b
# annualInterestRate => air
# Monthly interest rate => ir
# Monthly unpaid balance => ub
# Minimum fixed monthly payment => mfp
# Updated balance each month =>up_b


##Test Case 2: Lowest Payment: 440, 434.9
#balance = 4773
#annualInterestRate = 0.2


###Test Case 1: Lowest Payment: 29157.09
#balance = 320000
#annualInterestRate = 0.2

#Test Case 2: Lowest Payment: 90325.03
balance = 999999
annualInterestRate = 0.18

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

#one-twelfth of the original balance
#Monthly payment lower bound = Balance / 12
lowerbound=balance/20
#one-twelfth of the balance, after having its interest compounded monthly for an entire year.
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
upperbound=(balance*(1+ir)**12)/12


mfp=(lowerbound+upperbound)/2
#print("upperbound", upperbound)
#print("lowerbound", lowerbound)
#print("mfp", mfp) 
while True:
#for k in range(4):
    for ind in range(numberOfMonths):
        
#        print(ind+1, " months:")
    
        ub=calc_unpaid_balance(b0,mfp)
        b=calc_balance(ub, ir)
    
#        print(ub)
#        print(b)
    
        b0=b
#        print("")
    if b0<=0.2 and b0>=-0.2: break
    #bound re-definition
    newbound=(upperbound+lowerbound)/2
    if b0>0.2:
        lowerbound=newbound
    else:
        upperbound=newbound
    b0=balance
    mfp=(lowerbound+upperbound)/2
#    print("upperbound", upperbound)
#    print("lowerbound", lowerbound)
#    print("mfp", mfp)
#    print("")
#    if mfp==450: break

print("Lowest Payment:", round(mfp,2))
