import copy

class Battleground(object):
    def __init__(self, terrain, fog):

        # the size of the battleground (m * n matrix)
        self.m = len(terrain)
        self.n = len(terrain[0])

        # check input dimensions
        if len(fog) != self.m:
            raise ValueError("Shape mismatch: m_fog={} should have been equal to m_terrain={}".format(len(fog), self.m))
        if any(len(terrain[i]) != self.n for i in range(self.m)):
            raise ValueError("Shape mismatch: all rows in the terrain matrix should have had equal lengths")
        if any(len(fog[i]) != self.n for i in range(self.m)):
            raise ValueError("Shape mismatch: all rows in the fog matrix should have had equal lengths")

        self.terrain = terrain
        self.fog = fog

    def get_view(self, i=-1, j=-1, birdseye=True):
        """
        get a view of the battleground for a robot at (i, j)
        when (i, j) == (-1, -1) by default, return a view without the robot
        :param i: coordinate on axis-0/vertical axis (0-indexed)
        :param j: coordinate on axis-1/horizontal axis (0-indexed)
        :param birdseye: if True, everything not covered in fog on the battleground will be revealed;
         otherwise, only the 4 adjacent entries will be revealed, and everything else will be covered in fog.
        :return:
        """

        if birdseye:
            view = copy.deepcopy(self.terrain)
            for i in range(self.m):
                for j in range(self.n):
                    if self.fog[i][j]:  # there is fog in the area
                        view[i][j] = 1
        else:  # birdseye disabled
            view = [[1] * self.n for _ in range(self.m)]

        if i >= 0 and j >= 0:  # not default -> add information
            view[i][j] = self.terrain[i][j]
            if i - 1 >= 0:
                view[i - 1][j] = self.terrain[i][j]  # up
            if i + 1 < self.m:
                view[i + 1][j] = self.terrain[i + 1][j]  # down
            if j - 1 >= 0:
                view[i][j - 1] = self.terrain[i][j - 1]  # left
            if j + 1 < self.n:
                view[i][j + 1] = self.terrain[i][j + 1]  # right
        return view
