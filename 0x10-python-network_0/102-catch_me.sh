#!/bin/bash
# script makes request to 0.0.0.0:5000/catch_me and causes server to respond with "You got me!"
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
