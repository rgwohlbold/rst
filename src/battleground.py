import copy
from convex_hull import get_all_vertices, graham_scan
from polygon import interpolate
from colorama import init
from colorama import Fore, Back, Style

init()

displaymap = {
    # explored
    0: Fore.RESET + "_",

    # fog
    1: Fore.RESET + "#",

    # chasm
    2: Fore.RED    + "O",

    # mountains
    3: Fore.GREEN  + "^",
    4: Fore.BLUE   + "^",
    5: Fore.CYAN   + "^",
    6: Fore.YELLOW + "^",
    7: Fore.GREEN  + "+",
    8: Fore.BLUE   + "+",
    9: Fore.CYAN   + "+"
}

DEBUG = False

class Battleground(object):
    def __init__(self, mat):
        self.m = len(mat)
        self.n = len(mat[0])
        self.max_h = max(ent for row in mat for ent in row)  # the maximum height

        # check input dimensions
        if any(len(mat[i]) != self.n for i in range(self.m)):
            raise ValueError("Shape mismatch: all rows in the terrain matrix should have had equal lengths")

        self.terrain = copy.deepcopy(mat)
        self.fog = [[entry == 1 for entry in row] for row in mat]

        # get a complete terrain from mat using a convex hull algorithm
        # get coordinates for each height
        h_coordinates = {h: [] for h in range(3, self.max_h+1)}  # h -> list of coordinates that have height h
        for r in range(self.m):
            for c in range(self.n):
                if mat[r][c] >= 3:
                    h_coordinates[mat[r][c]].append((r, c))

        # fill in the mountains
        for h in h_coordinates:
            hull_verts = graham_scan(get_all_vertices(h_coordinates[h]))  # all vertices of the convex hull
            mask = interpolate(self.m, self.n, hull_verts, use_wn=True)
            if DEBUG:
                print("all coordinates for h={}: ".format(h), get_all_vertices(h_coordinates[h]))
                print("hull coordinates for h={}: ".format(h), hull_verts)
                #print("hull coordinates 1 for h={}: ".format(h), graham_scan_1(get_all_vertices(h_coordinates[h])))
                print("WAIT---Printing mask", h)
                for row in mask:
                    print([int(x) for x in row], end=',\n')
                print('ended')
            # import time
            # time.sleep(1)
            for r in range(self.m):
                for c in range(self.n):
                    if mask[r][c] and self.terrain[r][c] != 2:
                        self.terrain[r][c] = h

        # remove the remaining fog on the terrain
        for r in range(self.m):
            for c in range(self.n):
                if self.terrain[r][c] == 1:
                    self.terrain[r][c] = 0

    def _init_from_terrain_and_fog(self, terrain, fog):

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
        ret = ""
        for row in self.terrain:
            for tile in row:
                ret += displaymap[tile] + " "
            ret += "\n"
        ret += Fore.RESET
        return ret
        # ret = "<RST Battleground Object: Battleground(\n"
        # ret += "terrain=[\n"
        # for row in self.terrain:
        #     ret += str(row) + ",\n"
        # ret = ret[:-2] + "],\nfog=[\n"
        # for row in self.fog:
        #     ret += str(row) + ",\n"
        # ret = ret[:-2] + "])>"
        # return ret

    def get_view(self, i1=-1, j1=-1, interfere=False, birdseye=True):
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
