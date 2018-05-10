import atexit
from output.renderer import Renderer


class ConsoleCursesPlain(Renderer):

    def __init__(self):
        try:
            self.curses = __import__("curses")
        except ImportError:
            raise RuntimeError("Trying to use curses rendering backend without curses module installed!")

        self.config = {
            -1: "=",
            0: "_",
            1: "#",
            2: "O",
            3: "^",
            "all": "^"
        }

        self.stdscr = self.curses.initscr()
        self.curses.start_color()
        self.curses.noecho()
        self.curses.cbreak()
        self.curses.curs_set(0)
        atexit.register(self.__del__)

    def render(self, terrain):
        for i,r in enumerate(terrain):
            for j,c in enumerate(r):
                if c in self.config.keys():
                    self.stdscr.addstr(i,j*2,self.config[c][0])
                else:
                    self.stdscr.addstr(i,j*2,self.config["all"][0])

        last = terrain
        self.stdscr.move(8,0)
        self.stdscr.refresh()

    def __del__(self):
        self.curses.nocbreak()
        self.stdscr.keypad(False)
        self.curses.echo()
        self.curses.endwin()

