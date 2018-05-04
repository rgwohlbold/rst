import unittest
from rst.battleground import Battleground
from rst.robot import Robot


class TestRobot(unittest.TestCase):

    small_terrain = [
        [0,0],
        [0,0]
    ]

    empty_terrain = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]

    # Currently failing to follow_side
    blocked_terrain = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [3,3,3,3,3,3,3],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ]

    test_table = [
        {
            "terrain": small_terrain,
            "goal": None,
            "solvable": True,
            "moves_left": 2,
            "moves_right": 2
        },
        {
            "terrain": small_terrain,
            "goal": (1,0),
            "solvable": True,
            "moves_left": 3,
            "moves_right": 1,
        },
        {
            "terrain": empty_terrain,
            "goal": None,
            "solvable": True,
            "moves_left": 12,
            "moves_right": 12
        },
        {
            "terrain": empty_terrain,
            "goal": (6,0),
            "solvable": True,
            "moves_left": 18,
            "moves_right": 6,
        },
        {
            "terrain": blocked_terrain,
            "goal": None,
            "solvable": False,
            "moves_left": 16,
            "moves_right": 16,
        }
    ]

    def test_robot(self):

        for entry in TestRobot.test_table:
            if entry["goal"] is None and entry["solvable"]:
                goal = (len(entry["terrain"]) - 1, len(entry["terrain"]) - 1)
            elif entry["goal"] is None:
                goal = (0,0)
            else:
                goal = entry["goal"]

            battleground = Battleground(terrain=entry["terrain"])
            robot = Robot(battleground, goal=entry["goal"])
            self.assertEqual(robot.dfs(), entry["solvable"])
            self.assertEqual(goal, (robot.x, robot.y))

            battleground = Battleground(terrain=entry["terrain"])
            robot = Robot(battleground, goal=entry["goal"])
            self.assertEqual(robot.follow_left(), entry["solvable"])
            self.assertEqual(robot.moves, entry["moves_left"])
            self.assertEqual(goal, (robot.x, robot.y))

            battleground = Battleground(terrain=entry["terrain"])
            robot = Robot(battleground, goal=entry["goal"])
            self.assertEqual(robot.follow_right(), entry["solvable"])
            self.assertEqual(robot.moves, entry["moves_right"])
            self.assertEqual(goal, (robot.x, robot.y))

