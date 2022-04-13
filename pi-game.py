import curses
from curses import wrapper
from curses.ascii import isdigit
import time

lines = []

keys='''╔═══╦═══╦═══╗
║ 7 ║ 8 ║ 9 ║
╠═══╬═══╬═══╣
║ 4 ║ 5 ║ 6 ║
╠═══╬═══╬═══╣
║ 1 ║ 2 ║ 3 ║
╠═══╩═══╬═══╝
║  0    ║
╚═══════╝'''
keyCords=[(7,3),(5,2),(5,6),(5,10),(3,2),(3,6),(3,10),(1,2),(1,6),(1,10)]
def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()



def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def changeColorOfKey(keypad,char,color):
    if char != '':
        keypad.addch(keyCords[int(char)][0],keyCords[int(char)][1],char,color)
        keypad.refresh()


def main(stdscr):

    if curses.has_colors:
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(0, -1, -1)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        rightColor=curses.color_pair(1)
        offColor=curses.color_pair(0)
        wrongColor=curses.color_pair(2)
    else:
        rightColor=curses.A_STANDOUT
        offColor=curses.A_NORMAL
        wrongColor=curses.A_BLINK

    pifile = open('pi.txt')
    
    while True:
        # Get next line from file
        line = pifile.readline()
    # if line is empty
    # end of file is reached
        if not line:
            break
        if has_numbers(line) and "-" not in line and " " in line:
            cleanedLine = ''
            for c in line:
                if c != ' ' and c.isdigit():
                    cleanedLine = cleanedLine+c
            #print("Line{}: {}".format(count, line.strip()))
            lines.append(cleanedLine)
    pifile.close()

    # stops displaying keystrokes
    curses.noecho()
    # doesn't need return to get keys
    curses.cbreak()
    # disable cursor
    curses.curs_set(0)
    stdscr.keypad(True)
    window = curses.newwin(curses.LINES-1, curses.COLS-1)
    window.nodelay(False)
    window.addstr(1, 5, lines[0])
    window.refresh()
    correctDigits=0
    currentDigit=lines[0][0]
    cL=0
    keypad=curses.newwin(9,14,5,15)
    keypad.addstr(keys)
    keypad.refresh()
    oldKey=""
    while True:
        a = window.getkey()
        changeColorOfKey(keypad,oldKey,offColor)
        oldKey=a
        if a.isdigit():
            if a==currentDigit:
                window.addstr(1, 5, lines[cL][correctDigits+1:]+lines[cL+1][0:correctDigits])
                window.refresh()
                correctDigits+=1
                currentDigit=lines[cL][correctDigits]
                changeColorOfKey(keypad,a,rightColor)
                
            else:
                print('\a', end="",flush=True)
                changeColorOfKey(keypad,a,wrongColor)
            
        elif a == 'q':
            break
    exit(stdscr)

wrapper(main)
        
        

