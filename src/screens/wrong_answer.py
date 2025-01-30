from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen
import random


class WrongAnswer(BaseScreen):
    def __init__(self, screen, game_state_manager, draw, timer, question, button_handler, event_handler):
        super().__init__(screen, game_state_manager, draw)
        self.timer = timer
        self.question = question
        self.button_handler = button_handler
        self.event_handler = event_handler
        self.wrong_answer = [
            "Wrong answer! The killer heard you...",
            "Wrong answer. The killer is one step closer to finding you!",
            "Wrong answer! You're running out of places to hide..."
        ]

    # draws random wrong answer text
    def draw_screen(self):
        # Retrieves current wrong answer text
        wrong_answer_text = self.event_handler.get_wrong_answer_text()

        # If there is no wrong answer set, set a new random wrong answer text
        if not wrong_answer_text:
            wrong_answer_text = random.choice(self.wrong_answer)
            self.event_handler.set_wrong_answer_text(wrong_answer_text)

        self.draw.render_text(wrong_answer_text, MEDIUM_FONT, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def check_question_status(self):
        if self.question.index < len(self.question.questions):
            self.button_handler.next_question()
        else:
            self.wrong_answer = "Wrong answer..Times up..you must arrest a suspect"
            self.button_handler.arrest()

    def run(self):
        self.timer.draw_timer()
        self.draw_screen()
        self.check_question_status()


if __name__ == "__main__":
    pass
