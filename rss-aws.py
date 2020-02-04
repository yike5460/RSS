
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import codecs
 
url = 'https://www.amazonaws.cn/en/new/?nc1=h_ls'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'}
page = requests.get(url, headers=headers)
page.encoding = 'utf-8'
page_content = page.text
f = codecs.open('/Users/kyiamzn/00_tmp/news-01.txt', 'w', 'utf-8')
f.write(page_content)
f.close()
