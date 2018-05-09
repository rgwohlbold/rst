import importlib

curses_loader = importlib.util.find_spec("curses")
found = curses_loader is not None
if curses_loader is not None:
    import curses
import atexit


initialized = False
stdscr = None
last = [[-5] * 9] * 8

config = {
    -1: ("=", 1, curses.COLOR_CYAN, curses.COLOR_BLACK),
    0: ("_", 2, curses.COLOR_WHITE, curses.COLOR_BLACK),
    1: ("#", 3, curses.COLOR_WHITE, curses.COLOR_BLACK),
    2: ("O", 4, curses.COLOR_RED, curses.COLOR_BLACK),
    3: ("^", 5, curses.COLOR_GREEN, curses.COLOR_BLACK),
    "all": ("^", 6, curses.COLOR_BLUE, curses.COLOR_BLACK)
}


def init():
    if not found:
        raise RuntimeError("Trying to use curses rendering backend without curses module installed!")

    global stdscr, initialized
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    for k in config.keys():
        curses.init_pair(config[k][1], config[k][2], config[k][3])
    curses.curs_set(0);
    atexit.register(destroy)
    initialized = True


def render(terrain):
    global stdscr, initialized, last
    if not initialized:
        init()
    for i,r in enumerate(terrain):
        for j,c in enumerate(r):
            if c in config.keys():
                stdscr.addstr(i,j*2,config[c][0],curses.color_pair(config[c][1]))
            else:
                stdscr.addstr(i,j*2,config["all"][0],curses.color_pair(config["all"][1]))

    last = terrain
    stdscr.move(8,0)
    stdscr.refresh()


def destroy():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

