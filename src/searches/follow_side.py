from searches.search import Search

class FollowSide(Search):

    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        self.state = 0

    def tick(self):
        # represents the movements of different states.
        def get_coord(state, x = self.rob.x, y = self.rob.y):
            #        up    left   down   right
            wheel = [[0,1],[-1,0],[0,-1],[1,0]]
            state = (state + 4) % 4
            ret = wheel[state]
            ret[0] += x
            ret[1] += y
            return ret

        # isn't solveable
        if self.rob.x == self.rob.start_x and self.rob.y == self.rob.start_y and self.moves != 0 and self.state == 0:
            pass
            #return False

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
        # step went well
        return True
