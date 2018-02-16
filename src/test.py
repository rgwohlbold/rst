import unittest
from hull import graham_scan

class TestEverything(unittest.TestCase):

    def test_init(self):
        pass

    def test_convex_hull(self):
        points = [(0, -2), (0, 0), (-1, 0), (1, 2), (3, 0), (1, 5)]
        res = graham_scan(points)
        self.assertEquals(res, [(0, -2), (3, 0), (1, 5), (-1, 0)])





if __name__ == "__main__":
    unittest.main()
