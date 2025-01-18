from src.game_config.utils import render_text
from src.game_config.global_config import *
from src.api import questions
import random
from src.game_config.button import Button

class Question:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def display_question(self):
        self.display.fill("black")
        render_text(questions[0]["question"], SMALL_FONT, (SCREEN_WIDTH//2, 180), self.display)

    def display_choices(self):
        choices = []
        questions[0]["correct_answer"].append(choices)
        for ans in questions[0]["incorrect_answers"]:
            ans.append(choices)

        first_choice = Button(SCREEN_WIDTH//2, 220,800, 40, WHITE)



    def run(self):
        self.display_question()