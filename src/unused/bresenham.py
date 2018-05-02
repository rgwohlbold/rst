def plot_low(x0, y0, x1, y1):
    """
    Draws flat gradients where -1 <= dx <= 1 and x0 < x1
    :param x0: First x-coordinate
    :param y0: First y-coordinate
    :param x1: Second x-coordinate
    :param y1: Second y-coordinate
    :return: List of points occupied by the line
    """
    res = []
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2 * dy - dx
    y = y0

    for x in range(x0, x1+1):
        res.append((x, y))
        if D > 0:
            y = y + yi
            D = D - 2 * dx
        D = D + 2 * dy
    return res


def plot_high(x0, y0, x1, y1):
    """
    Draws flat gradients where dx < -1 or dx > 1 and x0 < x1
    :param x0: First x-coordinate
    :param y0: First y-coordinate
    :param x1: Second x-coordinate
    :param y1: Second y-coordinate
    :return: List of points occupied by the line
    """
    res = []
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x0

    for y in range(y0, y1+1):
        res.append((x, y))
        if D > 0:
            x = x + xi
            D = D - 2 * dy
        D = D + 2 * dx
    return res


def draw_line(p0, p1):
    """
    Draw line between two points
    :param p0: First point (x,y)
    :param p1: Second point (x,y)
    :return: List of all points (x,y) occupied by the line
    """
    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            return plot_low(x1, y1, x0, y0)
        else:
            return plot_low(x0, y0, x1, y1)
    else:
        if y0 > y1:
            return plot_high(x1, y1, x0, y0)
        else:
            return plot_high(x0, y0, x1, y1)
