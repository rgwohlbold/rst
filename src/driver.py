from robot  import Robot
from display import display 
from battleground import Battleground
view = [
    [1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 4, 1, 2, 4, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 4, 1, 1],
    [1, 2, 2, 4, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 3, 1, 1, 1, 2],
    [0, 1, 1, 1, 1, 1, 3, 1, 1],
    [0, 1, 3, 1, 1, 2, 1, 1, 1],
    [1, 0, 2, 0, 1, 2, 1, 1, 1]]

ground = Battleground(view)
robot = Robot(ground)
robot.dfs(debug=False,gui=True)