import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
location = 'University of Stellenbosch'

address = location


url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
print (data)

info = json.loads(data.decode())

for item in info['results']:
    print (item['place_id'])
