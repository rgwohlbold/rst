"""
Convex hull algorithm by Tenniel

In this algorithm, we assume that all coordinates are in the first quadrant, because the (row index, column index)
coordinate in a 2d array can be perfectly interpreted as (x, y) in the first quadrant. I believe there's an isomorphism.

"""


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


def graham_scan(points):
    # select the point with the lowest y coordinate
    # if several points have the same y coordinate, select the point with the lowest x coordinate
    lowest = min(points, key=lambda p: (p[1], p[0]))
    points.remove(lowest)

    # sort the rest of the points (p) by the angle theta between the vector (from lowest to p) and the x-axis
    # we know: 0 <= theta <= pi
    # cos(theta) = dot_product(p-lowest, [1,0]) / (||p|| * 1) = (p[0]-lowest[0])/(p[0]**2 + p[1]**2)**.5
    # cos(x) is monotonically decreasing with respect to x in the interval [0, pi]
    # as a result, sorting by lambda p: (-p[0]/(p[0]**2 + p[1]**2)**.5 is equivalent to sorting by theta
    points.sort(key=lambda p: -p[0]/(p[0]**2 + p[1]**2)**.5)

    # initialize the convex hull
    hull = [lowest, points.pop(0)]

    while points:
        is_ccw = ccw(hull[-2], hull[-1], points[0])
        if is_ccw == 0:  # three points are collinear
            # select the point with the maximum distance from hull[-2]
            hull[-1] = max([hull[-1], points.pop(0)], key=lambda p: (p[0]-hull[-2][0])**2+(p[1]-hull[-2][1])**2)
        elif is_ccw > 0 or len(hull) == 2:
            hull.append(points.pop(0))
        else:
            hull.pop()
    return hull

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
