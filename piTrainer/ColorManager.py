import curses


def initColors():
    if curses.has_colors:
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        #curses.init_pair(0, -1, -1)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        rightColor=curses.color_pair(1)
        offColor=curses.color_pair(0)
        wrongColor=curses.color_pair(2)
    else:
        rightColor=curses.A_STANDOUT
        offColor=curses.A_NORMAL
        wrongColor=curses.A_BLINK
    return rightColor,offColor,wrongColor

