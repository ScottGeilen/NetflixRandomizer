#!/usr/bin/env python
# coding: utf-8

import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *

root = Tk()
root.geometry('500x150')

myLabel = Label(root, text="Netflix Show Suggester")
myLabel.pack()
    
def suggestTitle():
    page = requests.get('https://en.wikipedia.org/wiki/List_of_Netflix_original_programming')
    soup = BeautifulSoup(page.text, 'html.parser')
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
    myLabel = Label(root, text='You should consider watching ' + str(choice[0]) + '!')
    myLabel.pack()
btn = Button(root, text='What should I watch?', bd='5', command=suggestTitle)
btn.pack()
root.mainloop()