from db.db_utils import DbConnection
from src.game_config.global_config import SCREEN_WIDTH, MEDIUM_FONT, SMALL_MED_FONT
from src.screens.base_screen import BaseScreen


class ArrestSuspect(BaseScreen):

    def __init__(self, display, game_state_manager, draw, timer, button_handler, suspects):
        super().__init__(display, game_state_manager, draw)
        self.timer = timer
        self.button_handler = button_handler
        self.suspects = suspects

    def draw_text(self):
        heading_text = "Time to make the arrest!"
        info_text = "Click on the suspect below to make the arrest"
        self.draw.render_text(heading_text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 115))
        self.draw.render_text(info_text, SMALL_MED_FONT, (SCREEN_WIDTH // 2, 165))

    @staticmethod
    def get_suspects():
        suspects = DbConnection().get_suspects()
        return suspects

    def draw_screen(self):
        self.timer.draw_timer()
        self.draw_text()
        self.suspects.draw_suspects()
        self.button_handler.arrest()

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
