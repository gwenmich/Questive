import pygame
from db.db_utils import DbConnection
from src.game_config.global_config import SMALL_FONT, MEDIUM_FONT, SCREEN_WIDTH, SMALL_MED_FONT
from src.screens.base_screen import BaseScreen


class Suspects(BaseScreen):
    def __init__(self, display, game_state_manager, draw, timer, question, clues, murderer, button_handler):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.question = question
        self.clues = clues
        self.murderer = murderer
        self.button_handler = button_handler
        self.active_clue = ""

    def draw_correct_answer(self):
        text = "Correct Answer!"
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 50))

    # gets random clue for Murderer
    def draw_clue(self):
        # returns a new clue each time the suspect screen is loaded
        if self.active_clue == "":
            self.active_clue = f"Clue: {self.clues.get_clue()}"
        self.draw.render_text(self.active_clue, MEDIUM_FONT, (SCREEN_WIDTH // 2, 115))

    def draw_info_text(self):
        info_text = "Click on a suspect to eliminate them"
        ready_to_arrest_text = "Ready to arrest the suspect?"
        self.draw.render_text(info_text, SMALL_MED_FONT, (SCREEN_WIDTH // 2, 165))
        self.draw.render_text(ready_to_arrest_text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 625))

    @staticmethod
    def get_suspects():
        suspects = DbConnection().get_suspects()
        return suspects

    # method also used in arrest_suspect
    def draw_suspects(self):
        all_suspects = self.get_suspects()

        n = 0
        x_starting_pos = 235
        x = x_starting_pos
        y = 350
        suspects_per_row = 5

        for suspect in all_suspects:
            if n < suspects_per_row:
                pass
            elif n == 5:
                x = x_starting_pos
                y = 550

            self.draw.render_text(suspect["name"], SMALL_FONT, (x, y))
            suspect_img = pygame.image.load(f"assets/suspects/{n}.png").convert_alpha()
            suspect_img_rect = suspect_img.get_rect(topleft=(x - 60, y - 140))
            self.display.blit(suspect_img, suspect_img_rect)

            self.check_guess(suspect_img_rect, n)

            x += 200
            n += 1

    def check_guess(self, suspect_img_rect, n):
        if self.game_state_manager.get_state() == "suspects":
            # could potentially add transparency settings in here?--------------------
            pass
        # Checks when the mouse is pressed - not sure this is in right place - potential refactoring -----------
        elif self.game_state_manager.get_state() == "arrest_suspect":
            if suspect_img_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                if self.murderer[0]["suspect_id"] == DbConnection().get_suspects()[n]["suspect_id"]:
                    print("The murder has been caught!")
                    self.game_state_manager.set_state("game_won")
                else:
                    print("Incorrect arrest")
                    self.game_state_manager.set_state("game_lost")

    def check_question_status(self):
        if self.question.index < len(self.question.questions):
            self.button_handler.next_question()

    def draw_screen(self):
        self.timer.draw_timer()
        self.draw_correct_answer()
        self.draw_clue()
        self.draw_info_text()
        self.draw_suspects()
        self.button_handler.arrest()

    def run(self):
        self.draw_screen()
        self.check_question_status()


if __name__ == "__main__":
    pass
