#codingame Temperatures

n = int(raw_input())  # the number of temperatures to analyse
smallestpos = None
smallestneg = None
result=0
zero=False

if (n==0):
    result=0
    print result
    exit()

for i in range(1,n+1): 
    temps = int(raw_input()) # the n temperatures expressed as integers ranging from -273 to 5526

    diff = abs(0-temps)
    # print "Difference: ",diff

    if temps==0: zero=True
    if temps<0:
        if smallestneg is None: smallestneg = diff 
        elif smallestneg > diff: smallestneg=diff
    
    # print "smallestpos old: ",smallestpos
    # print "smallestneg old: ",smallestneg
    
    if temps>0:
        if smallestpos is None: smallestpos = diff
        elif smallestpos > diff: smallestpos=diff
    


        
# print "smallestpos: ",smallestpos
# print "smallestneg: ",smallestneg



if (zero==True): 
        result=0
        print result
        exit()

if smallestpos==smallestpos: result=smallestneg*-1
if smallestpos<smallestneg: 
    result=smallestpos
else: result=smallestneg*-1

print result