import copy


class Battleground(object):
    def init_from_matrix(self, mat):
        # TODO: UNFINISHED, SEE INSTRUCTIONS BELOW
        self.m = len(mat)
        self.n = len(mat[0])
        # check input dimensions
        if any(len(mat[i]) != self.n for i in range(self.m)):
            raise ValueError("Shape mismatch: all rows in the terrain matrix should have had equal lengths")

        self.terrain = copy.deepcopy(mat)
        self.fog = [[entry == 1 for entry in row] for row in mat]  # TODO: nothing, this one is done
        # TODO: need to get a complete terrain from mat using a convex hull algorithm

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

    def __str__(self):
        ret = "<RST Battleground Object: Battleground(\n"
        ret += "terrain=[\n"
        for row in self.terrain:
            ret += str(row) + ",\n"
        ret = ret[:-2] + "],\nfog=[\n"
        for row in self.fog:
            ret += str(row) + ",\n"
        ret = ret[:-2] + "])>"
        return ret

    def get_view(self, i1=-1, j1=-1, interfere=True, birdseye=True):
        """
        get a view of the battleground for a robot at (i, j)
        when (i1, j1) == (-1, -1) by default, return a view without the robot
        :param i1: coordinate on axis-0/vertical axis (0-indexed)
        :param j1: coordinate on axis-1/horizontal axis (0-indexed)
        :param interfere: if True, the fog in the 3*3 square around (i, j) on the battleground will be removed
        :param birdseye: if True, everything not covered in fog on the battleground will be revealed;
         otherwise, only the 4 adjacent entries will be revealed, and everything else will be covered in fog.
        :return:
        """

        if birdseye:
            view = copy.deepcopy(self.terrain)  # default view: omniscience
            for i in range(self.m):
                for j in range(self.n):
                    if self.fog[i][j]:  # there is fog in the area
                        view[i][j] = 1
        else:  # birdseye disabled
            view = [[1] * self.n for _ in range(self.m)]  # default view: ignorance

        if i1 >= 0 and j1 >= 0:  # not default -> add information
            # get a list of coordinates for valid surrounding blocks
            neighbors = [(i, j) for j in range(max(j1-1, 0), min(j1+2, self.n)) for i in range(max(i1-1, 0), min(i1+2, self.m))]

            # update the view matrix
            for i, j in neighbors:
                view[i][j] = self.terrain[i][j]

            # update the fog matrix (only if interfere==True)
            if interfere:
                for i, j in neighbors:
                    self.fog[i][j] = False  # clear the fog out of the way

        return view

