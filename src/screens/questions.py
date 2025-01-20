from src.game_config.global_config import *
from src.api import questions
import random
from src.game_config.button import Button
from src.screens.base_screen import BaseScreen


class Question(BaseScreen):
    def __init__(self, display, game_state_manager, draw):
        super().__init__(display, game_state_manager, draw)
        self.buttons = []
        self.get_choices()

    def display_question(self):
        self.display.fill(BLACK)
        self.draw.render_text(questions[0]["question"], LARGE_FONT, (SCREEN_WIDTH // 2, 180))
        for button in self.buttons:
            self.display.blit(button.image, button.rect)

    def get_choices(self):
        choices = []
        choices.append(questions[0]["correct_answer"])
        for ans in questions[0]["incorrect_answers"]:
            choices.append(ans)

        random.shuffle(choices)

        for i, choice in enumerate(choices):
            x = SCREEN_WIDTH//2 - 400
            y = 250 + i * 80
            width, height = 800, 50
            button = Button(x, y, width, height, WHITE, DARK_GREY, choice, MEDIUM_FONT)
            self.buttons.append(button)

    def run(self):
        self.display_question()


if __name__ == "main__":
    pass
