#!/bin/bash
# script takes URL, sends GET request and displays the body of a 200 status code response
curl -Ls "$1"
