#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter and
displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
