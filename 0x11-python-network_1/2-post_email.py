#!/usr/bin/python3
"""
urllib.request: module to get response of a url
urllib.parse: module to parse the content
argv: module to get command line argument
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv = argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)
