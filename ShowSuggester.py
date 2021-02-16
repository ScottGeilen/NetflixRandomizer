#!/usr/bin/env python
# coding: utf-8

import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
from random import choice

root = Tk()
root.geometry('500x300')

myLabel = Label(root, text="Show Suggester")
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
    myLabel = Label(root, text='You should watch '+str(choice).strip('[]')+'!')
    myLabel.pack()
    return choice

magicConch = Button(root, text='What should I watch?', bd='5', command=magicConch)
magicConch.pack()
root.mainloop()