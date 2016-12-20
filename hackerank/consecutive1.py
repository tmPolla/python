# convert to binary
#slice the bin part from the result
# count how many consecutive 1 follow each other
# example 101 = 1; 1101=2; 100111011 = 3

#!/bin/python

import sys

n = int(raw_input().strip())
result= bin(n)
count=0
max=0
#print result
#print result[2:]
for i in result[2:]:
    #print "i", i
    if i=="1": count=count+1
    if i=="0":
        if max<count: max=count
        count=0
if max<count: max=count        
print max
    