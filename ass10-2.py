#Michigan Assignment 10-2
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

result=dict()

for line in handle:
    if line.startswith('From')==True:
        word=line.split()
        try:
            pattern = word[5].split(':')
            key=pattern[0]
            # print key
            result[key]=result.get(key,0)+1
            # print result
        except:
            continue


for k,v in sorted(result.items()):
    print k,v