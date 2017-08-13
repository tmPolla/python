# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:59:48 2017

@author: Polla
"""
import numpy as np

r= np.arange(36)
r.resize((6,6))
print("the whole matrix")
print(r)
print("")

print("one element of the matrix")
print(r[2,2])
print("")

print("first row")
print(r[::7])
print("")

print("last column")
print(r[0:6,::-7])
print("")

print("first column")
print(r[:,::7])
print("")

print("diagonal elements")
print(r.reshape(36)[::7])
print("")

print(r[2::2,2::2])
print(r[2:4,2:4])


old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old
new[0, :2] = 0
print("question 1")
print(old)
print("")

old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old.copy()
new[:, 0] = 0
print("question 2")
print(old)