import atexit
from output.renderer import Renderer


class ConsoleCursesColor(Renderer):

    def __init__(self):
        try:
            self.curses = __import__("curses")
        except ImportError:
            raise RuntimeError("Trying to use curses rendering backend without curses module installed!")

        self.config = {
            -1: ("=", 1, self.curses.COLOR_CYAN, self.curses.COLOR_BLACK),
            0: ("_", 2, self.curses.COLOR_WHITE, self.curses.COLOR_BLACK),
            1: ("#", 3, self.curses.COLOR_WHITE, self.curses.COLOR_BLACK),
            2: ("O", 4, self.curses.COLOR_RED, self.curses.COLOR_BLACK),
            3: ("^", 5, self.curses.COLOR_GREEN, self.curses.COLOR_BLACK),
            "all": ("^", 6, self.curses.COLOR_BLUE, self.curses.COLOR_BLACK)
        }

        self.destroyed = False
        self.stdscr = self.curses.initscr()
        self.curses.start_color()
        self.curses.noecho()
        self.curses.cbreak()
        for k in self.config.keys():
            self.curses.init_pair(self.config[k][1], self.config[k][2], self.config[k][3])
        self.curses.curs_set(0)
        atexit.register(self.__del__)

    def render(self, terrain):
        for i,r in enumerate(terrain):
            for j,c in enumerate(r):
                if c in self.config.keys():
                    self.stdscr.addstr(i,j*2,self.config[c][0],self.curses.color_pair(self.config[c][1]))
                else:
                    self.stdscr.addstr(i,j*2,self.config["all"][0],self.curses.color_pair(self.config["all"][1]))

        last = terrain
        self.stdscr.move(8,0)
        self.stdscr.refresh()

    def __del__(self):
        if not self.destroyed:
            self.curses.nocbreak()
            self.stdscr.keypad(False)
            self.curses.echo()
            self.curses.endwin()

            self.destroyed = True

