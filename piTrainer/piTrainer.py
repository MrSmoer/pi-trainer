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
import StandardMode
import learnMode
import simonSays

        
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
   
    rightColor, offColor, wrongColor =  ColorManager.initColors()
    initCursesSettings(stdscr)
    window = initMainWindow()
    modes={
        1:(StandardMode.Standard(),"Standard"),
        2:(learnMode.learnMode(),"Number Learning"),
        3:(simonSays.simonSays(),"Simon Says")
    }
    yCordOfOpt=10
    window.addstr(yCordOfOpt,3,"Select Your Mode")
    for key in modes:
        text= str(key)+') '+modes.get(key)[1]
        yCordOfOpt +=1
        window.addstr(yCordOfOpt,3,text)
    

    a = window.getkey()
    #print(a)q1
    game=modes.get(int(a))[0]
    window.erase()
    window.refresh()
    game.start(window)
    exit(stdscr)
    

if __name__== '__main__':
    wrapper(main)
  
    

 

        
        

