import json
import urllib

urlS="http://python-data.dr-chuck.net/comments_42.json"
urlA="http://python-data.dr-chuck.net/comments_335231.json"

running_mode="A"

if running_mode =="S": print "Enter location: ",urlS
else: print "Enter location: ",urlA

if running_mode =="S": url = urlS
else: url = urlA

uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieving', url
print 'Retrieved',len(data),'characters'

#print data

info = json.loads(data)

print 'User count:', len(info["comments"])

sumelement=0
for item in info["comments"]:
    sumelement = sumelement + item['count']
    
print "Sum: ", sumelement
# print data
# print info

