import unittest
from hull import graham_scan as graham_scan_r
from convex_hull import graham_scan as graham_scan_t
from battleground import Battleground
from polygon import crossing_number, winding_number
from bresenham import draw_line
from robot import Robot

class TestEverything(unittest.TestCase):
    def test_init(self):
        pass

    def test_point_in_polygon(self):
        square = ((0, 0), (10, 0), (10, 10), (0, 10))

        self.assertEqual([crossing_number((0, 6), square),
                          winding_number((0, 6), square),
                         winding_number((50**.5, 50**.5), ((0,0),(10,0),(10,10)))],
                         [1, 1, 1])

    def test_graham_scan_t(self):
        # test the implementation of Graham scan
        gs = graham_scan_t
        res_1 = gs([(4, 4), (5, 4), (4, 5), (5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (6, 2), (7, 2), (6, 3), (7, 3)])
        ans_1 = [(6, 2), (7, 2), (7, 3), (6, 7), (5, 7), (4, 5), (4, 4)]
        res_2 = gs([(1, 2), (2, 2), (1, 3), (2, 3), (1, 5), (2, 5), (1, 6), (2, 6), (2, 6), (3, 6), (2, 7), (3, 7), (3, 3), (4, 3), (3, 4), (4, 4)])
        ans_2 = [(1,2),(2,2),(4,3),(4,4),(3,7),(2,7),(1,6)]
        # the answers should be the same up to cycles... need modification
        # self.assertEqual([res_1, res_2], [ans_1, ans_2])

    def test_convex_hull(self):
        points = [(0, -2), (0, 0), (-1, 0), (1, 2), (3, 0), (1, 5)]
        res = graham_scan_r(points)
        self.assertEqual(res, [(0, -2), (3, 0), (1, 5), (-1, 0)])

    def test_bresenham_1(self):
        points = [(0, 0), (0, 3)]
        self.assertEqual(draw_line(points[0], points[1]),
                         [(0, 0),(0, 1),(0, 2),(0, 3)])

    def test_bresenham_2(self):
        points = [(5, 3), (2, 1)]
        self.assertEqual(draw_line(points[0], points[1]),
                         [(2, 1), (3, 2), (4, 2), (5, 3)])

    def test_bresenham_3(self):
        points = [(1, 0), (10, 5)]
        self.assertEqual(draw_line(points[0], points[1]),
                         [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2),
                          (6, 3), (7, 3), (8, 4), (9, 4), (10, 5)])

    def test_robot(self):
        terrain = [[0,0],
                   [0,0]]
        battleground = Battleground(terrain)
        robot = Robot(battleground, debug = True)
        self.assertTrue(robot.run())
        self.assertEqual(robot.moves(), 2)

        robot = Robot(battleground, debug = True)
        self.assertTrue(robot.run())
        self.assertTrue(robot.moves(), 2)

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
        # b1._init_from_terrain_and_fog(terrain, fog)
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
        b2 = Battleground(view)
        self.assertEqual(b2.fog, fog)
        # for row in b2.terrain:
        #     print(row)
        self.assertEqual(b2.terrain, terrain)


if __name__ == "__main__":
    unittest.main()
