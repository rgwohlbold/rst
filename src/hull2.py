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


def graham_scan(points):
    lowest = min(points, key=lambda p: (p[1], p[0]))
    
    return lowest


