#!/usr/bin/python3
"""
urllib.request: module to handle request
"""
import urllib.request
""" 
sys.argv: module to get command  line argument
"""
from sys import argv

url = argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

print(header)
