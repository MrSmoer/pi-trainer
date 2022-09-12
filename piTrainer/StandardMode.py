import PiFileReader
import KeypadManager
import Display
import ScoreBoard
import Exceptions

class Standard():
    
    def start(self,window,fileToLearn):
        pireader=PiFileReader.PiFileReader(fileToLearn)
        lines=pireader.lines
        keypad = KeypadManager.KeypadManager(window)
        display = Display.Display(lines)
        scBoard = ScoreBoard.ScoreBoard(10, 30)

        currentDigit=display.getCurrentDigit()
        correctDigits=0
        oldKey=""
        display.showStandard()
        keypad.keypad.touchwin()
        try:
            while True:
                currentDigit=display.getCurrentDigit()
                a = window.getkey()
                    
                keypad.setKeyOff(oldKey)
                oldKey=a
                if a.isdigit():
                    if a==currentDigit:
                        display.shiftLeft()
                        display.showStandard()
                        correctDigits+=1
                        keypad.setKeyRight(a)  
                        scBoard.incrementScore()
                    else:
                        print('\a', end="",flush=True)
                        keypad.setKeyWrong(a)
                        
                        scBoard.incrementMistakes()
                        
                elif a == 'q':
                    break
                elif a == 'r':
                    window.erase()
                    window.refresh()
                    self.start(window,fileToLearn)
        except Exceptions.DoneException:  
            print("You typed all digits of Pi that are provided in the Database ...")
            print(" ")