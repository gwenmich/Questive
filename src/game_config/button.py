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

        if len(self.text) > 50:
            self.split_long_text()
        else:
            self.content = self.font.render(self.text, True, self.colour)
            self.content_rect = self.content.get_rect(center=(self.width / 2, self.height / 2))
            self.image.blit(self.content, self.content_rect)

    def is_pressed(self):
        position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(position):
            if pressed[0]:
                return True
            else:
                return False
        return False

    # splits answer text when longer than 50 chars at closest space char
    def split_long_text(self):
        split_text = self.text.rfind(" ", 0, 50)
        part_1 = self.text[:split_text].strip()
        part_2 = self.text[split_text:].strip()
        parts = [part_1, part_2]
        i = 15
        for part in parts:
            self.content = self.font.render(part, True, self.colour)
            self.content_rect = self.content.get_rect(center=(self.width / 2, i))
            self.image.blit(self.content, self.content_rect)
            i += 20