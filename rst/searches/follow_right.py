from searches.follow_side import FollowSide

class FollowRight(FollowSide):
    def __init__(self, rob):
        super().__init__(rob, -1)
