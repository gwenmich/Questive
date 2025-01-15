class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self):
        # ------ red added for initial demo. To be replaced with main menu background etc ----------
        self.display.fill("red")


if __name__ == "__main__":
    pass
