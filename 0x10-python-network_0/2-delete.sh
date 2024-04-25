#!/bin/bash
# script sends DELETE request to URL passed as argument and displays the body of the response
curl -s -X DELETE "$1"
