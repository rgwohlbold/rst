import math
import hull


def angle(p1, p2, p3):
    """
    Compute the angle between three points (from p1 over p2 to p3)
    :param p1: Point (x,y) on which the angle starts
    :param p2: Point (x,y) over which the angle goes
    :param p3: Point (x,y) to which the angle goes
    :return: Angle in degrees
    """
    p12 = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    p23 = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
    p13 = math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)

    return math.acos((p12**2 + p23 ** 2 - p13**2) / (2 * p12 * p23)) * 180 / math.pi


def axis_angle(p1, p2, x_axis=True, right=True):
    """
    Angle to an axis
    :param p1: Point (x,y) where the angle starts
    :param p2: Point (x,y) over which the angle goes
    :param x_axis: Which axis to use
    :param right: Which direction to go in
    :return: Angle in degrees
    """
    if x_axis:
        p3 = (p2[0], p2[1] + 10 if right else -10)
    else:
        p3 = (p2[0] + 10 if right else -10, p2[1])
    return angle(p1, p2, p3)


def moves(p):
    """
    List of the possible destinations given a point.
    A destination is an offset of +/- 0.5 in both directions
    :param p: The point
    :return: The list of destinations
    """
    return [(p[0] + 0.5, p[1] + 0.5),
            (p[0] + 0.5, p[1] - 0.5),
            (p[0] - 0.5, p[1] + 0.5),
            (p[0] - 0.5, p[1] - 0.5)]


def rotate(point, move):
    """
    Returns the next destination of a point, given the current one
    in counter-clockwise order.
    :param point: Point (x,y) the destination originates from
    :param move: Current destination
    :return: Next destination
    """
    dx = move[0] - point[0]
    dy = move[1] - point[1]

    if dx > 0 and dy > 0:
        dx = -dx
    elif dx < 0 and dy > 0:
        dy = -dy
    elif dx < 0 and dy < 0:
        dx = -dy
    elif dx > 0 and dy < 0:
        dy = -dy

    return (point[0] + dx, point[1] + dy)

def dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx ** 2 + dy ** 2)

def interpolate(points):
    """
    Given the outer points of a convex hull, calculate the
    lines one has to draw to surround everything.
    The points are not points, but centers of rigid squares.
    One can imagine the process as spanning a rubber band around
    all the outer squares of a polygon.
    :param points: List of points (x,y) of the polygon
    :return: List of 2-tuples of points(x,y) to draw the lines
    """
    # The first point is the bottom left one. The first source is the bottom right one.
    prev = points[0]
    prev_dest = (prev[0] + 0.5, prev[1] - 0.5)
    del points[0]
    # We still need to draw a line to the first point
    points.append(prev)

    # Our lines
    lines = []
    # Calculate angles against y-axis? This is false if we go sideways
    y_axis = False
    # Are angles calculated to the right? (are we going down?)
    right = False

    for p in points:

        # Angle from new point over previous one to current axis
        alpha = axis_angle(p, prev, x_axis=y_axis, right=right)

        # If alpha = 90, we do not change directions and the same vertex is used twice
        if alpha > 90:
            source = prev_dest
        # If alpha <= 90, change directions and use the vertex twice
        else:
            source = rotate(prev, prev_dest)

        # All possible destinations
        dests = moves(p)

        # Choose the one with the smallest angle (on the outside)
        angles = list(map(lambda x: axis_angle(x, prev, y_axis, right=not right), dests))
        # Dest with smallest angle, when angles are equal the one with smallest distance to source
        smallest = min(angles)
        dests_new = []
        for i,a in enumerate(angles):
            if a == smallest:
               dests_new.append(dests[i])
        dest = sorted(dests_new, key=lambda x: dist(x, source))[0]

        if alpha <= 90:
            y_axis = not y_axis
            if not y_axis:
                right = not right

        prev = p
        prev_dest = dest
        lines.append((source, dest))

    return lines