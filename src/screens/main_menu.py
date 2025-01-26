import pygame.image

from src.screens.base_screen import BaseScreen
from src.game_config.utils import *


class MainMenu(BaseScreen):

    def __init__(self, display, game_state_manager, draw):
        super().__init__(display, game_state_manager, draw)
        self.logo_img = pygame.image.load("assets/images/questive_logo.png")
        self.play_button = Button(SCREEN_WIDTH // 2 - MEDIUM_BUTTON_WIDTH // 2, 360, MEDIUM_BUTTON_WIDTH,
                                  MEDIUM_BUTTON_HEIGHT, "Play", LARGE_FONT)
        self.exit_button = Button(SCREEN_WIDTH // 2 - MEDIUM_BUTTON_WIDTH // 2, 490, MEDIUM_BUTTON_WIDTH,
                                  MEDIUM_BUTTON_HEIGHT, "Exit", LARGE_FONT)

    def draw_screen(self):

        self.display.blit(self.logo_img, (SCREEN_WIDTH//2 - 292, 150))

        self.display.blit(self.play_button.image, self.play_button.rect)
        self.display.blit(self.exit_button.image, self.exit_button.rect)


    def run(self):
        self.draw_screen()

        # button logic
        if self.play_button.is_pressed():
            self.game_state_manager.set_state("rules")

        if self.exit_button.is_pressed():
            quit_app()


if __name__ == "__main__":
    pass
