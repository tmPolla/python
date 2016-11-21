#funcction usage
#Week6 - chapter 4 - Polla

def computepay(hour,rate):
   #return (40*rate)+((hour-40)*(rate+(rate/2)))
   if hour>40:
    return (40*rate)+((hour-40)*(rate+(rate/2)))
   else: return (hour*rate)

shour=float(raw_input('Whats the hours?'))
srate=float(raw_input('Whats the rate?'))
print computepay(shour,srate)