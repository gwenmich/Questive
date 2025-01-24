import pygame

from src.game_config.global_config import SCREEN_WIDTH, SCREEN_HEIGHT, MEDIUM_FONT
from src.screens.base_screen import BaseScreen


class ArrestSuspect(BaseScreen):

    def draw_screen(self):
        # ------ Temporary placeholder----- ----------
        self.draw.render_text("Arrest suspect screen", MEDIUM_FONT,
                              (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pygame.display.update()

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
