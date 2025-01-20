from src.clues import Clues
from src.event_handler import EventHandler
from src.game_config.utils import Draw
from src.game_state_manager import GameStateManager
from src.game_config.global_config import *
from src.screens.game_over import GameOver
from src.screens.main_menu import MainMenu
from src.screens.rules import Rules
from src.screens.questions import Question
from src.screens.suspects import Suspects


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.draw = Draw(self.screen)
        self.clues = Clues()

        self.game_state_manager = GameStateManager("main_menu")

        self.suspects = Suspects(self.screen, self.game_state_manager, self.draw, self.clues)
        self.main_menu = MainMenu(self.screen, self.game_state_manager, self.draw, self.suspects)
        self.rules = Rules(self.screen, self.game_state_manager, self.draw)
        self.game_over = GameOver(self.screen, self.game_state_manager, self.draw)
        self.question = Question(self.screen, self.game_state_manager, self.draw)

        self.states = {
            "main_menu": self.main_menu,
            "rules": self.rules,
            "game_over": self.game_over,
            "question": self.question,
            "suspects": self.suspects,
        }

        self.event_handler = EventHandler(self.game_state_manager, self.suspects)

    def run(self):
        while True:
            self.screen.fill(BLACK)

            # calls the central event handler for any state
            self.event_handler.handle_events()

            # returns current state and runs that state
            self.states[self.game_state_manager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
