from src.game_config.utils import render_text
from src.game_config.global_config import *
from src.api import questions

class Question:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def display_question(self):
        self.display.fill("black")
        render_text(questions[0]["question"], SMALL_FONT, (1280//2, 180), self.display)

    def display_choices(self):
        questions[0][]


    def run(self):
        self.display_question()