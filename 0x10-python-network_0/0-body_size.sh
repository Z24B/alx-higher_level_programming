#!/bin/bash
# script takes URL, sends request and displays size in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
