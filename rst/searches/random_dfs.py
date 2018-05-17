from searches.search import Search
from random import choices

class RandomDFS(Search):
    def __init__(self, rob):
        super().__init__(rob)
        self.stack = []
        self.visited = [[False for x in range(self.rob.battleground.n)] for y in range(self.rob.battleground.m)]

    def tick(self):
        self.visited[self.rob.x][self.rob.y] = True

        view = self.rob.get_view()
        
        def coord(movement):
            return (self.rob.x + movement[0], self.rob.y + movement[1])

        # is the movement given legal, (the space is open and inbounds of the battleground)
        def viable(movement):
            x, y = coord(movement)
            return self.rob.battleground.in_bounds(x,y) and view[x][y] == 0 and not(self.visited[x][y])
        
        movements = list(filter(viable, [(0,1), (1,0), (0,-1), (-1,0)]))
        
        if len(movements) == 0:
            if len(self.stack) == 0:
                return False

            back_x, back_y = self.stack.pop()
            self.rob.x -= back_x
            self.rob.y -= back_y
            self.inc_moves()

            return True
        else:
            movement = choices(movements)[0]
            self.rob.x, self.rob.y = coord(movement)
            self.stack.append(movement)
            self.inc_moves()

            return True

