from src.screens.base_screen import BaseScreen


class MainMenu(BaseScreen):
    def __init__(self, display, game_state_manager):
        super().__init__(display, game_state_manager)

    def run(self):
        # ------ red added for initial demo. To be replaced with main menu background etc ----------
        self.display.fill("red")


if __name__ == "__main__":
    pass
