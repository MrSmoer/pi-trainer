import time
import PiFileReader
import KeypadManager
import Display
import ScoreBoard
import Exceptions

class Standard():
    
    def start(self,window):
        pireader=PiFileReader.PiFileReader()
        lines=pireader.readPifileToLines('pi.txt')
        keypad = KeypadManager.KeypadManager(window)
        display = Display.Display(lines)
        scBoard = ScoreBoard.ScoreBoard(10, 30)

        currentDigit=display.getCurrentDigit()
        correctDigits=0
        oldKey=""
        display.show()
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
                        correctDigits+=1
                        keypad.setKeyRight(a)  
                        scBoard.incrementScore()
                    else:
                        print('\a', end="",flush=True)
                        keypad.setKeyWrong(a)
                        scBoard.incrementMistakes()
                        
                elif a == 'q':
                    break
        except Exceptions.DoneException:  
            print("You typed all digits of Pi that are provided in the Database ...")
            print(" ")