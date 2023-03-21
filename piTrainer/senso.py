import PiFileReader
import KeypadManager
import Display
import ScoreBoard
import Exceptions

class senso():
    def __init__(self) -> None:
        pass
        
    def animateTilGoal(self):
        self.keypad.clear()
        self.display.animateFromNtoM(0,self.scBoard.goal,self.keypad, self.scBoard)

    def start(self,window,fileToLearn):
        increments=1
        pireader=PiFileReader.PiFileReader(fileToLearn)
        lines=pireader.lines
        self.keypad = KeypadManager.KeypadManager(window)
        self.display = Display.Display(lines)
        self.display.rightEnabled=False
        self.scBoard = ScoreBoard.ScoreBoard(10, 30)
        self.scBoard.showGoal(True)
        self.scBoard.showIncrements(True)

        currentDigit=self.display.getCurrentDigit()
        oldKey=""
        self.display.showStandard()
        self.keypad.keypad.touchwin()
        self.scBoard.goal=1
        self.scBoard.correctDigits=0
        skipstuff=False
        try:
            while True:
                if not skipstuff:
                    self.animateTilGoal()
                    self.scBoard.correctDigits=0
                    self.scBoard.updateScreen()
                    self.display.showStandard()
                    self.currentDigit=0
                    #skipstuff=False
                else:
                    skipstuff=False
                self.scBoard.updateScreen()
                returnValue=self.handleInput(window, oldKey)
                if returnValue == 'q':
                    break
                if returnValue == 'r':
                    window.erase()
                    window.refresh()
                    self.start(window,fileToLearn)
                if returnValue == '+':
                    increments += 1
                    self.scBoard.incrementSize=increments
                    skipstuff=True
                    continue
                if returnValue == '-':
                    if increments > 1:
                        increments += -1
                        self.scBoard.incrementSize=increments
                    skipstuff=True
                    continue
                        
                    
                self.scBoard.goal += increments
                self.scBoard.correctDigits=0
                self.scBoard.updateScreen()
                self.display.setScreenToN(0)

        except Exceptions.DoneException:  
            print("You typed all digits of the number that are provided in the Database ...")
            print(" ")

    def handleInput(self, window, oldKey):
        while self.scBoard.correctDigits < self.scBoard.goal:
            self.currentDigit=self.display.getCurrentDigit()
            keypressed = window.getkey()

                        
            self.keypad.setKeyOff(oldKey)
            oldKey=keypressed
            controlKeys={'q','r','+','-'}
            if keypressed.isdigit():
                if keypressed==self.currentDigit:
                    self.display.shiftLeft()
                    self.display.showStandard()
                    self.keypad.setKeyRight(keypressed)  
                    self.scBoard.incrementScore()
                else:
                    print('\a', end="",flush=True)
                    self.keypad.setKeyWrong(keypressed)
                            
                    self.scBoard.incrementMistakes()
                            
            elif keypressed in controlKeys:
                return keypressed
                

    
