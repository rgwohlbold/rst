"""
polygon algorithms by Tenniel

see description for crossing number and winding number at: http://geomalgorithms.com/a03-_inclusion.html

"""


def _is_left(p0, p1, p2):
    """
    :return:
    >0 for p2 is left of the line through P0 and P1
    =0 for p2 is on the line
    <0 for p2 is right of the line
    """
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


def crossing_number(p, verts):
    cn = 0  # crossing number
    n = len(verts)  # number of vertices
    for i in range(n):
        if verts[i][1] <= p[1] < verts[(i+1)%n][1] or verts[(i+1)%n][1] <= p[1] < verts[i][1]:  # upward and downward crossing
            # compute the actual edge-ray intersect x-coordinate
            vt = (p[1] - verts[i][1]) / (verts[(i+1)%n][1] - verts[i][1])
            if p[0] < verts[i][0] + vt * (verts[(i+1)%n][0] - verts[i][0]):
                cn += 1
    return cn


def winding_number(p, verts):
    wn = 0  # winding number
    n = len(verts)
    for i in range(n):
        if verts[i][1] <= p[1]:
            if verts[(i+1)%n][1] > p[1] and _is_left(verts[i], verts[(i+1)%n], p) >= 0:  # upward crossing on p's left
                wn += 1
        else:
            if verts[(i+1)%n][1] <= p[1] and _is_left(verts[i], verts[(i+1)%n], p) < 0:
                wn -= 1
    return wn


def interpolate(m, n, verts, use_wn=True):
    """
    :param m: the maximum value of x-axis, 0 <= x <= m
    :param n: the maximum value of y-axis, 0 <= y <= n
    :param verts: the vertices of the convex polygon
    :param use_wn: use winding number (rather than crossing number) to determine if a point is in the polygon
    :return: a m*n boolean matrix

    TODO: prove these conjectures if possible
    conjecture 1: it is impossible for a convex lattice polygon to cover more than 50% of a lattice square's area
        without covering its center (the ENTIRE interpolate function relies on this conjecture)
    conjecture 2: the area of a convex polygon with more than n sides (I suspect that n=3) is greater than half of its
        bounding box's area (used to speed up calculation)

    """

    ret = [[False for c in range(n)] for r in range(m)]
    # create a circumscribed rectangle
    r_range = range(min(v[0] for v in verts), max(v[0] for v in verts))
    c_range = range(min(v[1] for v in verts), max(v[1] for v in verts))
    for r in r_range:
        for c in c_range:
            ret[r][c] = True
    # only consider the points within the bounding box -> speed up the algorithm
    for r in r_range:
        for c in c_range:
            x, y = r + 0.5, c + 0.5  # the center point
            is_outside = (winding_number((x, y), verts) == 0) if use_wn else (crossing_number((x, y), verts) % 2 == 0)
            if is_outside:
                ret[r][c] = False
            else:
                break
        for c in reversed(c_range):
            x, y = r + 0.5, c + 0.5  # the center point
            is_outside = (winding_number((x, y), verts) == 0) if use_wn else (crossing_number((x, y), verts) % 2 == 0)
            if is_outside:
                ret[r][c] = False
            else:
                break
    return ret