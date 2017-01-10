import urllib
import xml.etree.ElementTree as ET

serviceurlS = 'http://python-data.dr-chuck.net/comments_42.xml'
serviceurlA = 'http://python-data.dr-chuck.net/comments_335227.xml'

url = serviceurlA
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

lst = tree.findall('.//count')
print 'Count:', len(lst)


lst = tree.findall('.//comment')
sumcount=0
for item in lst:
    sumcount = sumcount + int(item.find('count').text)
    
print 'Sum:', sumcount