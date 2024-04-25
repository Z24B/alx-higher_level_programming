#!/bin/bash
# script sends a JSON POST request to a URL with the contents of a file as the body
if [ -f "$2" ]; then
	curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
	echo ""
else
	echo "File not found or invalid."
fi
