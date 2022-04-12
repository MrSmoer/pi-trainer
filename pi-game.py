#! /usr/bin/python3

import sys
from time import sleep
from consoledraw import Console
from datetime import datetime
from pynput import keyboard
import curses
format = """
    ╔══════════╗
    ║ {} ║
    ╚══════════╝
"""

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        with console:
            console.print(format.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
 
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

if __name__ == '__main__':
 
    #startDigit=input("From which digit do you want to start?:\n")
    #print("start digit is: " + startDigit)
    console = Console()
    s = 'testfas'
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    print("Quitting")
        
        

