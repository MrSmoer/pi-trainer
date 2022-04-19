import curses
from curses.ascii import isdigit
from Exceptions import DoneException
import ColorManager


class KeypadManager:
    def __init__(self,window):
        self.keypad=curses.newwin(9,14,5,15)
        self.keypad.addstr(self.keyPattern)
        
        self.keypad.refresh()
        self.rightColor, self.offColor, self.wrongColor = ColorManager.initColors()
        #return self.keypad

    def changeColorOfKey(self,char,color):
        if not char.isdigit():
            return
        if char != '':
            self.keypad.addch(self.keyCords[int(char)][0],self.keyCords[int(char)][1],char,color)
            self.keypad.refresh()


    def setKeyRight(self,key):
        self.changeColorOfKey(key,self.rightColor)

    def setKeyWrong(self,key):
        self.changeColorOfKey(key,self.wrongColor)

    def setKeyOff(self,key):
        self.changeColorOfKey(key,self.offColor)

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
