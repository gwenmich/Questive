from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen
import pygame


class GameLost(BaseScreen):

    def draw_screen(self):
        img = pygame.image.load("assets/game_lost.png")
        self.display.blit(img, (SCREEN_WIDTH // 2 - 128, 350))
        text = ["You didn't manage to uncover the killer in time...",
                "They struck again and you were the target.",
                "Let's hope someone else finds them..."
                ]
        self.draw.render_text_multiple_lines(text)

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
