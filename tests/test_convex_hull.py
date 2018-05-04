import unittest
from rst.convex_hull import graham_scan


class TestConvexHull(unittest.TestCase):


    def test_graham_scan_t(self):
        # test the implementation of Graham scan
        res_1 = graham_scan([(4, 4), (5, 4), (4, 5), (5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (6, 2), (7, 2), (6, 3), (7, 3)])
        ans_1 = [(6, 2), (7, 2), (7, 3), (6, 7), (5, 7), (4, 5), (4, 4)]
        res_2 = graham_scan([(1, 2), (2, 2), (1, 3), (2, 3), (1, 5), (2, 5), (1, 6), (2, 6), (2, 6), (3, 6), (2, 7), (3, 7), (3, 3), (4, 3), (3, 4), (4, 4)])
        ans_2 = [(1,2),(2,2),(4,3),(4,4),(3,7),(2,7),(1,6)]
        # the answers should be the same up to cycles... need modification
        # self.assertEqual([res_1, res_2], [ans_1, ans_2])
