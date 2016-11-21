#ex5-2
#print ('Now I will ask numbers and I will show the biggest and the smalles. If the list is over type Done')

largest = -1
smallest = None

while True:   
    s = raw_input("Enter a number: ")
    try:
        num = int(s)
        
        #check largest and smallest
        if largest < num: largest = num
        
        if smallest is None: smallest = num 
        elif smallest > num: smallest = num
        
        #print "Largest: " + largest
        #print "Smallest: " + smallest
        #print "N: " + n
    except:
        print("Invalid input")
        if s == "done": break
        else: continue


print "Maximum is", largest
print "Minimum is", smallest
