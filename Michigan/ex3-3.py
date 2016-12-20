#ex3-3
#input the number and throw an error if it is not float
try:
    grade=float(raw_input("Please type a grade from 0.0-1.0: "))
except:
    print("This is not a number")
    quit()

#check the range
if grade<=0.0 or grade >= 1.0:
    print("This is not in the range")
    quit()

#Score Grade table
if grade>=0.9:
    print("A")
elif grade>=0.8:
    print("B")
elif grade>=0.7:
    print("C")
elif grade>=0.6:
    print("D")
else: print("F")    