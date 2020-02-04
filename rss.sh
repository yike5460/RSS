#/bin/bash

python3 rss-aws.py
grep -i "Now Available in AWS China" news.txt | awk -F '>' '{print $3}' | cut -f1 -d"<" > result.txt
git diff result.txt result-01.txt

