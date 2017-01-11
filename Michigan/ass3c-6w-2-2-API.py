import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

addressS="South Federal University"
addressA="Cranfield University"

running_mode="A"

if running_mode =="S":  address=addressS
else: address=addressA

print "Enter location: ", address
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data

#print json.dumps(js, indent=4)


print "Place ID: ", js["results"][0]["place_id"]

# Actual data to copy result
# Retrieved 2207 characters
# Place ID:  ChIJ6Uyjok2sd0gRProggkZQM_4