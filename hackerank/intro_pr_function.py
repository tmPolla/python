#Introduction Print function
# input N pl 5
#output 123...N pl 12345
N=range(int(raw_input()))
s=''
for i in N: s=s+str(i+1)
print s
