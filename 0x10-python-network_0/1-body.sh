#!/bin/bash
#sending a get request to a url
url=$1
response=$(curl -s -w "%{http_code}" $url)

status_code=${response: -3}
body=${response::-3}

if [ $status_code -eq 200 ]; then
    echo $body
fi
