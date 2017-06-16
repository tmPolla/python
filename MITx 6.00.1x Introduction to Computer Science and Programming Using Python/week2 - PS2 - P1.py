# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:17:20 2017

@author: MarosiPA
week 2 Problem set 2 - Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the 
credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""


#balance => b
#minimum payment => p
#unpaid balance => ub
#interest => i
#annual interest rate => air
#minimum montly payment rate => mpr

stop_month=12

# Test Case 1:
#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04


#Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
          
air=annualInterestRate
mpr=monthlyPaymentRate


b0=balance

def calc_payment(b):
    p=b*mpr
    return p

def calc_unpaidbalance(p,b):
    ub=b-p
    return ub

def calc_interest(ub):
    i=(air/12)*ub
    return i

def calc_balance(ub,i):
    b=ub+i
    return b


for ind in range(stop_month):
    p=calc_payment(b0)
    ub=calc_unpaidbalance(p,b0)
    i=calc_interest(ub)
    b=calc_balance(ub,i)
    
    
#    print("Month ",ind+1," Remaining balance:", round(b,2))
    b0=b

#print("")
print("Remaining balance:", round(b,2))
    
#p=calc_payment(b0)
#ub=calc_unpaidbalance(p,b0)
#i=calc_interest(ub)
#b=calc_balance(ub,i)
#
#print (p)
#print (ub)
#print(i)
#print (b)