import pygame
from db.db_utils import DbConnection
from src.game_config.button import Button
from src.game_config.global_config import SMALL_FONT, MEDIUM_FONT, SCREEN_WIDTH, SMALL_BUTTON_WIDTH
from src.screens.base_screen import BaseScreen


class Suspects(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer, clues, murderer):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.clues = clues
        self.murderer = murderer
        self.active_clue = ""

    def draw_correct_answer(self):
        text = "Correct Answer!"
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 50))

    def draw_wrong_answer(self):
        text = "Wrong Answer! No clue this time"
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 50))

    # gets random clue for Murderer
    def draw_clue(self):
        # returns a new clue each time the suspect screen is loaded
        if self.active_clue == "":
            self.active_clue = f"Clue: {self.clues.get_clue()}"
        self.draw.render_text(self.active_clue, MEDIUM_FONT, (SCREEN_WIDTH // 2, 115))

    def draw_text_guidance(self):
        text = "Click on a suspect to eliminate them"
        self.draw.render_text(text, SMALL_FONT, (SCREEN_WIDTH // 2, 165))

    @staticmethod
    def get_suspects():
        suspects = DbConnection().get_suspects()
        return suspects

    def draw_suspects(self):
        all_suspects = self.get_suspects()

        n = 0
        x = 210
        y = 350
        suspects_per_row = 5

        for suspect in all_suspects:
            if n < suspects_per_row:
                pass
            elif n == 5:
                x = 210
                y = 550
            self.draw.render_text(suspect["name"], SMALL_FONT, (x, y))
            suspect_img = pygame.image.load(f"assets/suspects/{0}.png").convert_alpha()
            self.display.blit(suspect_img, (x - 60, y - 140))
            x += 200
            n += 1

    def draw_arrest_button(self):
        arrest_button = Button(SCREEN_WIDTH // 2 - SMALL_BUTTON_WIDTH // 2, 650, SMALL_BUTTON_WIDTH, 50,
                               "Arrest Suspect", SMALL_FONT)
        self.display.blit(arrest_button.image, arrest_button.rect)

    def run(self):
        self.timer.draw_timer()
        self.draw_correct_answer()
        self.draw_clue()
        self.draw_text_guidance()
        self.draw_suspects()
        self.draw_arrest_button()
        self.draw.draw_next_question_button()


if __name__ == "__main__":
    pass
