import copy
from time import sleep
from output.gui import render as gui_render
from output.console import get_display, display
from output.curses import render as curses_render
from searches.follow_left import FollowLeft

class Robot:

    DISPLAY_CONSOLE = display
    DISPLAY_CURSES = curses_render
    DISPLAY_WINDOW = gui_render
    DISPLAY_NONE = None

    def __init__(self, battleground, search = None, start = (0,0), goal = None, display_function=DISPLAY_NONE):
        """
        Initializes the robot
        :param battleground: The battleground object
        :param start: starting position
        :param goal: goal position
        :param display_function: function taking in terrain that is called every time the terrain is modified
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
        
        self.display_function = display_function

        # set the default search to be FollowLeft
        if search == None:
            #TODO:: PUT the best as default
            self.search = FollowLeft()
        else:
            self.search = search
        # give the search
        self.search.rob = self

    # string method, returns the battlefield with the robot marked on it.
    def __str__(self):
        arr = self.battleground.get_view()
        arr[self.x][self.y] = -1
        return get_display(arr)
    
    def render(self):
        if self.display_function is not None:
            view = self.battleground.get_view()
            view[self.x][self.y] = -1
            func = self.display_function
            func(view)
            sleep(0.2)
    
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
        return self.is_solved()

    # the number of steps the robot has taken
    def moves(self):
        return self.search.moves
