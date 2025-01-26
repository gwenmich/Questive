from src.api import ApiData
from src.game_config.global_config import *
import random
from src.game_config.button import Button
from src.screens.base_screen import BaseScreen


class Question(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.buttons = []

        self.api_data = ApiData(10, "easy")
        self.data = self.api_data.decode_strings()
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

    # splits question text into rows to fit on screen
    def split_long_text(self, char_split_length, part0):
        parts = []
        split_question = self.questions[self.index].rfind(" ", 0, char_split_length)
        part_1 = part0 + self.questions[self.index][:split_question].strip()
        parts.append(part_1)
        part_2 = self.questions[self.index][split_question:].strip()
        if len(part_2) > char_split_length:
            split_2 = part_2.rfind(" ", 0, char_split_length)
            part_2_1 = part_2[:split_2].strip()
            parts.append(part_2_1)
            part_2_2 = part_2[split_2:].strip()
            parts.append(part_2_2)
            return parts
        else:
            parts.append(part_2)
            return parts

    def display_question(self):
        part_0 = f"Q{self.index + 1}: "
        if len(self.questions[self.index]) > 60:
            parts = self.split_long_text(60, part_0)
            i = 0
            for part in parts:
                self.draw.render_text(part, MEDIUM_FONT, (SCREEN_WIDTH // 2, 150 + i))
                i += 30

        else:
            short_question = part_0 + self.questions[self.index]
            self.draw.render_text(short_question, MEDIUM_FONT, (SCREEN_WIDTH // 2, 180))

    def display_buttons(self):
        for button in self.buttons:
            self.display.blit(button.image, button.rect)

    def create_buttons(self):
        # checks against number of available questions
        if self.index < len(self.questions):
            self.buttons = []
            random.shuffle(self.question_answers[self.index])

            # creates number of buttons dependent on number of answers available
            for i, answer in enumerate(self.question_answers[self.index]):
                x = SCREEN_WIDTH // 2 - 400
                y = 250 + i * 80
                width, height = 800, 50
                if len(answer) > 50:
                    button = Button(x, y, width, height, answer, SMALL_MED_FONT)
                else:
                    button = Button(x, y, width, height, answer, MEDIUM_FONT)
                self.buttons.append(button)

    # for each button, a different state is set depending on correct/incorrect answer
    def checks_answer_pressed(self):
        for button in self.buttons:
            if button.is_pressed():
                if button.text == self.correct_answers[self.index]:
                    print(
                        f"Q{self.index + 1}: The player chose the CORRECT answer! Correct answer was {self.correct_answers[self.index]}")
                    self.game_state_manager.set_state("correct_answer")
                    self.index += 1
                    self.create_buttons()

                elif button.text in self.incorrect_answers[self.index]:
                    print(
                        f"Q{self.index + 1}: The player chose the INCORRECT answer. Correct answer was {self.correct_answers[self.index]}")
                    self.game_state_manager.set_state("wrong_answer")
                    self.index += 1
                    self.create_buttons()

    def run(self):
        self.timer.draw_timer()
        self.display_buttons()
        self.display_question()
        self.checks_answer_pressed()


if __name__ == "main__":
    pass
