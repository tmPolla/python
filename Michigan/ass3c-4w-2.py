
import urllib
from BeautifulSoup import *

urlSample = "http://python-data.dr-chuck.net/known_by_Fikret.html"
htmlSample = urllib.urlopen(urlSample).read()
soupSample = BeautifulSoup(htmlSample)

urlActual = "http://python-data.dr-chuck.net/known_by_Alvin.html "
htmlActual = urllib.urlopen(urlActual).read()
soupActual = BeautifulSoup(htmlActual)

# wokringType='Sample'
wokringType='Actual'

#Sample input
if wokringType=='Sample':
    count=4
    position=3
elif wokringType=='Actual':
    count=7
    position=18



# Retrieve all of the anchor tags
if wokringType=='Sample': tags = soupSample('a')
elif wokringType=='Actual': tags = soupActual('a')

if wokringType=='Sample': print 'Enter URL: ', urlSample
elif wokringType=='Actual': print 'Enter URL: ', urlActual

print 'Enter count: ',count
print 'Enter position: ',position

countS=1
while countS<count+1:
    positionS=1
    while positionS<position+1:
        for tag in tags:
            if positionS==position: 
                print 'Retrieving: ', tag.get('href', None)
                url = tag.get('href', None)
                html = urllib.urlopen(url).read()
                soup = BeautifulSoup(html)
                tags = soup('a')
            if positionS==position and countS==count : print 'Result:', tag.contents[0]
            positionS=positionS+1
    countS=countS+1
    
