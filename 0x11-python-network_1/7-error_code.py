#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If HTTP status code is greater than or equal to 400, print error message.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
