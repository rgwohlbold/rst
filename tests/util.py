import types
import colorama
import sys
import io
from contextlib import contextmanager

colorama.init()
escapes = list(colorama.Fore.__dict__.values()) + list(colorama.Back.__dict__.values())

@contextmanager
def redirect_stdout():
    def uncolorized(self):
        return uncolorize(self.getvalue())

    buffer = io.StringIO()
    buffer.__setattr__("uncolorized", types.MethodType(uncolorized, buffer))
    sys.stdout = buffer
    yield buffer
    sys.stdout = sys.__stdout__
    buffer.close()


def uncolorize(s):
    for escape in escapes:
        s = s.replace(escape, "")
    return s

def empty(m, n):
    return [[0] * n] * m

def empty_repr(m, n):
    return ("_ " * n + "\n") * m
