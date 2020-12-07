"""Computies"""
from os import system as sys
from os import name
from time import sleep as delay
from src.bootup import bootup_words
from src.bootup import waiting
import src.pathway as pathway

goodbye = "Goodluck and Goodbye :)"

def clear_screen():
    '''clear screen'''
    if name == "nt":
        sys("cls")
    else:
        sys("clear")

def namebootup(time=4):
    '''Name loading'''
    bootup = list(bootup_words * time)[:-1]
    print("\t\t\x1b[5;30;47m" + bootup[0] + "\x1b[0m")
    delay(0.5)

def subjectlist():
    '''subject printout'''
    for subject in pathway.subject_list:
        print(subject)
        delay(0.5)

def request_input():
    """input subject"""
    try:
        global subject
        subject = int(input("SELECT YOUR SUBJECT ID : "))
    except ValueError:
        clear_screen()
        print("INVALID INPUT")
        delay(1)
        mainscreen()
    except KeyboardInterrupt:
        subject = 0
        clear_screen()

def mainscreen():
    '''main screen'''
    clear_screen()
    namebootup()
    subjectlist()
    request_input()

mainscreen()

if subject:
    clear_screen()
    namebootup(1)
    for content in pathway.subjects[subject]:
        print(' - '+content)
        delay(0.5)
else:
    clear_screen()
    print(goodbye)