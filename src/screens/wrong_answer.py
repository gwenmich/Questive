import pygame

from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


class WrongAnswer(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer

    def draw_screen(self):
        # ------ Temporary placeholder----- ----------
        self.draw.render_text("Wrong answer....the murderer is on the loose. Try again", MEDIUM_FONT,
                              (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pygame.display.update()

    def run(self):
        self.timer.draw_timer()
        self.draw.draw_next_question_button()
        self.draw_screen()
        self.draw.check_button_press()


if __name__ == "__main__":
    pass
