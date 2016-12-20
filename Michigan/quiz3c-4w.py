import re

text='<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
result1 = re.findall('href="(.+)"',text)
print 'result1', result1

result2 = re.findall('href=".+"',text)
print 'result2', result2

result3 = re.findall('http://.*',text)
print 'result3', result3


result4 = re.findall('<.*>',text)
print 'result4', result4

result5 = re.findall('href.*',text)
print 'result5', result5
