import curses
import ColorManager
from Exceptions import DoneException
import time
import PiFileReader

class Display:
    def __init__(self,lines):
        self.display=curses.newwin(4,curses.COLS-1,1,1)
        self.lines=lines
        self.currentDigit=lines[0][0]
        self.digitOfLine=0
        self.cL=0
        self.rightColor, self.offColor, self.wrongColor = ColorManager.initColors()
        self.leftDisplay=15
        self.rightEnabled=True

    def shiftLeft(self):
        

        if Display.isLongerThanLine(self.digitOfLine, self.lines[self.cL]):
            self.cL+=1
            self.digitOfLine=0
            if self.cL == len(self.lines):
                raise DoneException
        else:
            self.digitOfLine += 1

        
        

    def showStandard(self):
        left=self.assembleLeft()
        right=self.assembleRight()
        
        self.display.refresh()
        self.display.touchwin()

    
    @staticmethod
    def isLongerThanLine(index,line):
        if index >= len(line)-1:
            return True
        else:
            return False
    
    def assembleRight(self):
        right=''
        if self.rightEnabled:
            currentline=self.lines[self.cL][self.digitOfLine:]
            nextline=''
            if len(self.lines)>self.cL+1:
                nextline=self.lines[self.cL+1][0:self.digitOfLine]
            right=currentline+nextline
            
            self.display.addstr(1,self.leftDisplay+1,right,self.offColor)
        return right
    
    def assembleLeft(self):
        ## OLDLINE
        oldline=''
        if self.leftDisplay > self.digitOfLine and not self.isFirstLine():
            spaceForOld=self.leftDisplay - self.digitOfLine
            oldline=self.lines[self.cL-1][-spaceForOld:]
        
        ## CURRENT LINE
        currentline=self.lines[self.cL][:self.digitOfLine]
        if self.leftDisplay < len(currentline):
            charsToChop = len(currentline)-self.leftDisplay
            currentline = currentline[charsToChop:]
        left=oldline+currentline

        ## START FROM MIDDLE
        #xstart=1
        spacepad=''
        if self.isFirstLine() and self.digitOfLine<self.leftDisplay:
            
        #    xstart=self.leftDisplay+1-self.digitOfLine
            spaceCount=self.leftDisplay-self.digitOfLine
            for i in range(spaceCount):
                spacepad=' '+spacepad
            self.display.addstr(1,1, spacepad,self.offColor)
            
        self.display.addstr(1,len(spacepad)+1, left,self.rightColor)
        #self.display.addstr(3,1, currentline+"                       ",self.rightColor)
        return left
    
    def getCurrentDigit(self):
        currentDigit=self.lines[self.cL][self.digitOfLine]
        return currentDigit
    def isFirstLine(self):
        return self.cL==0

    def animateFromNtoM(self,n,m,keypad,scBoard):
        oldKey=''
        oldN=self.cL*len(self.lines[0])+self.digitOfLine
        self.setScreenToN(n)
        currentDigit=0
        for i in range(m-n):
            keypad.setKeyOff(oldKey)
            currentDigit=self.getCurrentDigit()
            oldKey=currentDigit
            self.shiftLeft()
            self.showStandard()
            #correctDigits+=1
            keypad.setKeyRight(currentDigit)
            scBoard.incrementScore()
            time.sleep(0.1)
        scBoard.score=n
        self.setScreenToN(oldN)
        keypad.setKeyOff(currentDigit)

    def setScreenToN(self,n):
        piFile=PiFileReader.PiFileReader('pi.txt')
        self.currentDigit=piFile.getDigit(n)
        self.digitOfLine=piFile.getDigitOfLine(n)
        self.cL=piFile.getLineOfDigit(n)
        self.showStandard()
