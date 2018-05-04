import unittest
from rst.polygon import crossing_number, winding_number


class TestPolygon(unittest.TestCase):
    def test_point_in_polygon(self):
        square = ((0, 0), (10, 0), (10, 10), (0, 10))

        self.assertEqual([crossing_number((0, 6), square),
                          winding_number((0, 6), square),
                          winding_number((50**.5, 50**.5), ((0,0),(10,0),(10,10)))],
                         [1, 1, 1])

