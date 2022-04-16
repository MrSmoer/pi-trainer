from calendar import c
import curses
from curses import wrapper
from curses.ascii import isdigit
import fileinput
from operator import truediv
import time
import PiFileReader
import KeypadManager
import ScoreBoard
import Display
import ColorManager
import Exceptions

        
def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def initMainWindow():
    window = curses.newwin(curses.LINES-1, curses.COLS-1)
    window.nodelay(False)
    window.refresh()
    return window


def initCursesSettings(stdscr):
    curses.noecho()
    # doesn't need return to get keys
    curses.cbreak()
    # disable cursor
    curses.curs_set(0)
    stdscr.keypad(True)


def main(stdscr):
    pireader=PiFileReader.PiFileReader()
    lines=pireader.readPifileToLines('pi.txt')
    
    rightColor, offColor, wrongColor =  ColorManager.initColors()
    initCursesSettings(stdscr)
    window = initMainWindow()
    keypad = KeypadManager.KeypadManager()
    display = Display.Display(lines)
    scBoard = ScoreBoard.ScoreBoard(10, 30)

    currentDigit=display.getCurrentDigit()
    correctDigits=0
    oldKey=""
    display.show()
    try:
        while True:
            currentDigit=display.getCurrentDigit()
            a = window.getkey()
            
            keypad.setKeyOff(oldKey)
            oldKey=a
            if a.isdigit():
                if a==currentDigit:
                    display.shiftLeft()
                    correctDigits+=1
                    keypad.setKeyRight(a)  
                    scBoard.incrementScore()
                else:
                    print('\a', end="",flush=True)
                    keypad.setKeyWrong(a)
                    scBoard.incrementMistakes()
                
            elif a == 'q':
                break
            
        exit(stdscr)
    except Exceptions.DoneException:
        exit(stdscr)
        print("You typed all digits of Pi that are provided in the Database ...")
        print(" ")

if __name__== '__main__':
    wrapper(main)
  
    

 

        
        

