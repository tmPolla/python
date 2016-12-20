#!/bin/python
# from Hackerrank
#print element from array in the revesre order
#print without brakets
# input 1 4 3 2
# with only print the output should be [2, 3, 4, 1]
# good output 2 3 4 1

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

j=len(arr)
list=[]
for i in range(1, len(arr)+1):
    #print 'index:', j-i
    list.append(arr[j-i])

print ' '.join(map(str, list))