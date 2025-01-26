from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen
import random


class WrongAnswer(BaseScreen):
    def __init__(self, screen, game_state_manager, draw, timer, question, button_handler):
        super().__init__(screen, game_state_manager, draw)
        self.timer = timer
        self.question = question
        self.button_handler = button_handler
        self.text = [
            "Wrong answer. The killer heard you...",
            "Wrong. The killer is one step closer to finding you!",
            "You're running out of places to hide..."
        ]

        self.message = random.choice(self.text)


    def draw_screen(self, text):
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


    def check_question_status(self):
        if self.question.index < len(self.question.questions):
            self.button_handler.next_question()
        else:
            self.text = "Wrong answer..Times up..you must arrest a suspect"
            self.button_handler.arrest()


    def run(self):
        self.timer.draw_timer()
        self.draw_screen(self.message)
        self.check_question_status()



if __name__ == "__main__":
    pass
