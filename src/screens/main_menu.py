from src.game_config.global_config import LARGE_FONT
from src.screens.base_screen import BaseScreen
from src.game_config.button import Button
import pygame

class MainMenu(BaseScreen):

    def __init__(self, display, game_state_manager, draw):
        super().__init__(display, game_state_manager, draw)
        self.play_button = Button(550, 360, 200, 80, "Play", LARGE_FONT)
        self.exit_button = Button(550, 490, 200, 80, "Exit", LARGE_FONT)


    def draw_screen(self):
        # to add logo of game above buttons
        self.display.blit(self.play_button.image, self.play_button.rect)
        self.display.blit(self.exit_button.image, self.exit_button.rect)


    def run(self):
        self.draw_screen()
        mouse_pressed = pygame.mouse.get_pressed()

        # button logic
        if self.play_button.is_pressed(mouse_pressed):
            self.game_state_manager.set_state("rules")

        if self.exit_button.is_pressed(mouse_pressed):
            pygame.quit()



if __name__ == "__main__":
    pass
