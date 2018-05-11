from searches.follow_side import FollowSide

class FollowLeft(FollowSide):
    def __init__(self, rob):
        super().__init__(rob, 1)
