import unittest
from battleground import Battleground
from util import redirect_stdout


class TestBattleground(unittest.TestCase):

    view1 = [
        [1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 4, 1, 2, 4, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 4, 1, 1],
        [1, 2, 2, 4, 1, 1, 1, 1, 2],
        [1, 1, 1, 1, 3, 1, 1, 1, 2],
        [0, 1, 1, 1, 1, 1, 3, 1, 1],
        [0, 1, 3, 1, 1, 2, 1, 1, 1],
        [1, 0, 2, 0, 1, 2, 1, 1, 1]]

    fog1 = [
        [1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 1]]

    terrain1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 4, 2, 4, 4, 0, 0],
        [0, 0, 4, 2, 4, 4, 4, 0, 0],
        [0, 2, 2, 4, 4, 4, 0, 0, 2],
        [0, 0, 0, 3, 3, 3, 0, 0, 2],
        [0, 0, 3, 3, 3, 3, 3, 0, 0],
        [0, 0, 3, 3, 3, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 2, 0, 0, 0]]

    repr1 = """
_ _ _ _ _ _ _ _ _ 
_ _ ^ ^ O ^ ^ _ _ 
_ _ ^ O ^ ^ ^ _ _ 
_ O O ^ ^ ^ _ _ O 
_ _ _ ^ ^ ^ _ _ O 
_ _ ^ ^ ^ ^ ^ _ _ 
_ _ ^ ^ ^ O _ _ _ 
_ _ O _ _ O _ _ _ 
"""

    test_init_table = [
        {
            "view": view1,
            "fog": fog1,
            "terrain": terrain1,
            "from": "view",
            "repr": repr1
        },
        {
            "view": view1,
            "fog": fog1,
            "terrain": terrain1,
            "from": "fog+terrain",
            "repr": repr1
        },
        {
            "from": "dimensions",
            "m": 3,
            "n": 5,
        },
        {
            "from": "dimensions",
            "m": 7,
            "n": 9,
        },
        {
            "from": "dimensions",
            "m": -1,
            "n": 3,
            "exception": ValueError()
        },
        {
            "from": "dimensions",
            "m": 7,
            "n": -478,
            "exception": ValueError()
        },
        {
            "from": "nothing",
            "exception": RuntimeError()
        },
    ]

    def test_initialization(self):
        for entry in TestBattleground.test_init_table:
            exception = None
            try:
                if entry["from"] == "view":
                    battleground = Battleground(view=entry["view"])
                    self.assertEqual(battleground.fog, entry["fog"])
                    self.assertEqual(battleground.terrain, entry["terrain"])
                elif entry["from"] == "fog+terrain":
                    battleground = Battleground(terrain=entry["terrain"], fog=entry["fog"])
                    self.assertEqual(battleground.get_view(), entry["view"])
                elif entry["from"] == "dimensions":
                    battleground = Battleground(m=entry["m"], n=entry["n"])
                    view = battleground.get_view()
                    self.assertEqual(len(view), entry["m"])
                    for column in view:
                        self.assertEqual(len(column), entry["n"])
                    if entry.get("fog") is not None:
                        self.assertEqual(battleground.fog, entry["fog"])
                elif entry["from"] == "nothing":
                    battleground = Battleground()
                else:
                    raise RuntimeError("invalid test case")

                if entry.get("repr") is not None:
                    with redirect_stdout() as file:
                        print(battleground)
                    with open(file, 'r') as f:
                        self.assertEqual(f.read().strip(), entry["repr"].strip())

            except Exception as e:
                if e.__class__ != entry.get("exception").__class__:
                    raise e
                exception = e
            finally:
                self.assertEqual(entry.get("exception").__class__, exception.__class__)


