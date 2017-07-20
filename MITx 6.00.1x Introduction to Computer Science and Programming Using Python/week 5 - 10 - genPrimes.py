# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:33:10 2017

@author: MarosiPA

Write a generator, genPrimes, that returns the sequence of prime numbers on 
successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""

#def genPrimes(n):
#    yield 2
#    i=1
#    while i<=n-2:
#        i+=2
#        if i//2==1:
#            yield i
#        else:
#            break
        

def isprime(n):
    for i in range(2 ,int((n**0.5))+1):
        if n % i == 0:
            return False
    return True

def genPrimes():
    yield 2
    i = 1
    while True:
        i += 2
        if isprime(i):
            yield i