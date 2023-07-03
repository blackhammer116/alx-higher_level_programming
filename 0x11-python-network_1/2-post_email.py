#!/usr/bin/python3
"""
urllib and sys modules
"""
import urllib.request, urllib.parse
from sys import argv

url = argv[1]
email = argv = argv[2]

data = urllib.parse.urllencode({'email':email}).encode('utf-8')
req = urllibe.request.Request(url, data=data, method='POST')

with urllibe.request.urlopen(req) as response:
    body = response.read().decode('utf-8')

print(body)
