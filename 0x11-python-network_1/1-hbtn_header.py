#!/usr/bin/python3
"""
urllib and sys module
"""
import urllib.request
from sys import argv

url = argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

print(header)
