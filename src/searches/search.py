import time
# interface for a solving algorithm

class Search:

    def __init__(self):
        self.debug = False
        self.rob = None
        self.moves = 0

    # run one step of the search algorithm
    # should return false if the algorithm is the maze is unsolveable
    # otherwise return true
    def tick(self):
        # using this default implimentation the maze will never be solved.
        return False

    def inc_moves(self):
        self.moves += 1
        if self.debug:
            time.sleep(.2)
            print("\n")
            print(self.rob)

    def in_bounds(self, x, y):
        return -1 < self.rob.y < self.rob.battleground.n and -1 < x < self.rob.battleground.m
