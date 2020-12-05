"""Computies"""
from os import system as sys
from os import name
from time import sleep as delay
from src.bootup import bootup_words as bootup

sys("cls"), sys("title Computies") if name == "nt" else sys("clear"), sys("title Computies")

for word in bootup: print(word); delay(0.3)
