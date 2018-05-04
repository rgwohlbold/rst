import unittest
from rst.unused.hull import graham_scan


class TestHull(unittest.TestCase):

    def test_convex_hull(self):
        points = [(0, -2), (0, 0), (-1, 0), (1, 2), (3, 0), (1, 5)]
        res = graham_scan(points)
        self.assertEqual(res, [(0, -2), (3, 0), (1, 5), (-1, 0)])
