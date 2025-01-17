import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

FONT = "/assets/font/PressStart2P-Regular.ttf"
small_font = pygame.font.Font(FONT, 20)
large_font = pygame.font.Font(FONT, 30)


def render_text(text, font, pos, screen):
    rendered_text = font.render(text, True, "white")
    rendered_txt_rect = rendered_text.get_rect(center=pos)
    screen.blit(rendered_text, rendered_txt_rect)