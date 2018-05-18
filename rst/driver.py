from robot import Robot
from battleground import Battleground
import argparse
import logging as log

view = [
    [1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 4, 1, 2, 4, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 4, 1, 1],
    [1, 2, 2, 4, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 3, 1, 1, 1, 2],
    [0, 1, 1, 1, 1, 1, 3, 1, 1],
    [0, 1, 3, 1, 1, 2, 1, 1, 1],
    [1, 0, 2, 0, 1, 2, 1, 1, 1]]


search_choices = list(map(lambda x: x[7:].lower(), filter(lambda x: x.startswith("SEARCH_"), Robot.__dict__.keys())))
display_choices = list(map(lambda x: x[8:].lower(), filter(lambda x: x.startswith("DISPLAY_"), Robot.__dict__.keys())))

parser = argparse.ArgumentParser()
#parser.add_argument("-f", "--file", help="load terrain from a file")
parser.add_argument("-o", "--output", help="which output method should be used", action="store", choices=display_choices, default="curses_color")
parser.add_argument("-s", "--search", help="which search to perform", action="store", choices=search_choices, default="follow_left")

args = parser.parse_args()
search = Robot.__dict__["SEARCH_" + args.search.upper()]
output = Robot.__dict__["DISPLAY_" + args.output.upper()]

ground = Battleground(view=view)
robot = Robot(ground, search=search, display=output)
robot.run()
