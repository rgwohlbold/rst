from searches.search import Search
from random import choices

class RandomFrequency(Search):
    def __init__(self, rob):
        super().__init__(rob)
        # keep track of how many times each spot has been visited
        self.visited = [[0 for x in range(self.rob.battleground.n)] for y in range(self.rob.battleground.m)]
    
    def tick(self):
        # if you've been to the same space more than the width plus the height it
        # is unsolvable
        if self.visited[self.rob.x][self.rob.y] == \
                self.rob.battleground.n + self.rob.battleground.m:
            return False
        self.visited[self.rob.x][self.rob.y] += 1
        view = self.rob.get_view()
        # turn a movement tuple into the resulting position 
        def coord(movement):
            return (self.rob.x + movement[0], self.rob.y + movement[1])

        # is the movement given legal, (the space is open and inbounds of the battleground)
        def viable(movement):
            x, y = coord(movement)
            return self.rob.battleground.in_bounds(x,y) and view[x][y] == 0
        
        # get the number of times that the space resulting from the given movement
        # has been moved on.
        def get_weight(movement):
            x, y = coord(movement) 
            return self.visited[x][y]

        movements = list(filter(viable, [(0,1),(1,0),(0,-1),(-1,0)]))
        weights = list(map(get_weight, movements))
        maximum = max(weights)
        if all(map(lambda x : x==maximum, weights)):
            move = choices(movements)
        else:
            # subtract all the weights from the maximum, 
            # this makes it do that weights of [100,101,100] and [20,21,20]
            # both simplify to [1,0,1]
            shrinked_weights = list(map(lambda x : maximum - x, weights))
            # divide each weight by the sum so that the sum of the resulting array is 1
            total = sum(shrinked_weights)
            new_weights = list(map(lambda x : x / total, shrinked_weights))
            move = choices(movements, new_weights)
        x, y = coord(move[0])
        self.rob.x = x
        self.rob.y = y
        self.inc_moves()
        return True
