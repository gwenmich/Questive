class Rules:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self):
        # ------ blue added for initial demo. To be replaced with rules background etc ----------
        self.display.fill("blue")


if __name__ == "__main__":
    pass
