from colorama import init
from colorama import Fore, Back, Style

init()

displaymap = {
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


def display(terrain):
    print(get_display(terrain),"\n\n")

def get_display(terrain):
    ret = ""
    for row in terrain:
        for tile in row:
            ret += displaymap[tile] + " "
        ret += "\n"
    ret += Fore.RESET
    return ret
