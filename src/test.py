import unittest
from hull import graham_scan
from interpolate import interpolate
from battleground import Battleground


class TestEverything(unittest.TestCase):

    def test_init(self):
        pass

    def test_convex_hull(self):
        points = [(0, -2), (0, 0), (-1, 0), (1, 2), (3, 0), (1, 5)]
        res = graham_scan(points)
        self.assertEqual(res, [(0, -2), (3, 0), (1, 5), (-1, 0)])

    def test_interpolate_1(self):
        points = [(0, -2), (3, 0), (1, 5), (-1, 0)]
        self.assertEqual(interpolate(points),
                         [(( 0.5, -2.5), ( 3.5, -0.5)),
                          (( 3.5,  0.5), ( 1.5,  5.5)),
                          (( 0.5,  5.5), (-1.5,  0.5)),
                          ((-1.5, -0.5), (-0.5, -2.5))])

    def test_interpolate_2(self):
        points = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        self.assertEqual(interpolate(points),
                         [(( 0.5, -2.5), ( 2.5, -0.5)),
                          (( 2.5,  0.5), ( 0.5,  2.5)),
                          ((-0.5,  2.5), (-2.5,  0.5)),
                          ((-2.5, -0.5), (-0.5, -2.5))])

    def test_interpolate_3(self):
        points = [(0, 0), (2, 0), (2, 2), (0, 2)]
        self.assertEqual(interpolate(points),
                         [(( 0.5, -0.5), ( 2.5, -0.5)),
                          (( 2.5,  0.5), ( 2.5,  1.5)),
                          (( 2.5,  2.5), ( 0.5,  2.5)),
                          ((-0.5,  2.5), (-0.5,  0.5))])

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

        b1 = Battleground()
        b1._init_from_terrain_and_fog(terrain, fog)
        self.assertEqual(b1.get_view(i1=-1, j1=-1, interfere=False, birdseye=True), view)

if __name__ == "__main__":
    unittest.main()
