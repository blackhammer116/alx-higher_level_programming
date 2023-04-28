#!/usr/bin/bash
# This script takes a URL from command line and
# uses curl to get the size of the body of the response
if [ $# -eq 0 ]; then
	echo "no argument found"
fi
response=$(curl -s -w "%{size_download}" "$1")
size=$(echo "$response" | tail -n 1)
echo "$size"
