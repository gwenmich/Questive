from src.game_config.button import Button
from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SMALL_BUTTON_HEIGHT, LARGE_BUTTON_WIDTH
from src.screens.base_screen import BaseScreen


class Rules(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.start_investigation_button = Button(SCREEN_WIDTH // 2 - LARGE_BUTTON_WIDTH // 2, 625, LARGE_BUTTON_WIDTH,
                                                 SMALL_BUTTON_HEIGHT,
                                                 "Start investigation...", MEDIUM_FONT)

    def draw_screen(self):
        text = [
            "It was supposed to be a fun Quiz Night in Trivia Hollow.",
            "But when the Quizmaster was found dead backstage, the night ",
            "turned into a deadly game of wits. The suspects? Everyone in ",
            "the pub—from the trivia-obsessed know-it-all to the mysterious",
            "bartender.",
            "",
            "Your mission: solve 10 questions to uncover clues, eliminate",
            "suspects, and unmask the killer. Each correct answer gets",
            "you closer to the truth, but one wrong move, and you might",
            "be the next victim of the killer who hates bad answers.",
            "",
            "Can you solve the murder and save Quiz Night?",
            "Or will you be remembered ",
            "as the player who didn’t know their capital cities?",
            "",
            "Trivia Hollow needs you!"
        ]

        self.draw.render_text_multiple_lines(text, 125)

    def draw_button(self):
        self.display.blit(self.start_investigation_button.image, self.start_investigation_button.rect)

    def check_button_press(self):
        if self.start_investigation_button.is_pressed():
            self.game_state_manager.set_state("question")
            self.timer.start_timer()

    def run(self):
        self.draw_screen()
        self.draw_button()
        self.check_button_press()


if __name__ == "__main__":
    pass
