#!/bin/bash

url="https://en.wikipedia.org/w/index.php?title=2020_California_wildfires&offset=&limit=500&action=history"
curl $url | grep -i "16 August 2020\|17 August 2020\|18 August 2020\|19 August 2020\|20 August 2020\|21 August 2020\|22 August 2020\|23 August 2020\|24 August 2020\|25 August 2020\|26 August 2020\|27 August 2020\|28 August 2020" > temp1.txt

cat temp1.txt | grep -o -P 'oldid=.{0,9}' > temp2.txt
sort temp2.txt | uniq > temp3.txt
sed -e 's/^/https:\/\/en.wikipedia.org\/w\/index.php\?title=2020_California_wildfires\&/' temp3.txt > urls.txt

county="Santa_Cruz_County"
county="Stanislaus_County"
county="Yolo_County"
county="Mendocino_County"
while read line; do
curl $line | grep -i "revision as of" | grep -o -P 'Revision as of.{0,25}' >> ${county}_raw_3.txt
curl $line | grep -A 3 -i $county | head -n4 | grep -o -P 'table-no.{0,10}' >> ${county}_raw_3.txt
curl $line | grep -A 3 -i $county | head -n4 | grep -o -P -i '.{0,8}contained' >> ${county}_raw_2.txt
curl $line | grep -A 3 -i $county | head -n4 | grep -o -P -i 'August.{0,5}' | tail -n1 >> ${county}_raw_2.txt
done < urls.txt

