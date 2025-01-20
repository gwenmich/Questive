from db.db_utils import DbConnection
from src.game_config.button import Button
from src.game_config.global_config import BLACK, SMALL_FONT, MEDIUM_FONT, SCREEN_WIDTH, WHITE, DARK_GREY, \
    SMALL_BUTTON_WIDTH
from src.screens.base_screen import BaseScreen


class Suspects(BaseScreen):
    def __init__(self, display, game_state_manager, draw):
        super().__init__(display, game_state_manager)
        self.draw = draw

    def draw_screen(self):
        self.display.fill(BLACK)

    def draw_correct_answer(self):
        text = "Correct Answer!"
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 50))

    def draw_clue(self):
        text = "Clue:"  # random clue to be entered here -------------------
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 115))

    def draw_text_guidance(self):
        text = "Click on a suspect to eliminate them"
        self.draw.render_text(text, SMALL_FONT, (SCREEN_WIDTH // 2, 165))

    @staticmethod
    def get_murderer():
        murderer = DbConnection().get_random_suspect()
        murderer_name = murderer[0]['name']
        return murderer_name

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
            x += 200
            n += 1

    def draw_arrest_button(self):
        arrest_button = Button(SCREEN_WIDTH // 2 - SMALL_BUTTON_WIDTH // 2, 650, SMALL_BUTTON_WIDTH, 50, WHITE,
                               DARK_GREY, "Arrest Suspect", SMALL_FONT)
        self.display.blit(arrest_button.image, arrest_button.rect)

    def run(self):
        self.draw_screen()
        self.draw_correct_answer()
        self.draw_clue()
        self.draw_text_guidance()
        self.draw_suspects()
        self.draw_arrest_button()
        self.draw.draw_next_question_button()


if __name__ == "__main__":
    pass
    # print(Suspects.get_murderer()) # returns random murderer
