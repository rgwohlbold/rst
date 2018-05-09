import unittest
from unused.bresenham import draw_line


class TestBresenham(unittest.TestCase):

    bresenham_table = [
        {
            "input": [(0, 0), (0, 3)],
            "output": [(0, 0),(0, 1),(0, 2),(0, 3)]
        },
        {
            "input": [(5, 3), (2, 1)],
            "output": [(2, 1), (3, 2), (4, 2), (5, 3)]
        },
        {
            "input": [(2, 1), (5, 3)],
            "output": [(2, 1), (3, 2), (4, 2), (5, 3)]
        },
        {
            "input": [(1, 0), (10, 5)],
            "output": [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2),(6, 3), (7, 3), (8, 4), (9, 4), (10, 5)]
        },
        {
            "input": [(3, 5), (1, 2)],
            "output": [(1, 2), (2, 3), (2, 4), (3, 5)]
        },
    ]

    def test_bresenham_output(self):
        for entry in TestBresenham.bresenham_table:
            input = entry["input"]
            self.assertEqual(draw_line(input[0], input[1]), entry["output"])


