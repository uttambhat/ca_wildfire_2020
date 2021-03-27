#!/bin/bash

rm temp1.txt
url="https://en.wikipedia.org/w/index.php?title=2018_California_wildfires&offset=20180814190532%7C854926929&limit=500&action=history"

curl $url | grep -i "26 July 2018\|27 July 2018\|28 July 2018\|29 July 2018\|30 July 2018\|31 July 2018\|August 2018" > temp1.txt

url="https://en.wikipedia.org/w/index.php?title=2018_California_wildfires&dir=prev&offset=20180814190330%7C854926716&limit=500&action=history"

curl $url | grep -i "August 2018" >> temp1.txt

cat temp1.txt | grep -o -P 'oldid=.{0,9}' > temp2.txt
sort temp2.txt | uniq > temp3.txt
sed -e 's/^/https:\/\/en.wikipedia.org\/w\/index.php\?title=2018_California_wildfires\&/' temp3.txt > urls_2018.txt

county="Mendocino_county"
while read line; do
curl $line | grep -i "revision as of" | grep -o -P 'Revision as of.{0,25}' >> ${county}_raw_2018.txt
curl $line | grep -A 5 -i "mendocino complex" | grep -o -P 'table-no.{0,10}' >> ${county}_raw_2018.txt
curl $line | grep -A 5 -i "mendocino complex" | grep -o -P -i '.{0,8}contained' >> ${county}_raw_2018.txt
curl $line | grep -A 5 -i "mendocino complex" | grep -o -P -i 'July.{0,5}\|August.{0,5}' | tail -n1 >> ${county}_raw_2018.txt
done < urls_2018.txt

county="Mendocino_county"
url="https://en.wikipedia.org/w/index.php?title=2018_California_wildfires&oldid=852435822"
url="https://en.wikipedia.org/w/index.php?title=2018_California_wildfires&oldid=854767931"
curl $url | grep -i "revision as of" | grep -o -P -i 'revision as of.{0,20}

