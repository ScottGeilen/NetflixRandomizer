#!/usr/bin/env python
# coding: utf-8

import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as Tk

page = requests.get('https://en.wikipedia.org/wiki/List_of_Netflix_original_programming')
soup = BeautifulSoup(page.text, 'html.parser')

print('\nNetflix Movie or Show Suggestions\n')
exit = False
suggestion = 'y'
while exit == False:
    if (suggestion.lower() == 'y'):
        title_list = []
        table = soup.find('div', {'id': 'mw-content-text'})
        #body = table.find_all('tbody')
        rows = table.find_all('tr')

        for row in rows:
            title_row = row.find_all('a')
            titles = [x.text.strip() for x in title_row]
            #title = titles[0]
            title_list.append(titles)
        choice = random.choice(title_list)
        print('SUGGESTION: You should consider watching ' + str(choice[0]) + '!\n')
        print('Need another suggestion? y/n')
        suggestion = input()
    elif (suggestion.lower() == 'n'):
        print('Enjoy your show or movie!')
        exit = True
        break