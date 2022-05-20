import PiFileReader
import KeypadManager
import Display
import ScoreBoard
import Exceptions

class simonSays():
    def __init__(self) -> None:
        pass
        
    def animateTilGoal(self):
        self.keypad.clear()
        self.display.animateFromNtoM(0,self.scBoard.goal,self.keypad, self.scBoard)

    def start(self,window):
        pireader=PiFileReader.PiFileReader('pi.txt')
        lines=pireader.lines
        self.keypad = KeypadManager.KeypadManager(window)
        self.display = Display.Display(lines)
        self.display.rightEnabled=False
        self.scBoard = ScoreBoard.ScoreBoard(10, 30)
        self.scBoard.showGoal(True)

        currentDigit=self.display.getCurrentDigit()
        oldKey=""
        self.display.showStandard()
        self.keypad.keypad.touchwin()
        self.scBoard.goal=1
        self.scBoard.correctDigits=0
        try:
            while True:
                self.animateTilGoal()
                self.scBoard.correctDigits=0

                self.scBoard.updateScreen()
                self.display.showStandard()
                self.currentDigit=0
                returnValue=self.handleInput(window, oldKey)
                if returnValue == 'q':
                    break
                if returnValue == 'r':
                    window.erase()
                    window.refresh()
                    self.start(window)
                    
                self.scBoard.goal += 1
                self.scBoard.correctDigits=0
                self.scBoard.updateScreen()
                self.display.setScreenToN(0)

        except Exceptions.DoneException:  
            print("You typed all digits of Pi that are provided in the Database ...")
            print(" ")

    def handleInput(self, window, oldKey):
        while self.scBoard.correctDigits < self.scBoard.goal:
            self.currentDigit=self.display.getCurrentDigit()
            a = window.getkey()

                        
            self.keypad.setKeyOff(oldKey)
            oldKey=a
            if a.isdigit():
                if a==self.currentDigit:
                    self.display.shiftLeft()
                    self.display.showStandard()
                    self.keypad.setKeyRight(a)  
                    self.scBoard.incrementScore()
                else:
                    print('\a', end="",flush=True)
                    self.keypad.setKeyWrong(a)
                            
                    self.scBoard.incrementMistakes()
                            
            elif a == 'q':
                return 'q'
            elif a == 'r': 
                return 'r'
                

    
