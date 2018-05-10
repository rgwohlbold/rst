import atexit
from output.renderer import Renderer


class ConsoleCurses(Renderer):

    def __init__(self):
        try:
            __import__("curses")
        except ImportError:
            raise RuntimeError("Trying to use curses rendering backend without curses module installed!")
        import curses

        self.config = {
            -1: ("=", 1, curses.COLOR_CYAN, curses.COLOR_BLACK),
            0: ("_", 2, curses.COLOR_WHITE, curses.COLOR_BLACK),
            1: ("#", 3, curses.COLOR_WHITE, curses.COLOR_BLACK),
            2: ("O", 4, curses.COLOR_RED, curses.COLOR_BLACK),
            3: ("^", 5, curses.COLOR_GREEN, curses.COLOR_BLACK),
            "all": ("^", 6, curses.COLOR_BLUE, curses.COLOR_BLACK)
        }

        self.stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        for k in self.config.keys():
            curses.init_pair(self.config[k][1], self.config[k][2], self.config[k][3])
        curses.curs_set(0)

    def render(self, terrain):
        try:
            __import__("curses")
        except ImportError:
            raise RuntimeError("Trying to use curses rendering backend without curses module installed!")
        import curses

        for i,r in enumerate(terrain):
            for j,c in enumerate(r):
                if c in self.config.keys():
                    self.stdscr.addstr(i,j*2,self.config[c][0],curses.color_pair(self.config[c][1]))
                else:
                    self.stdscr.addstr(i,j*2,self.config["all"][0],curses.color_pair(self.config["all"][1]))

        last = terrain
        self.stdscr.move(8,0)
        self.stdscr.refresh()


    def __del__(self):
        try:
            __import__("curses")
        except ImportError:
            raise RuntimeError("Trying to use curses rendering backend without curses module installed!")
        import curses

        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

