import time
import PiFileReader
import KeypadManager
import Display
import ScoreBoard
import Exceptions

class simonSays():
    def __init__(self) -> None:
        pass
        
    def animateTilGoal(self):
        self.display.animateFromNtoM(0,self.scBoard.goal,self.keypad, self.scBoard)

    def start(self,window):
        pireader=PiFileReader.PiFileReader('pi.txt')
        lines=pireader.lines
        self.keypad = KeypadManager.KeypadManager(window)
        self.display = Display.Display(lines)
        self.scBoard = ScoreBoard.ScoreBoard(10, 30)
        self.scBoard.showGoal(True)

        currentDigit=self.display.getCurrentDigit()
        correctDigits=0
        oldKey=""
        self.display.showStandard()
        self.keypad.keypad.touchwin()
        self.scBoard.goal=20
        self.scBoard.correctDigits=0
        try:
            while True:
                self.animateTilGoal()
                currentDigit=self.display.getCurrentDigit()
                a = window.getkey()
                    
                self.keypad.setKeyOff(oldKey)
                oldKey=a
                if a.isdigit():
                    if a==currentDigit:
                        self.display.shiftLeft()
                        self.display.showStandard()
                        correctDigits+=1
                        self.keypad.setKeyRight(a)  
                        self.scBoard.incrementScore()
                    else:
                        print('\a', end="",flush=True)
                        self.keypad.setKeyWrong(a)
                        
                        self.scBoard.incrementMistakes()
                        
                elif a == 'q':
                    break
                elif a == 'r':
                    window.erase()
                    window.refresh()
                    self.start(window)
        except Exceptions.DoneException:  
            print("You typed all digits of Pi that are provided in the Database ...")
            print(" ")

    
