import pygame
import sys
from class_button import Button

pygame.init()

# GUI set up
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 350
INTERFACE_BACKGROUND = (255, 255, 255)
NOIR = (0, 0, 0)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Main GUI")

# Texts
font = pygame.font.SysFont(None, 36)
alarm = font.render("Alarm System", True, NOIR)
living_room_light = font.render("Living Room Light", True, NOIR)
kitchen_light = font.render("Kitchen Light", True, NOIR)
history = font.render("History", True, NOIR)

#  Buttons
alarm_on_button = Button(10, 40, 40, 65, "ON")
alarm_off_button = Button(77, 40, 40, 65, "OFF")

living_room_on_button = Button(10, 125, 40, 65, "ON")
living_room_off_button = Button(77, 125, 40, 65, "OFF")

kitchen_on_button = Button(10, 210, 40, 65, "ON")
kitchen_off_button = Button(77, 210, 40, 65, "OFF")

history_button = Button(10, 295, 40, 100, "SHOW")

# State containers
alarm_state = Button(175, 40, 40, 90, "Disarmed", (255, 255, 255), (255, 0, 0))

living_room_light_state = Button(175, 125, 40, 65, "OFF", (255, 255, 255), (255, 0, 0))

kitchen_light_state = Button(175, 210, 40, 65, "OFF", (255, 255, 255), (255, 0, 0))


def start_gui():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill(INTERFACE_BACKGROUND)

    screen.blit(alarm, (10, 10))
    alarm_on_button.draw_button(screen)
    alarm_off_button.draw_button(screen)
    alarm_state.draw_button(screen)
    pygame.draw.line(screen, NOIR, (10, 87), (290, 87), 2)

    screen.blit(living_room_light, (10, 95))
    living_room_on_button.draw_button(screen)
    living_room_off_button.draw_button(screen)
    living_room_light_state.draw_button(screen)
    pygame.draw.line(screen, NOIR, (10, 172), (290, 172), 2)

    screen.blit(kitchen_light, (10, 180))
    kitchen_on_button.draw_button(screen)
    kitchen_off_button.draw_button(screen)
    kitchen_light_state.draw_button(screen)
    pygame.draw.line(screen, NOIR, (10, 257), (290, 257), 2)

    screen.blit(history, (10, 265))
    history_button.draw_button(screen)
    pygame.display.update()


while True:
    start_gui()
