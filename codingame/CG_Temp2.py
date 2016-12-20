#codingame Temperatures

n = int(raw_input())  # the number of temperatures to analyse
temps=raw_input() # this is a string!!!!
smallestpos = None
smallestneg = None
result=0
zero=False

# print temps
temps = temps.split()
# print temps

if (n==0):
    result=0
    print "Result: ",result
    exit()

for i in range(0,n): 
    temps2 = int(temps[i])

    diff = abs(0-temps2)
    # print "Difference: ",diff
    # print temps2
    
    if temps2==0: zero=True
    if temps2<0:
        # print "kisebb mint 0"
        # print "smallestneg: ",smallestneg
        if smallestneg is None: smallestneg = diff 
        elif smallestneg > diff: smallestneg=diff
    
    # print "smallestpos old: ",smallestpos
    # print "smallestneg old: ",smallestneg
    
    if temps2>0:
        if smallestpos is None: smallestpos = diff
        elif smallestpos > diff: smallestpos=diff
    


        
print "smallestpos: ",smallestpos
print "smallestneg: ",smallestneg



if (zero==True): 
        result=0
        print result
        exit()

if smallestneg is None:
    print smallestpos
    exit()
 
if smallestpos is None:
    print smallestneg*-1
    exit()

    
if smallestpos==smallestneg: 
    print smallestpos
    exit()

if smallestpos<smallestneg: 
    result=smallestpos
else: result=smallestneg*-1

print result