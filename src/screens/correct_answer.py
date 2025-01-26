from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SMALL_MED_FONT
from src.screens.base_screen import BaseScreen


class CorrectAnswer(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer, question, clues, button_handler, suspects):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.question = question
        self.clues = clues
        self.button_handler = button_handler
        self.suspects = suspects
        self.active_clue = ""
        self.draw_suspects = self.suspects.draw_suspects()

    def draw_correct_answer(self):
        text = "Correct Answer!"
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 50))

    # draws random clue for the Murderer
    def draw_clue(self):
        if self.active_clue == "":
            self.active_clue = f"Clue: {self.clues.get_clue()}"
        self.draw.render_text(self.active_clue, MEDIUM_FONT, (SCREEN_WIDTH // 2, 115))

    def draw_info_text(self):
        info_text = "Click on a suspect to eliminate them"
        ready_to_arrest_text = "Ready to arrest the suspect?"
        self.draw.render_text(info_text, SMALL_MED_FONT, (SCREEN_WIDTH // 2, 165))
        self.draw.render_text(ready_to_arrest_text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 625))

    def check_question_status(self):
        if self.question.index < len(self.question.questions):
            self.button_handler.next_question()

    def draw_screen(self):
        self.timer.draw_timer()
        self.draw_correct_answer()
        self.draw_clue()
        self.draw_info_text()
        self.suspects.draw_suspects()
        self.button_handler.arrest()

    def run(self):
        self.draw_screen()
        self.check_question_status()


if __name__ == "__main__":
    pass
