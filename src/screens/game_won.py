from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


class GameWon(BaseScreen):

    def draw_screen(self):
        # ------ Temporary placeholder----- ----------
        text = "You win"
        self.draw.render_text(text, MEDIUM_FONT, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
