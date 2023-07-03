#!/usr/bin/python3
"""
requests: module to handle url requests
sys: module to get command line argument
"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)
if responses.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
