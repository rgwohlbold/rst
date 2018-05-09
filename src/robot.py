from searches.follow_left import FollowLeft

import copy
from display import get_display
from time import sleep


class Robot:

    def __init__(self, battleground, search = None, start = (0,0), goal = None, debug = False):
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

        # set the default search to be FollowLeft
        if search == None:
            #TODO:: PUT the best as default
            self.search = FollowLeft()
        else:
            self.search = search
        # give the search
        self.search.rob = self
        self.search.debug = debug

    # string method, returns the battlefield with the robot marked on it.
    def __str__(self):
        arr = self.battleground.get_view()
        arr[self.x][self.y] = -1
        return get_display(arr)
    
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
            return False
        return self.search.tick()

    # play out untill shown to be unsolvable or solved
    # if it solved the maze True, else False
    def run(self):
        while self.tick():
            pass
        return self.is_solved()

    # the number of steps the robot has taken
    def moves(self):
        return self.search.moves
