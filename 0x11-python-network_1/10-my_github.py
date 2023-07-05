#!/usr/bin/python3
"""
requests: module to handle requests
sys: module to get command line argument
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        response_json = response.json()
        print(response_json.get('id'))
    else:
        print("None")
