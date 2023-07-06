#!/usr/bin/python3
"""
requests: module to handle url requests
sys: module to get command line argument
"""
import requests
import sys

if __name__ == "__main__":
    try:
        url = "http://0.0.0.0:5000/search_user"
        letter = sys.argv[1] if len(sys.argv) > 1 else ""
        data = {'q': letter}

        response = requests.post(url, data=data)

        response_json = response.json()
        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
