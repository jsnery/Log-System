from os import system
from sys import platform
from tools.logFile import * 


def clear():
    if platform.startswith('linux') or platform.startswith('darwin'):
        return system('clear')
    return system('cls')

