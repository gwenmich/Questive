from src.game_config.utils import render_text
from src.game_config.global_config import *
from src.api import questions
import random
from src.game_config.button import Button

class Question:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager
        self.buttons = []
        self.get_choices()

    def display_question(self):
        self.display.fill(BLACK)
        render_text(questions[0]["question"], SMALL_FONT, (SCREEN_WIDTH//2, 180), self.display)
        for button in self.buttons:
            self.display.blit(button.image, button.rect)

    def get_choices(self):
        choices = []
        choices.append(questions[0]["correct_answer"])
        for ans in questions[0]["incorrect_answers"]:
            choices.append(ans)

        random.shuffle(choices)

        for i, choice in enumerate(choices):
            x = SCREEN_WIDTH//2
            y = 220 + i * 50
            width, height = 800, 40
            button = Button(x, y, width, height, WHITE, DARK_GREY, choice, SMALL_FONT)
            self.buttons.append(button)




    def run(self):
        self.display_question()
        # self.display_choices()