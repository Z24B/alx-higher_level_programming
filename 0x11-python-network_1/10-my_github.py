#!/usr/bin/python3
"""
Uses the GitHub API to display id using Basic Authentication
with a personal access token.
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print(None)
