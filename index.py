#!/usr/bin/env python
# coding: utf-8
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://reelgood.com/source/netflix')
soup = BeautifulSoup(page.text, 'html.parser')

title_list = []
body = soup.find('tbody')
rows = body.find_all('tr')

for row in rows:
    titles = row.find_all('a')
    titles = [x.text.strip() for x in titles]
    title_list.append(titles[1])
    #print(title_list)
print('You should consider watching ' + random.choice(title_list) + '!')