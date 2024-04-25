#!/bin/bash
# script sends GET request to URL with a specific header and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
