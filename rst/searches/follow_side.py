from searches.search import Search

class FollowSide(Search):

    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        self.state = 0
        self.initialized = False

    def _init_with_robot(self):
        """
        Initializes the search when self.robot is available, call this only once
        Sets self.initialized to True
        """

        # Put all valid adjacent fields of the starting positions into self.adjacent
        self.adjacent = []
        if self.rob.battleground.in_bounds(self.rob.start_x - 1,self.rob.start_y):
            self.adjacent.append((self.rob.start_x - 1, self.rob.start_y))

        if self.rob.battleground.in_bounds(self.rob.start_x, self.rob.start_y - 1):
            self.adjacent.append((self.rob.start_x, self.rob.start_y - 1))

        if self.rob.battleground.in_bounds(self.rob.start_x + 1, self.rob.start_y):
            self.adjacent.append((self.rob.start_x + 1, self.rob.start_y))

        if self.rob.battleground.in_bounds(self.rob.start_x, self.rob.start_y + 1):
            self.adjacent.append((self.rob.start_x, self.rob.start_y + 1))

        self.initialized = True

    def tick(self):
        if not self.initialized:
            self._init_with_robot()

        # represents the movements of different states.
        def get_coord(state, x = self.rob.x, y = self.rob.y):
            #        down   left   up   right
            wheel = [[0,1],[-1,0],[0,-1],[1,0]]
            state = (state + 4) % 4
            ret = wheel[state]
            ret[0] += x
            ret[1] += y
            return ret

        # it isn't solvable if we are on our starting positions, we have moved and visited every adjacent field
        if self.rob.x == self.rob.start_x and self.rob.y == self.rob.start_y and self.moves != 0 and len(self.adjacent) == 0:
            return False

        self.state = (self.state + 4) % 4
        view = self.rob.get_view()
        # if the block beneath me is open, move down, else if it is closed, if the front is open move their
        # if it isn't, move up
        # 'beneath' x and y
        bx, by = get_coord(self.state + self.direction)
        if (self.rob.battleground.in_bounds(bx, by) and view[bx][by] == 0):
            self.rob.x = bx
            self.rob.y = by
            self.state += self.direction
            self.inc_moves()
        else:
            # 'forward' x and y
            fx, fy = get_coord(self.state)
            if (self.rob.battleground.in_bounds(fx, fy) and view[fx][fy] == 0):
                self.rob.x = fx
                self.rob.y = fy
                self.inc_moves()
            else:
                self.state -= self.direction

        # Remove current position from self.adjacent to signal that we already visited this position
        if (self.rob.x, self.rob.y) in self.adjacent:
            self.adjacent.remove((self.rob.x, self.rob.y))
        # step went well
        return True
