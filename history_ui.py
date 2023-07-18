import pygame
import sys

pygame.init()

# GUI set up
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850
INTERFACE_BACKGROUND = (255, 255, 255)
NOIR = (0, 0, 0)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("History UI")


def show_history():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill(INTERFACE_BACKGROUND)
    pygame.display.update()
