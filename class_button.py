#!/usr/bin/python3

import pygame


class Button:
    def __init__(
        self,
        pos_x,
        pos_y,
        height,
        width,
        text,
        fillColor=(0, 0, 0),
        textColor=(255, 255, 255),
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.text = text
        self.fillColor = fillColor
        self.textColor = textColor

    def draw_button(self, screen):
        sysfont = pygame.font.get_default_font()
        font = pygame.font.SysFont(None, 36)
        pygame.draw.rect(
            screen,
            self.fillColor,
            pygame.Rect(self.pos_x, self.pos_y, self.width, self.height),
        )
        textBtn = font.render(self.text, True, self.textColor)
        rectBtn = textBtn.get_rect()
        rectBtn.center = (self.pos_x + self.width / 2, self.pos_y + self.height / 2)
        screen.blit(textBtn, rectBtn)

    def isOverButton(self, mouse_pos):
        mouse_x_pos = mouse_pos[0]
        mouse_y_pos = mouse_pos[1]

        if (
            mouse_x_pos >= self.pos_x
            and mouse_x_pos <= self.pos_x + self.width
            and mouse_y_pos >= self.pos_y
            and mouse_y_pos <= self.pos_y + self.height
        ):
            return True
        return False
