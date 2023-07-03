#!/usr/bin/python3
"""
requests: module to handle requests
sys: module to get command line argument
"""
import requests, sys

url = sys.argv[1]

r = requests.get(url)
header = r.headers.get('X-Request-Id')

print(header)
