#!/usr/bin/python3
"""
requests: module to handle request
sys: to geet command line argument
"""
import requests, sys

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
response = requests.post(url, data=data)
body = response.text

print(body)
