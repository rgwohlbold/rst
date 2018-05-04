import unittest
from rst.battleground import Battleground
from rst.robot import Robot


class TestRobot(unittest.TestCase):

    def test_robot(self):
        terrain = [[0,0],
                   [0,0]]
        battleground = Battleground(terrain=terrain)
        robot = Robot(battleground)
        self.assertTrue(robot.dfs())
        self.assertEqual(robot.moves, 2)

        robot = Robot(battleground)
        self.assertTrue(robot.follow_left())
        self.assertTrue(robot.moves, 2)

