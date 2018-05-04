import unittest
from rst.battleground import Battleground
from util import redirect_stdout


class TestRobot(unittest.TestCase):

    def test_battleground_1(self):
        view = [
            [1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 4, 1, 2, 4, 1, 1, 1],
            [1, 1, 1, 2, 1, 1, 4, 1, 1],
            [1, 2, 2, 4, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 3, 1, 1, 1, 2],
            [0, 1, 1, 1, 1, 1, 3, 1, 1],
            [0, 1, 3, 1, 1, 2, 1, 1, 1],
            [1, 0, 2, 0, 1, 2, 1, 1, 1]]
        fog = [
            [1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1],
            [0, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 1, 1]]
        # TODO: we interpret 2 surrounded by 3s or 4s as ravines surrounded by mountains, so the 2s in the terrain shall
        # TODO: remain after interpolation.
        terrain = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 4, 4, 2, 4, 4, 0, 0],
            [0, 0, 4, 2, 4, 4, 4, 0, 0],
            [0, 2, 2, 4, 4, 4, 0, 0, 2],
            [0, 0, 0, 3, 3, 3, 0, 0, 2],
            [0, 0, 3, 3, 3, 3, 3, 0, 0],
            [0, 0, 3, 3, 3, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 2, 0, 0, 0]]

        # b1 = Battleground()
        # self.assertEqual(b1.get_view(i1=-1, j1=-1, interfere=False, birdseye=True), view)

    def test_battleground_2(self):
        view = [
            [1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 4, 1, 2, 4, 1, 1, 1],
            [1, 1, 1, 2, 1, 1, 4, 1, 1],
            [1, 2, 2, 4, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 3, 1, 1, 1, 2],
            [0, 1, 1, 1, 1, 1, 3, 1, 1],
            [0, 1, 3, 1, 1, 2, 1, 1, 1],
            [1, 0, 2, 0, 1, 2, 1, 1, 1]]
        fog = [
            [1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1],
            [0, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 1, 1]]
        # TODO: we interpret 2 surrounded by 3s or 4s as ravines surrounded by mountains, so the 2s in the terrain shall
        # TODO: remain after interpolation.
        terrain = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 4, 4, 2, 4, 4, 0, 0],
            [0, 0, 4, 2, 4, 4, 4, 0, 0],
            [0, 2, 2, 4, 4, 4, 0, 0, 2],
            [0, 0, 0, 3, 3, 3, 0, 0, 2],
            [0, 0, 3, 3, 3, 3, 3, 0, 0],
            [0, 0, 3, 3, 3, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 2, 0, 0, 0]]
        b2 = Battleground(view=view)
        self.assertEqual(b2.fog, fog)
        self.assertEqual(b2.terrain, terrain)

    def test_test(self):

        with redirect_stdout() as buffer:
            view = [
                [1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 4, 1, 2, 4, 1, 1, 1],
                [1, 1, 1, 2, 1, 1, 4, 1, 1],
                [1, 2, 2, 4, 1, 1, 1, 1, 2],
                [1, 1, 1, 1, 3, 1, 1, 1, 2],
                [0, 1, 1, 1, 1, 1, 3, 1, 1],
                [0, 1, 3, 1, 1, 2, 1, 1, 1],
                [1, 0, 2, 0, 1, 2, 1, 1, 1]]
            b2 = Battleground(view=view)
            print(b2)
            s = buffer.uncolorized()
        self.assertEqual(s,
"""_ _ _ _ _ _ _ _ _ 
_ _ ^ ^ O ^ ^ _ _ 
_ _ ^ O ^ ^ ^ _ _ 
_ O O ^ ^ ^ _ _ O 
_ _ _ ^ ^ ^ _ _ O 
_ _ ^ ^ ^ ^ ^ _ _ 
_ _ ^ ^ ^ O _ _ _ 
_ _ O _ _ O _ _ _ 

""")
