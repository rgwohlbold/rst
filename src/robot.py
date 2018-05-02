import copy 
from display import get_display
from time import sleep 

class Robot:
    
    def __init__(self, battleground, start = (0,0), goal = None):
        self.x = start[0]
        self.y = start[1]
        self.battleground = battleground 
        self.start_x = start[0]
        self.start_y = start[1]
        if goal == None:
            self.goal_x = battleground.m - 1
            self.goal_y = battleground.n - 1
        else:
            self.goal_x = goal[0]
            self.goal_y = goal[1]
        self.moves = 0
   
    # string method, returns the battlefield with the robot marked on it.
    def __str__(self):
        arr = self.battleground.get_view()
        arr[self.x][self.y] = -1
        return get_display(arr) 

    # depth first search on the battleground
    def dfs(self, debug = False, visited = None):
         
        if visited == None:
            visited = [[False for x in range(self.battleground.n)] for y in range(self.battleground.m)]
        
        visited[self.x][self.y] = True
        
        if self.x == self.goal_x and self.y == self.goal_y:
            return True 
        
        view = self.battleground.get_view(self.x,self.y,True)
        
        for x_off in [-1,1]:
            new_x = x_off + self.x 
            if 0 <= new_x < len(view) and view[new_x][self.y] == 0 and not visited[new_x][self.y]:
                self.x += x_off 
                self.inc_moves(debug)
                if self.dfs(debug, visited):
                    return True 
                self.x -= x_off 
                self.inc_moves(debug)
        
        for y_off in [-1,1]:
            new_y = y_off + self.y 
            if 0 <= new_y < len(view[0]) and view[self.x][new_y] == 0 and not visited[self.x][new_y]:
                self.y += y_off 
                self.inc_moves(debug)
                if self.dfs(debug, visited):
                    return True 
                self.y -= y_off 
                self.inc_moves(debug)
                
        return False 
    
    # follow left algorithm for solving the maze, it is generalized for right or left,
    # @param direction should only be 1 or -1, any other numbers will cause strange behavior.
    # @param state, don't change this variable or some edge cases will be marked as
    def follow_side(self, debug = False, state = 0, direction = 1):
        # represents the movements of different states.
        def get_coord(state, x = self.x, y = self.y):
            #        up    left   down   right
            wheel = [[0,1],[-1,0],[0,-1],[1,0]]
            state = (state + 4) % 4
            ret = wheel[state]
            ret[0] += x
            ret[1] += y
            return ret
        
        # its solved
        if self.x == self.goal_x and self.y == self.goal_y:
            return True

        # isn't solveable
        if self.x == self.start_x and self.y == self.start_y and self.moves != 0 and state == 0:
            return False 

        state = (state + 4) % 4
        view = self.battleground.get_view(self.x, self.y, True)
        # if the block beneath me is open, move down, else if it is closed, if the front is open go forward, else turn up.
        # 'beneath' x and y
        bx, by = get_coord(state + direction) 
        if (self.in_bounds(bx, by) and view[bx][by] == 0):
            self.x = bx 
            self.y = by
            state += direction
            self.inc_moves(debug)
        else:
            # 'forward' x and y
            fx, fy = get_coord(state)
            if (self.in_bounds(fx, fy) and view[fx][fy] == 0):
                self.x = fx
                self.y = fy
                self.inc_moves(debug)
            else:
                state -= direction
        return self.follow_side(debug, state,direction)

    # follow_side call for a follow left algorithm
    def follow_left(self, debug = False):
        return self.follow_side(debug, 0, 1)

    # follow_side call for a follow right algorithm
    def follow_right(self, debug = False):
        return self.follow_side(debug, 0, -1)

    # easily allows printing out the battleground when moving
    def inc_moves(self, debug = False):
        if debug:
            sleep(.2)
            print(self)
            print("\n\n")
        self.moves += 1
    
    # is the given coordinate in bounds of the battlefield
    def in_bounds(self, x, y):
        return -1 < y < self.battleground.n and -1 < x < self.battleground.m
