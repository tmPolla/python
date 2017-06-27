# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:39:16 2017

@author: MarosiPA
"""

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']


print("T1")
print(listA.sort)

print("T2")
listA.sort()
print(listA)

print("T3")
print(listA)

print("T4")
listA.insert(0, 100)
print(listA)

print("T5")
listA.remove(3)
print(listA)

print("T6")
listA.append(7)

print("T7")
print(listA)

print("T8")
print(listA + listB)

print("T9")
listB.sort()

print(listB.pop())

print("T10")
print(listB.count('a'))

#print("T11")
#listB.remove('a')
#print(listB)

print("T12")
listA.extend([4, 1, 6, 3, 4])
print(listA)

print("T13")
listA.count(4)

print("T14")
print(listA.index(1))

print("T15")
listA.pop(4)


print("T16")
listA.reverse()

print("T17")
print(listA)