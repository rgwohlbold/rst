"""
Convex hull algorithm by Tenniel

In this algorithm, we assume that all coordinates are in the first quadrant, because the (row index, column index)
coordinate in a 2d array can be perfectly interpreted as (x, y) in the first quadrant. I believe there's an isomorphism.

"""
from scipy.spatial import ConvexHull


def get_all_vertices(squares):
    """
    :param squares: list of coordinates that represent the squares' lower-left
    :return: vertices: list of all vertices of all squares
    """
    verts = []
    for x, y in squares:
        verts.extend([(x, y), (x+1, y), (x, y+1), (x+1, y+1)])
    return verts


def ccw(p1, p2, p3):
    """
    Return if points form a counter-clockwise triangle
    :param p1: Point(x,y) 1
    :param p2: Point(x,y) 2
    :param p3: Point(x,y) 3
    :return: >0 if counter-clockwise, <0 if clockwise, =0 if colinear
    """
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])


"""
import hull
from copy import deepcopy

ce1 = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3), (1, 0), (2, 0), (1.5, 0), (1.1, 0)]
# counter-example to the naive implementation of Graham scan
# the problem occurs when the first few points are all collinear
# visualize the dots on desmos.com, etc. to see the problem

print(graham_scan(deepcopy(ce1)))
print(hull.graham_scan(deepcopy(ce1)))
"""


def graham_scan(points):
    return [points[v] for v in ConvexHull(points).vertices]


# print(graham_scan())
# dat_1 = [(4, 4), (5, 4), (4, 5), (5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (6, 2), (7, 2), (6, 3), (7, 3)]
# ans_1 = [(6, 2), (7, 2), (7, 3), (6, 7), (5, 7), (4, 5), (4, 4)]
# hull_1 = ConvexHull(dat_1)
# print(hull_1.points)
# print([dat_1[v] for v in hull_1.vertices])


