# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:22:36 2017

@author: MarosiPA
Week 4: Good Programming Practices   8. Exceptions and Assertions   Exercise 2

"""


#Task 1
print("Task1")
def fancy_divide1(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

print("fancy_divide1([0, 2, 4], 1)")
fancy_divide1([0, 2, 4], 1)
print("")
print("fancy_divide1([0, 2, 4], 4)")
fancy_divide1([0, 2, 4], 4)
print("")
print("fancy_divide1([0, 2, 4], 0)")
fancy_divide1([0, 2, 4], 0)

print("")

#Task 2
print("Task2")
def fancy_divide2(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

print("fancy_divide2([0, 2, 4], 1)")
fancy_divide1([0, 2, 4], 1)
print("")
print("fancy_divide2([0, 2, 4], 4)")
fancy_divide1([0, 2, 4], 4)
print("")
print("fancy_divide2([0, 2, 4], 0)")
fancy_divide1([0, 2, 4], 0)
        
print("")

##Task 3     
print("Task3")   
def fancy_divide3(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide3(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
        
print("fancy_divide3([0, 2, 4], 1)")
fancy_divide3([0, 2, 4], 1)
print("")
print("fancy_divide3([0, 2, 4], 4)")
fancy_divide3([0, 2, 4], 4)
print("")
print("fancy_divide3([0, 2, 4], 0)")
fancy_divide3([0, 2, 4], 0)

print("")

#Task 4
def fancy_divide4(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
fancy_divide4([0, 2, 4], 0)

print("")

#Task 5
def fancy_divide5(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        
fancy_divide5([0, 2, 4], 0)