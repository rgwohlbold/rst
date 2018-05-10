from robot import Robot
from battleground import Battleground

from searches.follow_right import FollowRight
from searches.follow_left  import FollowLeft
from searches.dfs import DFS

view = [
    [1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 4, 1, 2, 4, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 4, 1, 1],
    [1, 2, 2, 4, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 3, 1, 1, 1, 2],
    [0, 1, 1, 1, 1, 1, 3, 1, 1],
    [0, 1, 3, 1, 1, 2, 1, 1, 1],
    [1, 0, 2, 0, 1, 2, 1, 1, 1]]

ground = Battleground(view=view)

# console, gui or ncurses or output
for search in [DFS, FollowRight, FollowLeft]:
    robot = Robot(ground, search(), display_function=Robot.DISPLAY_COLOR)
    robot.run()
