from searches.search import Search


class DFS(Search):

    def __init__(self, rob):
        super().__init__(rob)
        self.visited = None
        self.stack = []

    def tick(self):

        if self.visited is None:
            self.visited = [[False for x in range(self.rob.battleground.n)] for y in range(self.rob.battleground.m)]

        self.visited[self.rob.x][self.rob.y] = True

        view = self.rob.get_view()

        for x_off in [-1,1]:
            new_x = x_off + self.rob.x
            if 0 <= new_x < len(view) and view[new_x][self.rob.y] == 0 and not self.visited[new_x][self.rob.y]:
                self.rob.x += x_off
                self.inc_moves()
                self.stack.append((x_off,0))
                return True

        for y_off in [-1,1]:
            new_y = y_off + self.rob.y
            if 0 <= new_y < len(view[0]) and view[self.rob.x][new_y] == 0 and not self.visited[self.rob.x][new_y]:
                self.rob.y += y_off
                self.inc_moves()
                self.stack.append((0,y_off))
                return True
        
        if len(self.stack) == 0:
            return False

        back_x, back_y = self.stack.pop()
        self.rob.x -= back_x
        self.rob.y -= back_y
        self.inc_moves()

        return True
