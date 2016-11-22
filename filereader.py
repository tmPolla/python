#file reading
#python 2 - week 3 - chapter 7 - files
handle = open('text.txt')

for line in handle:
    print line

print
print

handle = open('text.txt') #ujra meg kell nyitni kulonben ures lesz
inp = handle.read()
print len(inp)
print inp[:4]