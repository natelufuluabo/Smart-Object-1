import pygame
import sys

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 350
INTERFACE_BACKGROUND = (255, 255, 255)
NOIR = (0, 0, 0)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Main GUI")

font = pygame.font.SysFont(None, 36)
alarm = font.render("Alarm System", True, NOIR)
living_room_light = font.render("Living Room Light", True, NOIR)
kitchen_light = font.render("Kitchen Light", True, NOIR)
history = font.render("History", True, NOIR)


def start_gui():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill(INTERFACE_BACKGROUND)
    screen.blit(alarm, (10, 10))
    screen.blit(living_room_light, (10, 60))
    screen.blit(kitchen_light, (10, 110))
    screen.blit(history, (10, 160))
    pygame.display.update()


while True:
    start_gui()
