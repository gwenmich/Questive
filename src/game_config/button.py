import pygame
from src.game_config.global_config import *


class Button:

    def __init__(self, x, y, width, height, text, font_size, colour=WHITE, bg_colour=DARK_GREY):
        self.font = pygame.font.Font(FONT, font_size)
        self.text = text

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.colour = colour
        self.bg_colour = bg_colour

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg_colour)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.content = self.font.render(self.text, True, self.colour)
        self.content_rect = self.content.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.content, self.content_rect)

    def is_pressed(self, pressed):
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pressed[0]:
                return True
            else:
                return False
        return False
