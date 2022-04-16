import curses


class ScoreBoard:
    def __init__(self, y, x):
        self.scWin= curses.newwin(3, 25, y, x)
        self.correctDigits=0
        self.mistakes=0
        self.x=x
        self.y=y
        self.updateScreen()
    
    def incrementScore(self):
        self.correctDigits+=1
        self.updateScreen()
    
    def incrementMistakes(self):
        self.mistakes+=1
        self.updateScreen()
    
    def reset(self):
        self.correctDigits=0
        self.mistakes=0

    def updateScreen(self):
        self.scWin.addstr(0,1,"Digits: "+str(self.correctDigits))
        self.scWin.addstr(2,1,"Mistakes: "+str(self.mistakes))
        self.scWin.refresh()
