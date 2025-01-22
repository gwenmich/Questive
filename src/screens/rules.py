from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


class Rules(BaseScreen):

    def draw_screen(self):
        # ------ Temporary placeholder----- ----------
        # self.draw.render_text("Rules - Press ENTER to move to next screen", MEDIUM_FONT,
        #                       (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        text = [
            "It was supposed to be a fun Quiz Night in Trivia Hollow.,",
            "But when the Quizmaster was found dead backstage, the night ",
            "turned into a deadly game of wits. The suspects? Everyone in ",
            "the pub—from the trivia-obsessed know-it-all to the bartender ",
            "with a peanut alibi.",
            "",
            "Your mission: solve quizzes to uncover clues, eliminate",
            "suspects, and unmask the killer. Each correct answer gets",
            "you closer to the truth, but one wrong move, and you might",
            "be the next victim of the killer who hates bad answers.",
            "",
            "Can you solve the murder and save Quiz Night?",
            "Or will you be remembered ",
            "as the player who didn’t know their capital cities?",
            "",
            "Press ENTER to continue"
        ]
        self.draw.render_text_multiple_lines(text)

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
