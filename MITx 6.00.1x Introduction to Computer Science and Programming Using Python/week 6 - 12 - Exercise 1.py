# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:05:15 2017

@author: Polla
12. Searching and Sorting Algorithms   Exercise 1
"""

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

print(a[0])

print(a[a[1]])

print(b[b[2]])

print(a[c[a[b[3]]]])


num = 1
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

print(val)


val=0
num = 0
while val!=3:
    L = [2, 0, 1, 5, 3, 4]
    val = 0
    for i in range(0, num):
        val = L[L[val]]
    num+=1
print("Good num is: ", num)
print(val)



