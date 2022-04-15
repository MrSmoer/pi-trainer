import curses
from curses import wrapper
from curses.ascii import isdigit
import time

lines = []

keyPattern='''╔═══╦═══╦═══╗
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

def readPifileToLines(filename):
    pifile = open(filename)
    
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

def initColors():
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
    return rightColor,offColor,wrongColor




class KeypadManager:
    
    
    def __init__(self):
        self.keypad=curses.newwin(9,14,5,15)
        self.keypad.addstr(keyPattern)
        self.keypad.refresh()
        self.rightColor, self.offColor, self.wrongColor = initColors()
        #return self.keypad

    def changeColorOfKey(self,char,color):
        if char != '':
            self.keypad.addch(keyCords[int(char)][0],keyCords[int(char)][1],char,color)
            self.keypad.refresh()


    def setKeyRight(self,key):
        self.changeColorOfKey(key,self.rightColor)

    def setKeyWrong(self,key):
        self.changeColorOfKey(key,self.wrongColor)
    def setKeyOff(self,key):
        self.changeColorOfKey(key,self.offColor)

class Display:
    def __init__(self,lines):
        self.display=curses.newwin(1,1,1,1)
        self.lines=lines

    def shiftLeft():
        print("",end="")

def main(stdscr):
    readPifileToLines('pi.txt')
    
    rightColor, offColor, wrongColor = initColors()
    initCursesSettings(stdscr)
    window = initMainWindow()
    keypad = KeypadManager()
    display = Display()

    digitOfLine=0
    currentDigit=lines[0][0]
    cL=0
    correctDigits=0
    oldKey=""

    while True:
        
        a = window.getkey()
        keypad.setKeyOff(oldKey)
        oldKey=a
        if a.isdigit():
            if a==currentDigit:
                display.shiftLeft
                digitOfLine+=1
                
                correctDigits+=1
                currentDigit=lines[cL][digitOfLine]
                keypad.setKeyRight(a)
                
            else:
                print('\a', end="",flush=True)
                keypad.setKeyWrong(a)
            
        elif a == 'q':
            break
    exit(stdscr)

wrapper(main)
  
    

 

        
        

