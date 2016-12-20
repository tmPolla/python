#Assignment 6.5
text = "X-DSPAM-Confidence:    0.8475";

#solution 1
pos=text.find('0')
#print pos
result = text[pos:]
print float(result)

#solution 2
pos2 = text.find(':')
result2 = float(text[pos2+1:])
print result2

