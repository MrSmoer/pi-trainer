import curses
from curses import wrapper
import ColorManager
import StandardMode
import learnMode
import senso
import numberToLearn

        
def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    

def initMainWindow():
    window = curses.newwin(curses.LINES-1, curses.COLS-1)
    window.nodelay(False)
    window.refresh()
    return window


def initCursesSettings(stdscr):
    curses.noecho()
    # doesn't need return to get keys
    curses.cbreak()
    # disable cursor
    curses.curs_set(0)
    stdscr.keypad(True)

def callwrapper():
    wrapper(main)

def main(stdscr):
    fileToLearn="pi.txt"
    while(True):
        rightColor, offColor, wrongColor =  ColorManager.initColors()
        initCursesSettings(stdscr)
        window = initMainWindow()
        modes={
            1:(StandardMode.Standard(),"Standard"),
            2:(learnMode.learnMode(),"Number Learning"),
            3:(senso.senso(),"Senso"),
            4:(numberToLearn.numberToLearn(),"Select number")
        }
        yCordOfOpt=4
        window.addstr(yCordOfOpt,3,"Select Mode")
        for key in modes:
            text= str(key)+') '+modes.get(key)[1]
            yCordOfOpt +=1
            window.addstr(yCordOfOpt,3,text)
        
        a=''
        while not a.isdigit():
            a = window.getkey()
            if a=='q':
                break
        
        if not a.isdigit():
            exit(stdscr)
            return
        game=modes.get(int(a))[0]
        window.erase()
        window.refresh()
        returning=game.start(window,fileToLearn)
        print(returning)
        if returning is None or not returning[0]:
            exit(stdscr)
            break
        if returning[1] is not None:
            fileToLearn=returning[1]
    

if __name__== '__main__':
    callwrapper()
  
    

 

        
        

