import unittest
import curses

from piTrainer.piTrainer import Display, readPifileToLines


class DisplayTestClass(unittest.TestCase):
    def test_left(self):
        scr=curses.initscr()
        curses.start_color()
        lines=readPifileToLines("pi.txt")
        display=Display(lines)
        display.cL=0
        display.digitOfLine=26
        display.assembleLeft()
        #print("NextDigit: "+lines[display.cL][display.digitOfLine])
        self.assertEqual('979323846264338', display.assembleLeft())
        exit(scr)

def exit(stdscr):
    #curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    #curses.endwin()


if __name__ == '__main__':
    unittest.main()