import unittest
from hull import graham_scan
from interpolate import interpolate

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

if __name__ == "__main__":
    unittest.main()
