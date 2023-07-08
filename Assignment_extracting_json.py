
# The program will prompt for a URL,
# read the XML data from that URL using urllib and
# then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.

# http://py4e-data.dr-chuck.net/comments_42.xml


import urllib.request, urllib.parse, urllib.error
import json
import ssl


# input
url = input('URL: ')
if len(url) == 0:
    url = "http://py4e-data.dr-chuck.net/comments_1822034.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get the data
con = urllib.request.urlopen(url, context=ctx)
data = con.read()
info = json.loads(data)

items = info['comments']

# count
total = 0
for item in items:
    print('Name', item['name'])
    print('count', item['count'])
    total += item['count']

print(total)
