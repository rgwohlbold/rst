from searches.search import Search
from random import randint


class Random(Search):    
    def tick(self):
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        direction = directions[randint(0,3)]
        new_x, new_y = map(sum, zip(direction, (self.rob.x, self.rob.y)))
        
        view = self.rob.get_view()

        if self.rob.battleground.in_bounds(new_x, new_y) and view[new_x][new_y] == 0:
            self.inc_moves()
            self.rob.x, self.rob.y = new_x, new_y
        else:
            return self.tick()
        
        return True
