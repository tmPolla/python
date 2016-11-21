#ex3-1
hours=float(raw_input("Enter hours: "))
rate=float(raw_input("Enter rate per hour: "))

#calculate gross pay
if hours>40:
    grossPay=(40)*rate*1.0+(hours-40)*rate*1.5
else:
    grossPay=hours*rate*1.1
print grossPay