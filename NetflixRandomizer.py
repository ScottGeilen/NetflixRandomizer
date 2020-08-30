#!/usr/bin/env python
# coding: utf-8

import requests
import random
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://en.wikipedia.org/wiki/List_of_Netflix_original_programming')
soup = BeautifulSoup(page.text, 'html.parser')

title_list = []
table = soup.find('div', {'id': 'mw-content-text'})
body = table.find_all('tbody')
rows = table.find_all('tr')

for row in rows:
    title_row = row.find_all('td')
    titles = [x.text.strip() for x in title_row]
    title = titles[:1]
    title_list.append(title)
    
choice = random.choice(title_list)
print('You should consider watching ' + str(choice[0]) + '!')