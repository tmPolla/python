# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:59:18 2017

@author: MarosiPA
"""


#4
print("task 4")
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

#3
print("task 3")
num = 10
while num > 3:
    num -= 1
    print(num)


#1
print("task 1")
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 


print("done")


#task while 1
print("task while 1")
x=2
while x<=10:
    print (x)
    x=x+2
print("Goodbye!")


#task while 2
print("task while 2")
print("Hello")
x=10
while x>=2:
    print (x)
    x=x-2
    
    
#task while 3
print("task while 3")
input=6
start=1
end=input
counter=0
while start<=end:
    counter=counter+start
    start=start+1
print (counter)
    

#task loops 1
print("task loops 1")
for i in range(2,12,2):
    print (i)
print("Goodbye!")


#task loops 2
print("task loops 2")
print("Hello!")
for i in range(10,0,-2):
    print (i)

#task loops 3
print("task loops 3")
input=6
start=1
end=input
counter=0
for i in range(start,end+1,1):
    counter=counter+i
print (counter)


#exercise 5 - 1 
print("exercise 5 - 1 ")
num = 10
for num in range(5):
    print(num)
print(num)

#exercise 5 - 2 
print("exercise 5 - 2 ")
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
    
#exercise 5 - 3 
print("exercise 5 - 3 ")   
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')     

#exercise 5 - 4 
print("exercise 5 - 4 ")     
for letter in 'hola':
    print(letter) 



#exercise 5 - 5 
print("exercise 5 - 5 ")   
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)



#exercise 6 - 1 
print("exercise 5 - 5 ") 
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')

    