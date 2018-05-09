import curses
import atexit
from .console import get_display

initialized = False
stdscr = None


def init():
    global stdscr, initialized
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    atexit.register(destroy)
    initialized = True

def render(terrain):
    global stdscr, initialized
    if not initialized:
        init()
    stdscr.clear()
    s = get_display(terrain)
    import util
    s = util.uncolorize(s)
    lines = s.split("\n")
    for line in lines:
        stdscr.addstr(line + "\n")
    stdscr.refresh()


def destroy():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

