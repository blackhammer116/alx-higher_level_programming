#!/bin/bash
# This script takes a URL from command line and uses curl to get the size of the body of the response
curl -s "$1" -w "%{size_download}\n" | tail -n 1
