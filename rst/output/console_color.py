from output.renderer import Renderer
from colorama import init
from colorama import Fore


class ConsoleColor(Renderer):

    def __init__(self):
        init()

        self.displaymap = {
            # robot
           -1: Fore.CYAN + "=",

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

    def render(self, terrain):
        print(self._get_display(terrain),"\n\n")

    def _get_display(self, terrain):
        ret = ""
        for row in terrain:
            for tile in row:
                ret += self.displaymap[tile] + " "
            ret += "\n"
        ret += Fore.RESET
        return ret
