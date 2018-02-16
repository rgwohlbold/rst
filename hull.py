from math import atan, pi


# Three points are a counter-clockwise turn if ccw > 0, clockwise if
# ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
# gives twice the signed  area of the triangle formed by p1, p2 and p3.
def ccw(p1, p2, p3):
    """
    Return if points form a counter-clockwise triangle
    :param p1: Point(x,y) 1
    :param p2: Point(x,y) 2
    :param p3: Point(x,y) 3
    :return: >0 if counter-clockwise, <0 if clockwise, =0 if colinear
    """
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])


def angle(p1, p2):
    """
    Compute the angle from a point over another one to the x-axis
    :param p1: Point (x,y) on which the angle starts
    :param p2: Point (x,y) over which the angle goes
    :return: Angle in degrees
    """
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0:
        if dy == 0:
            return 0
        return 90
    alpha = atan(dy / dx) * 180 / pi
    if alpha < 0:
        alpha = 180 - alpha
    return alpha


def graham_scan(points):
    """
    Return convex hull of a list of points using Graham Scan.
    :param points: List of points (x,y)
    :return: List of vertices of the convex hull (x,y) in counter-clockwise order
    """

    # Find point with smallest y coordinate
    # If two points have equal y coordinates, select the one with the lower x-coordinate
    smallest = points[0]
    for p in points:
        if p[1] < smallest[1]:
            smallest = p
        elif p[1] == smallest[1]:
            if p[0] < smallest[0]:
                smallest = p

    # Sort points by angle over smallest to x-axis
    points.sort(key=lambda x: angle(x, smallest))

    # Our stack
    hull = [smallest, points[1]]
    i = 2
    while i < len(points):
        # If the last points and the new point form a counter-clockwise triangle,
        # we need the last point. Therefore, push the new point
        if ccw(hull[-2], hull[-1], points[i]) > 0 or len(hull) == 2:
            hull.append(points[i])
            i += 1
        # If the two last points and the new point don't form a counter-clockwise triangle,
        # the we don't need the last point
        else:
            hull.pop()
    return hull


