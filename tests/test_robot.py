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

    test_table = [
        {
            "terrain": small_terrain,
            "moves_left": 2,
            "moves_right": 2,
            "solvable": True
        },
        {
            "terrain": empty_terrain,
            "moves_left": 12,
            "moves_right": 12,
            "solvable": True
        }

    ]

    def test_robot(self):

        for entry in TestRobot.test_table:
            battleground = Battleground(terrain=entry["terrain"])
            robot = Robot(battleground)
            self.assertEqual(robot.dfs(), entry["solvable"])

            self.assertEqual(robot.dfs(), entry["solvable"])
            battleground = Battleground(terrain=entry["terrain"])
            robot = Robot(battleground)
            self.assertEqual(robot.follow_right(), entry["solvable"])
            self.assertEqual(robot.moves, entry["moves_left"])

            battleground = Battleground(terrain=entry["terrain"])
            robot = Robot(battleground)
            self.assertEqual(robot.follow_right(), entry["solvable"])
            self.assertEqual(robot.moves, entry["moves_right"])

