from game_config.global_config import *
from src.api import questions

class Question:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self):
        pass

    def display_question(self):
        self.display.fill("black")
        render_text(questions[0]["question"], small_font, (1280//2, 180))