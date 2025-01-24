import sys
import pygame
from src.game_config.button import Button
from src.game_config.global_config import *


class Draw:
    def __init__(self, game_state_manager, screen):
        self.game_state_manager = game_state_manager
        self.screen = screen
        self.next_question_button = Button(1050, 650, MEDIUM_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, "Next Question",
                                           SMALL_FONT)

    def render_text(self, text, font_size, pos):
        font = pygame.font.Font(FONT, font_size)
        rendered_text = font.render(text, True, WHITE)
        rendered_txt_rect = rendered_text.get_rect(center=pos)
        self.screen.blit(rendered_text, rendered_txt_rect)

    def render_text_multiple_lines(self, text):
        y_pos = 0
        font = pygame.font.Font(FONT, MEDIUM_FONT)
        for line in text:
            rendered_line = font.render(line, True, WHITE)
            render_line_rect = rendered_line.get_rect(center=(SCREEN_WIDTH // 2, 150 + y_pos))
            y_pos += 28
            self.screen.blit(rendered_line, render_line_rect)

    def draw_next_question_button(self):
        self.screen.blit(self.next_question_button.image, self.next_question_button.rect)

    def check_button_press(self):
        if self.next_question_button.is_pressed():
            self.game_state_manager.set_state("question")


class Quit:
    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    pass
