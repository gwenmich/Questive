from src.screens.base_screen import BaseScreen


class Rules(BaseScreen):
    def __init__(self, display, game_state_manager):
        super().__init__(display, game_state_manager)

    def run(self):
        # ------ blue added for initial demo. To be replaced with rules background etc ----------
        self.display.fill("blue")


if __name__ == "__main__":
    pass
