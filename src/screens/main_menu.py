from src.screens.base_screen import BaseScreen


class MainMenu(BaseScreen):

    def run(self):
        # ------ red added for initial demo. To be replaced with main menu background etc ----------
        self.display.fill("red")


if __name__ == "__main__":
    pass
