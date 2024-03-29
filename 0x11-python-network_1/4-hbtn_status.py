#!/usr/bin/python3
"""
requests: module to request a page from a url
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    request = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(request.text)}")
    print(f"\t- content: {request.text}")
