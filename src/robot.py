import copy 
from display import get_display
from time import sleep 

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
        self.visited = [[False for x in range(battleground.n)] for y in range(battleground.m)]
        self.moves = -1
    
    def __str__(self):
        arr = self.battleground.get_view()
        arr[self.x][self.y] = -1
        return get_display(arr) 



    # depth first search on the battleground
    def dfs(self, debug = False):
        if self.visited[self.x][self.y]:
            return False 
        
        self.inc_moves(debug)
        self.visited[self.x][self.y] = True
        
        if self.x == self.goal_x and self.y == self.goal_y:
            return True 
        
        view = self.battleground.get_view(self.x,self.y,True)
        
        for x_off in [-1,1]:
            new_x = x_off + self.x 
            if 0 <= new_x < len(view) and view[new_x][self.y] == 0:
                self.x += x_off 
                if self.dfs(debug):
                    return True 
                self.x -= x_off 
                self.inc_moves(debug)
        
        for y_off in [-1,1]:
            new_y = y_off + self.y 
            if 0 <= new_y < len(view[0]) and view[self.x][new_y] == 0:
                self.y += y_off 
                if self.dfs(debug):
                    return True 
                self.y -= y_off 
                self.inc_moves(debug)

        return False 

    def inc_moves(self, debug = False):
        if debug:
            sleep(.2)
            print(self)
            print("\n\n")
        self.moves += 1
