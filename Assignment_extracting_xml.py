
# The program will prompt for a URL,
# read the XML data from that URL using urllib and
# then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.

# http://py4e-data.dr-chuck.net/comments_42.xml


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# input
url = input('URL: ')
if len(url) == 0:
    url = "http://py4e-data.dr-chuck.net/comments_1822033.xml"

# get the data
con = urllib.request.urlopen(url, context=ctx)
data = con.read()
tree = ET.fromstring(data)

# extract
counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)

print(total)

