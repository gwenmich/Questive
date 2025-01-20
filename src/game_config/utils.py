from src.game_config.button import Button
from src.game_config.global_config import *


class Draw:
    def __init__(self, screen):
        self.screen = screen

    def render_text(self, text, font_size, pos):
        font = pygame.font.Font(FONT, font_size)
        rendered_text = font.render(text, True, WHITE)
        rendered_txt_rect = rendered_text.get_rect(center=pos)
        self.screen.blit(rendered_text, rendered_txt_rect)

    def draw_next_question_button(self):
        next_question_button = Button(1075, 650, SMALL_BUTTON_WIDTH, 50, WHITE, DARK_GREY, "Next Question", SMALL_FONT)
        self.screen.blit(next_question_button.image, next_question_button.rect)


if __name__ == "__main__":
    pass
