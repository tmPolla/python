# Coursera Assignments32 3 cours and week 3
# Read the numbers from the text and sum them
# use the http://python-data.dr-chuck.net/regex_sum_42.txt to the test
# use http://python-data.dr-chuck.net/regex_sum_335225.txt as actual data

import re

file = raw_input('Give me the file: ')
if len(file)==0: file='regex_sum_335225.txt'
handle = open(file)
sum=0

for line in handle:
    numberlist = re.findall('[0-9]+',line)
    if len(numberlist)<>0:
        for i in range(0,len(numberlist)):
            sum=sum + int(numberlist[i])

print sum