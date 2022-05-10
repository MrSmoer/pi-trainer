import curses


class ScoreBoard:
    def __init__(self, y, x):
        self.scWin= curses.newwin(3, 25, y, x)
        self.correctDigits=0
        self.mistakes=0
        self.x=x
        self.y=y
        self.goal=1
        self.goalVisible=False
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
        goalText=""
        if(self.goalVisible):
            goalText="/"+str(self.goal)
        self.scWin.addstr(0,1,"Digits: "+str(self.correctDigits)+goalText)
        self.scWin.addstr(2,1,"Mistakes: "+str(self.mistakes))
        self.scWin.refresh()
    
    def incrementGoal(self):
        self.goal += 1
        self.updateScreen()

    def showGoal(self):
        self.goalVisible=True
        self.updateScreen()

    def hideGoal(self):
        self.goalVisible=False
        self.updateScreen()
    
