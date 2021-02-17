#!/usr/bin/env python
# coding: utf-8

import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
from random import choice

root = Tk()
root.geometry('3000x1300')
root['background'] = '#293361'

myLabel = Label(root, text="Show or Movie Selector", bg='#293361', fg='white')
myLabel.config(font=("Courier", 32))
myLabel.pack()

def magicConch():
    Hulu = [
        'Dave',
        'Bojack Horseman',
        'Letterkenny',
        'The Undoing',
        'Luther',
        'Friday Night Lights',
        'Westworld',
        ]
    Netflix = [
        'The Midnight Gospel',
        'Narcos',
        'Bloodline',
        'Mindhunter',
        'Blacklist',
        'Wentworth',
        'Shameless',
        'The 100',
        'Hannibal',
        'Peaky Blinders',
        'TURN',
        'New Girl',
        'Occupied',
        ]
    PrimeVideo = [
        'The Boys',
        'Your Honor',
        'Silence of the Lambs (film)',
        'Clarice',
        'Dexter',
        'The Wilds',
        "Schitt's Creek",
        'Bosch',
        'Wayne',
        'Eighth Grade (film)',
        'Animal Kingdom',
        'Fargo',
        'Sneaky Pete',
        'The Americans',
        ]
    DisneyPlus = [
        'Wanda Vision'
    ]
    streaming_services = [
        random.choice(Hulu)+' on Hulu', 
        random.choice(Netflix)+' on Netflix', 
        random.choice(PrimeVideo)+' on Prime Video', 
        random.choice(DisneyPlus)+' on Disney+']
    choice = random.choice(streaming_services)
    myLabel = Label(root, text='You should watch '+str(choice).strip('[]')+'!', bg='#293361', fg='white')
    myLabel.config(font=("Courier", 12))
    myLabel.pack()
    return choice

magicConch = Button(root, text='What should I watch?', bg='#293361', fg='white', bd='5', borderwidth=1, command=magicConch)
magicConch.config(font=("Courier", 12))
magicConch.pack(pady=8)
root.mainloop()