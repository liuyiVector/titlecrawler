#!/bin/sh
# kill -9 $(ps -ef|grep chromedriver|gawk '$0 !~/grep/ {print $2}' |tr -s '\n' ' ')
index=`sed -n 1p now.txt`
echo ${index}
while [ ${index} -lt 480 ]; do
  python -u titleFetcher.py >> ./tmps.txt
done
