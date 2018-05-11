import pygame
import sys
from output.renderer import Renderer


class GUI(Renderer):

    COLOR_PLAYER = (255, 255, 255)
    COLOR_EMPTY = (0, 0, 0)
    COLOR_FOG = (160, 160, 160)
    COLOR_PIT = (101, 67, 33)
    SIZE = 50

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((9 * GUI.SIZE, 9 * GUI.SIZE))

    def render(self, battleground, on_exit=sys.exit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if on_exit is not None:
                    on_exit()
                pygame.quit()
                return

        self.screen.fill((0, 0, 0))
        for r, row in enumerate(battleground):
            for c, column in enumerate(row):
                if column == -1:
                    GUI.draw_color(GUI.COLOR_PLAYER, r, c, self.screen)
                elif column == 0:
                    GUI.draw_color(GUI.COLOR_EMPTY, r, c, self.screen)
                elif column == 1:
                    GUI.draw_color(GUI.COLOR_FOG, r, c, self.screen)
                elif column == 2:
                    GUI.draw_color(GUI.COLOR_PIT, r, c, self.screen)
                else:
                    GUI.draw_color(GUI.get_color(column), r, c, self.screen)

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 8 * GUI.SIZE, GUI.SIZE * 9, GUI.SIZE))

        pygame.display.flip()

    @staticmethod
    def get_color(c):
        green = 255 - (c * 50)
        if green < 0 or green > 255:
            green = 0

        blue = c * 50
        if blue > 255 or blue < 0:
            blue = 255
        return 0, green, blue

    @staticmethod
    def draw_color(color, r, c, screen):
        pygame.draw.rect(screen, color, pygame.Rect(c * GUI.SIZE, r * GUI.SIZE, GUI.SIZE, GUI.SIZE))
