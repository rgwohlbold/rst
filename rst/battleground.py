import copy
import random
import itertools
from convex_hull import get_all_vertices, graham_scan
from polygon import interpolate
from output.console_plain import ConsolePlain



DEBUG = False


class Battleground(object):
    def __init__(self, view=None, terrain=None, fog=None, m=None, n=None, fog_rate=None, hill_rates=None, **kwargs):
        if view is not None:
            self._init_from_view(view)
        elif terrain is not None:
            self._init_from_terrain_and_fog(terrain, fog)
        elif m is not None and n is not None:
            # default fog_rate and hill_rates
            fog_rate = 0.6 if fog_rate is None else fog_rate
            hill_rates = [0.2, 0.2] if hill_rates is None else hill_rates
            # please supply parameters:
            # max_h: the maximum height of the mountain
            #
            self._init_from_size(m, n, fog_rate, hill_rates)
        else:
            raise RuntimeError("Trying to create uninitialized battleground")

    def _init_from_view(self, view):
        self.m = len(view)
        self.n = len(view[0])
        self.max_h = max(entry for row in view for entry in row)  # the maximum height

        # check input dimensions
        self._check_valid(view, "input view")

        # initialize terrain and fog
        self.terrain = copy.deepcopy(view)
        self.fog = [[entry == 1 for entry in row] for row in view]

        # find the mountain coordinates
        h_coordinates = {h: [] for h in range(3, self.max_h + 1)}  # h -> list of coordinates that have height h
        for r in range(self.m):
            for c in range(self.n):
                if self.terrain[r][c] >= 3:
                    h_coordinates[self.terrain[r][c]].append((r, c))

        # fill the mountains
        for h in h_coordinates:  # iterate over different heights
            self._fill_mountain_1(h, h_coordinates)

        # remove the remaining fog on the terrain
        for r in range(self.m):
            for c in range(self.n):
                if self.terrain[r][c] == 1:
                    self.terrain[r][c] = 0

    def _fill_mountain_1(self, h, h_coordinates):
        hull_verts = graham_scan(get_all_vertices(h_coordinates[h]))  # all vertices of the convex hull
        mask = interpolate(self.m, self.n, hull_verts, use_wn=True)
        for r in range(self.m):
            for c in range(self.n):
                if mask[r][c] and self.terrain[r][c] != 2:
                    self.terrain[r][c] = h

    def _init_from_terrain_and_fog(self, terrain, fog=None):
        # the size of the battleground (m * n matrix)
        self.m = len(terrain)
        self.n = len(terrain[0])
        self.max_h = max(entry for row in terrain for entry in row)  # the maximum height

        self._check_valid(terrain, "input terrain")

        self.terrain = terrain

        if fog is None:
            # if there is no fog, set fog to 0
            self.fog = [[0] * self.n for _ in range(self.m)]
        else:
            self._check_valid(fog, "input fog")
            self.fog = fog

    def _init_from_size(self, m, n, fog_rate, hill_rates):
        self.m = m
        self.n = n

        self.terrain = [[0] * self.n for _ in range(self.m)]

        self.fog = [[0] * self.n for _ in range(self.m)]
        assert 0.0 <= fog_rate <= 1.0
        # add fog
        for r, c in random.sample(population=list(itertools.product(range(self.m), range(self.n))),
                                  k=int(round(fog_rate * self.m * self.n))):
            self.fog[r][c] = 1

        self._check_valid(self.terrain, "generated terrain")

        # randomly initialize mountains and ravines
        self.max_h = len(hill_rates) + 1
        h_coordinates = {}  # h -> list of coordinates that have height h

        for h in range(2, len(hill_rates) + 2):
            rate = hill_rates[h - 2]
            hills = list(itertools.product(range(self.m), range(self.n)))
            for r, c in random.sample(population=hills, k=int(round(rate * self.m * self.n))):
                self.terrain[r][c] = h
            if h != 2:
                h_coordinates[h] = hills

        # fill the mountains
        for h in h_coordinates:  # iterate over different heights
            self._fill_mountain_1(h, h_coordinates)

    def _check_valid(self, mat, name="input"):
        """
        check whether the input matrix (mat, fog, terrain, etc) is valid (match the dimensions)
        raise a ValueError if invalid.
        """
        if self.m <= 0:
            raise ValueError("self.m must be positive, got {} instead".format(self.m))
        if self.n <= 0:
            raise ValueError("self.n must be positive, got {} instead".format(self.n))

        if len(mat) != self.m:
            raise ValueError("Input Matrix Shape Mismatch: the {} matrix has {} rows, but self.m={}".
                             format(name, len(mat), self.m))
        for i, row in enumerate(mat):
            if len(row) != self.n:
                raise ValueError("Input Matrix Shape Mismatch: the {} matrix has {} columns at row {}, but self.n={}"
                                 .format(name, len(row), i, self.n))

    def __str__(self):
        return ConsolePlain.get_display(self.terrain)

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
            neighbors = [(i, j) for j in range(max(j1 - 1, 0), min(j1 + 2, self.n)) for i in
                         range(max(i1 - 1, 0), min(i1 + 2, self.m))]

            # update the view matrix
            for i, j in neighbors:
                view[i][j] = self.terrain[i][j]

            # update the fog matrix (only if interfere==True)
            if interfere:
                for i, j in neighbors:
                    self.fog[i][j] = False  # clear the fog out of the way

        return view

    # are the given coordinates in bounds or not?
    def in_bounds(self, x, y):
        return -1 < y < self.n and -1 < x < self.m

