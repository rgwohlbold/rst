import pygame
import sys

COLOR_PLAYER = (255, 255, 255)
COLOR_EMPTY = (0, 0, 0)
COLOR_FOG = (160, 160, 160)
COLOR_PIT = (101, 67, 33)

STATE_UNINITIALIZED = 0
STATE_RUNNING = 1
STATE_FINISHED = 2
state = STATE_UNINITIALIZED
screen = None
running = False
size = 50


def init():
    global screen, state, size
    pygame.init()
    screen = pygame.display.set_mode((9 * size, 9 * size))
    state = STATE_RUNNING


def render(battleground, on_exit=sys.exit):
    global state

    if state == STATE_UNINITIALIZED or state == STATE_FINISHED:
        init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if on_exit is not None:
                on_exit();
            pygame.quit()
            state = STATE_FINISHED
            return

    screen.fill((0, 0, 0))
    for r, row in enumerate(battleground):
        for c, column in enumerate(row):
            if column == -1:
                draw_color(COLOR_PLAYER, r, c, screen)
            elif column == 0:
                draw_color(COLOR_EMPTY, r, c, screen)
            elif column == 1:
                draw_color(COLOR_FOG, r, c, screen)
            elif column == 2:
                draw_color(COLOR_PIT, r, c, screen)
            else:
                draw_color(get_color(column), r, c, screen)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 8 * size, size * 9, size))

    pygame.display.flip()


def get_color(c):
    green = 255 - (c * 50)
    if green < 0 or green > 255:
        green = 0

    blue = c * 50
    if blue > 255 or blue < 0:
        blue = 255
    return 0, green, blue


def draw_color(color, r, c, screen):
    pygame.draw.rect(screen, color, pygame.Rect(c * size, r * size, size, size))
