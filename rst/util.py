import os
import atexit
import colorama
import tempfile
from contextlib import contextmanager
from contextlib import redirect_stdout as do_redirect

colorama.init()
escapes = list(colorama.Fore.__dict__.values()) + list(colorama.Back.__dict__.values())

@contextmanager
def redirect_stdout():
    def uncolorized(self):
        return uncolorize(self.getvalue())

    name = tempfile.mktemp('out', 'txt')
    atexit.register(os.remove, name)

    with open(name, 'w') as f:
        with do_redirect(f):
            yield name
    with open(name, 'r') as f:
        content = f.read()
    with open(name, 'w') as f:
        f.write(uncolorize(content))



def uncolorize(s):
    for escape in escapes:
        s = s.replace(escape, "")
    return s

def empty(m, n):
    return [[0 for x in  range(n)] for y in range(m)]

def empty_repr(m, n):
    return ("_ " * n + "\n") * m

def battleground_from_file(path, delimiter = " "):
    terrain = []
    for line in open(path):
        # remove newlines and trailing spaces
        line   = line.strip()
        # split along the delimeter and remove empty strings
        blocks = filter(lambda x : x != "", line.split(delimiter))
        # turn the strings to ints
        nums   = list(map(int, blocks))
        # add the new row to the terrain
        terrain.append(nums)
    # return the constructed terrain
    return terrain

