#Assignment 7.1
# Use words.txt as the file name
fname = raw_input("Enter file name: ")

#ez egy trukk hogy ne kelljen mindig begepelni a kodot
if len(fname) == 0:
    fname='mbox-short.txt'
    
try:
    fh = open(fname)
except:
    print('Wrong file name!'),fname
    exit()

for line in fh:
    #line2 = line.upper()
    #print line2.rstrip()
    line = line.rstrip().upper()
    print line


