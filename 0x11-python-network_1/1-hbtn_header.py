#!/usr/bin/python3
"""Python script that takes URL, sends request to URL and displays value of X-Request-Id variable found in header of response"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
