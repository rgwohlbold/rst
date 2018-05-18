import copy
from time import sleep
from output.gui import GUI
from output.console_plain import ConsolePlain
from output.console_color import ConsoleColor
from output.curses_plain import ConsoleCursesPlain
from output.curses_color import ConsoleCursesColor
from searches.follow_left import FollowLeft
from searches.follow_right import FollowRight
from searches.random import Random
from searches.random_frequency import RandomFrequency
from searches.dfs import DFS
from searches.random_dfs import RandomDFS


class Robot:

    DISPLAY_PLAIN = ConsolePlain
    DISPLAY_COLOR = ConsoleColor
    DISPLAY_CURSES_PLAIN = ConsoleCursesPlain
    DISPLAY_CURSES_COLOR = ConsoleCursesColor
    DISPLAY_WINDOW = GUI
    DISPLAY_NONE = None

    SEARCH_DFS = DFS
    SEARCH_FOLLOW_LEFT = FollowLeft
    SEARCH_FOLLOW_RIGHT = FollowRight
    SEARCH_RANDOM = Random
    SEARCH_RANDOM_FREQUENCY = RandomFrequency
    SEARCH_RANDOM_DFS = RandomDFS

    def __init__(self, battleground, search=SEARCH_FOLLOW_LEFT, start=(0,0), goal=None, display=DISPLAY_NONE, speed=0.2):
        """
        Initializes the robot
        :param battleground: The battleground object
        :param search: An uninitialized Search class
        :param start: starting position
        :param goal: goal position
        :param display_function: An unintialized Renderer class
        :param speed: Interval between render steps (if display is not None)
        """
        self.battleground = battleground

        # the robot's position
        self.x = start[0]
        self.y = start[1]

        # the starting position
        self.start_x = start[0]
        self.start_y = start[1]

        # set the default goal to be the bottom right corner unless
        # otherwise specified
        if goal == None:
            self.goal_x = battleground.m - 1
            self.goal_y = battleground.n - 1
        else:
            self.goal_x = goal[0]
            self.goal_y = goal[1]

        if display is not None:
            self.display = display()
        else:
            self.display = None
        self.speed = speed

        # TODO specify best as default
        if search is not None:
            self.search = search(self)

    # string method, returns the battlefield with the robot marked on it.
    def __str__(self):
        arr = self.battleground.get_view()
        arr[self.x][self.y] = -1
        return ConsolePlain.get_display(arr)
    
    def render(self):
        if self.display is not None:
            view = self.battleground.get_view()
            view[self.x][self.y] = -1
            self.display.render(view)
            sleep(self.speed)
    
    # gets the robots view from the battleground
    def get_view(self):
        return self.battleground.get_view(self.x, self.y, True)

    # True if the robot is at the finish
    def is_solved(self):
        return self.x == self.goal_x and self.y == self.goal_y


    # follow movement algo for one step
    # if it returns false the algo is finished
    def tick(self):
        if self.is_solved():
            ret = False
        else:
            ret = self.search.tick()

        self.render() 

        return ret

    # play out untill shown to be unsolvable or solved
    # if it solved the maze True, else False
    def run(self):
        while self.tick():
            pass
        self.display.__del__()
        return self.is_solved()

    # the number of steps the robot has taken
    def moves(self):
        return self.search.moves
