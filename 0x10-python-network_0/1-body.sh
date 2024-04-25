#!/bin/bash
# script takes URL, sends GET request and displays the body of a 200 status code response
curl -s -X GET -L "$1" -o /dev/null -w "%{http_code}" | grep -q 200 && curl -s "$1"
