from src.api import questions
from game_config.global_config import *

class Category:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self):
        pass

    def display_category(self):
        self.display.fill("black")
        render_text("Category", small_font, (1280 // 2, 150))
        render_text(questions[0]["category"], large_font, (1280 // 2, 200))
        pygame.display.update()
        pygame.time.delay(2000)