import pygame
import sys

screen = None
initialized = False
size = 50

def init():
    global screen, initialized,size
    pygame.init()
    screen = pygame.display.set_mode((9*size, 9*size))
    initialized = True

def render(battleground):

    if not initialized:
        init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,0,0))
    for r,row in enumerate(battleground):
        for c,column in enumerate(row):
            if column == -1:
                draw_color((255,0,0),r,c,screen)
            elif column == 0:
                draw_color((0,0,0),r,c,screen)
            elif column == 1:
                draw_color((160,160,160),r,c,screen)
            elif column == 2:
                draw_color((101, 67, 33),r,c,screen)
            else:
                draw_color(get_color(column),r,c,screen)

    pygame.draw.rect(screen, (255,255,255),pygame.Rect(0,8*size,size*9,size))

    pygame.display.flip()


def get_color(c):
    blue = min(250, c * 50)
    green = max(0, 255-(c*50))
    return (0,green,blue)

def draw_color(color,r,c,screen):
    pygame.draw.rect(screen, color, pygame.Rect(c*size,r*size,size,size))
