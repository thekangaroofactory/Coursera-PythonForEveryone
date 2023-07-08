
# The program will prompt for a location,
# contact a web service and retrieve JSON for the web service
# and parse that data,
# and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

address = input('Location: ')

serviceurl = "https://py4e-data.dr-chuck.net/json?"


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
parms['key'] = 42
parms['address'] = address

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

# print(json.dumps(js, indent=4))

print('Place id', js['results'][0]['place_id'])
