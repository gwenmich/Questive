import pygame
from src.game_config.global_config import *

def render_text(text, font_size, pos, screen):
    font = pygame.font.Font(FONT, font_size)
    rendered_text = font.render(text, True, WHITE)
    rendered_txt_rect = rendered_text.get_rect(center=pos)
    screen.blit(rendered_text, rendered_txt_rect)


if __name__ == "__main__":
    pass