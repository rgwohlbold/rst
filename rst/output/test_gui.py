import unittest
import pygame
from functools import partial
import output.gui as gui


class TestGUI(unittest.TestCase):

    battleground = [
        [1,0,0,0,0,0,0,0,0],
        [0,-1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,25,0],
        [0,0,0,5,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,17284719827,0,0,2,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,-16477]
    ]

    def test_gui_errors_with_init(self):
        gui.init()
        gui.render(self.battleground)
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        gui.render(self.battleground, on_exit=None)

    def test_gui_errors_without_init(self):
        gui.render(self.battleground)
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        gui.render(self.battleground, on_exit=None)

    def test_gui_exit_callback(self):
        self.i = 0

        def callback(self):
            self.i += 1

        func = partial(callback, self)
        gui.init()
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        gui.render(self.battleground, on_exit=func)
        self.assertEqual(self.i, 1)

