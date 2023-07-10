#!/bin/bash
# getting json response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
