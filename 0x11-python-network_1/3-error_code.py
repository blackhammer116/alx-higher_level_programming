#!/usr/bin/python3
"""
urllib.request: module to send request to a url
urllib.error.HTTPError: module to get exception
argv: module to get command line argument
"""
import urllib.request, urllib.error.HTTPError
from sys import argv

try:
    url = argv[1]

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    print(body)
except urllib.error.HTTPError as error:
    print(f"Error: {error.code}")
