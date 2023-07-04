#!/bin/bash
#sending a get request to a url
curl -s -w "\n%{http_code}" $1 | awk 'END{if($0==200)exit;print $0}'
