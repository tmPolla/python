#!/bin/python
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# a b c
  # d
# e f g
#we have to find hourglasses like this and sum the component sum(a:g) and find the biggest sum

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

#print "base array", arr
max = -99
k=0
l=0
count=0
for i in range(len(arr[0])-2):
    for j in range(len(arr)-2):
        #print arr[i][j], arr[i][j+1], arr[i][j+2]
        #print arr[i+1][j+1]
        #print arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]
        count=int(arr[i][j])+int(arr[i][j+1])+int(arr[i][j+2])+int(arr[i+1][j+1])+int(arr[i+2][j])+int(arr[i+2][j+1])+int(arr[i+2][j+2])
        if max<count: max=count
    #print "new hourglasses"

print max
