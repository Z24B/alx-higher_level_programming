#!/bin/bash
# script sends a JSON POST request to a URL with the contents of a file as body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
