import json
import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_42.json'
actual = 'http://python-data.dr-chuck.net/comments_199724.json'
url = actual
print ('Retrieving', url)
data = urllib.request.urlopen(url)
    
data2=data.read().decode()

print (type(data2))

info = json.loads(data2)
print ('User count:', len(info))

total = 0
for item in info['comments']:
    total += item['count']
print (total)
