#!/bin/bash

function response_code {
  response=$(curl -so /dev/null -w "%{http_code}\n" ${1})
  echo "Response Code: ${response}"
}
 
response_code $1