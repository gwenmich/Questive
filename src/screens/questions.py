from src.game_config.global_config import *
from src.api import decode_strings
import random
from src.game_config.button import Button
from src.screens.base_screen import BaseScreen


class Question(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.buttons = []

        self.data = decode_strings()
        self.question_data = self.data["results"]
        self.questions = []
        self.correct_answers = []
        self.incorrect_answers = []
        self.question_answers = []

        self.index = 0

        self.get_question_data()
        self.create_buttons()

    def get_question_data(self):
        for question in self.question_data:
            self.questions.append(question["question"])
            self.correct_answers.append(question["correct_answer"])
            self.incorrect_answers.append(question["incorrect_answers"])

            all_answers = [question["correct_answer"]] + question["incorrect_answers"]
            self.question_answers.append(all_answers)

    def display_question(self):
        if len(self.questions[self.index]) > 50:
            split_question = self.questions[self.index].rfind(" ", 0, 50)
            part_1 = self.questions[self.index][:split_question].strip()
            part_2 = self.questions[self.index][split_question:].strip()
            self.draw.render_text(part_1, MEDIUM_FONT, (SCREEN_WIDTH // 2, 150))
            self.draw.render_text(part_2, MEDIUM_FONT, (SCREEN_WIDTH // 2, 180))
        else:
            self.draw.render_text(self.questions[self.index], MEDIUM_FONT, (SCREEN_WIDTH // 2, 180))

    def display_buttons(self):
        for button in self.buttons:
            self.display.blit(button.image, button.rect)

    def create_buttons(self):
        self.buttons = []
        random.shuffle(self.question_answers[self.index])

        for i, answer in enumerate(self.question_answers[self.index]):
            x = SCREEN_WIDTH // 2 - 400
            y = 250 + i * 80
            width, height = 800, 50
            button = Button(x, y, width, height, answer, MEDIUM_FONT)
            self.buttons.append(button)

    def run(self):
        self.timer.draw_timer()

        if self.index < len(self.questions):
            self.display_question()
            self.display_buttons()

        for button in self.buttons:
            if button.text == self.correct_answers[self.index]:
                if button.is_pressed():
                    self.game_state_manager.set_state("suspects")
                    self.index += 1
                    self.create_buttons()

            elif button.text in self.incorrect_answers[self.index]:
                if button.is_pressed():
                    self.game_state_manager.set_state("suspects")
                    self.index += 1
                    self.create_buttons()


if __name__ == "main__":
    pass
