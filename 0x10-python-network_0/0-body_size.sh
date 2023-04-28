#!/bin/bash
# This script takes a URL from command line and uses curl to get the size of the body of the response
curl -s -w "%{size_download}\n" "$1"
