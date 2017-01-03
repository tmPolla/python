#Coursera - Regular expression
import re
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y= re.findall('@(\S+)',x)
print '1 exp: ',y
print ''

y= re.findall('[0-9]+',x)
print '2 exp: ',y
print ''

y= re.findall('[0-9]',x)
print '3 exp: ',y
print ''

y= re.findall('\S+?@\S+',x)
print '4 exp: ',y
print ''

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y