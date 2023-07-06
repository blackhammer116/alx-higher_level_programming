#!/usr/bin/python3
"""
requests: module to handle url requests
sys: module to get command line argument
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    params = {'per-page': 8}
    response = requests.get(url, params=params)
    response_json = response.json()
    for commit in response_json:
        sha = commit['sha']
        name = commit['commit']['author']['name']
        print(f'{sha}: {name}')
