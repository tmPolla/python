# michigan week 5 9.4

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
line = text.split()

counts = dict()

prev=False

for word in line:
    if prev==True: 
        counts[word]= counts.get(word,0)+1
        
    if word =='From': 
        prev=True
    else: prev=False
    
maxivalue=0
maxikey=''  
for aa,bb in counts.items():
    if maxivalue<bb: 
        maxivalue=bb
        maxikey=aa

print maxikey,maxivalue 