import copy 

class Robot:

    def __init__(self, battleground, start = (0,0), goal = None):
        self.x = start[0]
        self.y = start[1]
        self.battleground = battleground 
        if goal == None:
            self.goal_x = battleground.m - 1
            self.goal_y = battleground.n - 1
        else:
            self.goal_x = goal[0]
            self.goal_y = goal[1]
        self.visited = [[False for x in range(battleground.m)] for y in range(battleground.n)]
        self.moves = -1

    def dfs(self):
        if self.visited[self.x][self.y]:
            return False 
        self.moves += 1
        self.visited[self.x][self.y] = True
        if self.x == self.goal_x and self.y == self.goal_y:
            return True 
        view = self.battleground.get_view(self.x,self.y,True)
        for x_off in [-1,1]:
            new_x = x_off + self.x 
            if 0 <= new_x < len(view) and view[new_x][self.y] == 0:
                self.x += x_off 
                if self.dfs():
                    return True 
                self.x -= x_off 
        for y_off in [-1,1]:
            new_y = y_off + self.y 
            if 0 <= new_y < len(view[0]) and view[self.x][new_y] == 0:
                self.y += y_off 
                if self.dfs():
                    return True 
                self.y -= y_off 
        return False 

                
