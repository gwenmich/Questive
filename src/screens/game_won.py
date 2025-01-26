from src.game_config.global_config import MEDIUM_FONT, SCREEN_WIDTH
from src.screens.base_screen import BaseScreen


class GameWon(BaseScreen):
    def __init__(self, display, game_state_manager, draw, murderer, timer):
        super().__init__(display, game_state_manager, draw)
        self.murderer = murderer
        self.timer = timer

    def draw_text(self):
        heading_text = "Congratulations Detective!"
        sub_heading_text = "You solved the murder!"
        time_to_arrest = f"Arrest time: {self.timer.get_time()}"
        arrest_info_text = [
            f"{self.murderer[0]["name"]} has been arrested",
            "",
            f"and sent to the Trivia slammer.",
            "",
            f"Drinks are on the house!",
            "",
            "",
            f"The pub is now safe thanks to you.",
            "",
            f"Quiz Night has returned to being",
            "",
            f"about fun facts and not fatal acts."
        ]

        self.draw.render_text(heading_text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 65))
        self.draw.render_text(sub_heading_text, MEDIUM_FONT, (SCREEN_WIDTH // 2, 115))
        self.draw.render_text(time_to_arrest, MEDIUM_FONT, (SCREEN_WIDTH // 2, 215))
        self.draw.render_text_multiple_lines(arrest_info_text, 300)

    def run(self):
        self.timer.timer_running = False
        self.draw_text()


if __name__ == "__main__":
    pass
