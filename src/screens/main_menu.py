from src.game_config.global_config import SCREEN_HEIGHT, SCREEN_WIDTH, MEDIUM_FONT
from src.screens.base_screen import BaseScreen


class MainMenu(BaseScreen):
    def __init__(self, display, game_state_manager, draw, suspects):
        super().__init__(display, game_state_manager, draw)
        self.suspects = suspects

    def draw_screen(self):
        # ------ Temporary placeholder----- ----------
        self.draw.render_text("Main Menu - Press ENTER to move to next screen", MEDIUM_FONT,
                              (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def run(self):
        self.draw_screen()
        self.suspects.get_murderer()


if __name__ == "__main__":
    pass
