from output.renderer import Renderer


class ConsolePlain(Renderer):

    DISPLAYMAP = {
        # robot
        -1: "=",
        # explored
        0: "_",
        # fog
        1: "#",
        # chasm
        2: "O",
        # mountains
        3: "^",
        4: "^",
        5: "^",
        6: "^",
        7: "+",
        8: "+",
        9: "+"
    }

    def render(self, terrain):
        print(ConsolePlain.get_display(terrain),"\n\n")

    @staticmethod
    def get_display(terrain):
        ret = ""
        for row in terrain:
            for tile in row:
                ret += ConsolePlain.DISPLAYMAP[tile] + " "
            ret += "\n"
        return ret
