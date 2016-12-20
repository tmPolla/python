import urllib
from BeautifulSoup import *

urlS = "http://python-data.dr-chuck.net/comments_42.html"
htmlS = urllib.urlopen(urlS).read()

urlA = "http://python-data.dr-chuck.net/comments_335230.html"
htmlA = urllib.urlopen(urlA).read()

soup = BeautifulSoup(htmlA)

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
    print
    
for tag in tags:
    sum = sum+ int(tag.contents[0])
print 'Final sum: ',sum