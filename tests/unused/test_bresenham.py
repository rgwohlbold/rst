import unittest
from rst.unused.bresenham import draw_line


class TestBresenham(unittest.TestCase):

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

