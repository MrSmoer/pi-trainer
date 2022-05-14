import curses
import time
import KeypadManager
import PiFileReader
import Display
import ScoreBoard
import Exceptions


class learnMode:
    def start(self, window):
        default_digit=5
        window.addstr(1,1,"Which digit is your first target?(default is "+str(default_digit)+")")
        curses.echo(True)
        curses.cbreak(False)
        c=window.getstr().decode(encoding="utf-8")
        curses.noecho()
        curses.cbreak(True)
        if c =='' or not c.isnumeric():
            c=default_digit
        target=int(c)
        pireader=PiFileReader.PiFileReader('pi.txt')
        lines=pireader.lines
        keypad = KeypadManager.KeypadManager(window)
        display = Display.Display(lines)
        scBoard = ScoreBoard.ScoreBoard(10, 30)
        scBoard.showGoal()
        currentDigit=display.getCurrentDigit()
        correctDigits=0
        oldKey=""
        self.showLeft(display)
        keypad.keypad.touchwin()
        for i in range(target):
            keypad.setKeyOff(oldKey)
            currentDigit=display.getCurrentDigit()
            oldKey=currentDigit
            display.shiftLeft()
            self.showLeft(display)
            correctDigits+=1
            keypad.setKeyRight(currentDigit)
            scBoard.incrementScore()
            time.sleep(0.5)
        try:
            while True:
                currentDigit=display.getCurrentDigit()
                a = window.getkey()
                    
                keypad.setKeyOff(oldKey)
                oldKey=a
                if a.isdigit():
                    if a==currentDigit:
                        display.shiftLeft()
                        self.showLeft(display)
                        correctDigits+=1
                        keypad.setKeyRight(a)  
                        scBoard.incrementScore()
                    else:
                        print('\a', end="",flush=True)
                        keypad.setKeyWrong(a)
                        raise Exceptions.GameOverException
                        #scBoard.incrementMistakes()
                        
                elif a == 'q':
                    break
                elif a == 'r':
                    self.retry(window)
        except Exceptions.DoneException:  
            print("You typed all digits of Pi that are provided in the Database ...")
            print(" ")
        except Exceptions.GameOverException:
            display.display.erase()
            display.display.refresh()
            keypad.keypad.erase()
            keypad.keypad.refresh()
            scBoard.scWin.erase()
            scBoard.scWin.refresh()
            startLine = 3
            window.addstr(startLine+0,3,"GAME OVER, "+str(correctDigits)+" CORRECT DIGITS")
            window.addstr(startLine+1,4,"DIGIT "+str(correctDigits+1)+" WOULD HAVE BEEN A "+str(currentDigit))
            window.addstr(startLine+2,3,"PRESS r TO RETRY AND ANY OTHER KEY TO QUIT")
            window.refresh()
            a=window.getkey()
            if a == 'r':
                self.retry(window)
                

    
    def showLeft(self,display):
        left=display.assembleLeft()
        #right=display.assembleRight()
        #display.display.addstr(1,16,right,display.offColor)
        display.display.refresh()
        display.display.touchwin()
    
    def retry(self,window):
        window.erase()
        window.refresh()
        self.start(window)
