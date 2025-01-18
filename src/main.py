import pygame

from src.event_handler.event_handler import EventHandler
from src.game_state.game_state_manager import GameStateManager
from src.game_config.global_config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.screens.game_over import GameOver
from src.screens.game_play import GamePlay
from src.screens.main_menu import MainMenu
from src.screens.rules import Rules

from src.screens.questions import Question
from src.screens.categories import Category
from src.screens.clues import Clue


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager("main_menu")
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.rules = Rules(self.screen, self.game_state_manager)
        self.game_play = GamePlay(self.screen, self.game_state_manager)
        self.game_over = GameOver(self.screen, self.game_state_manager)

        self.question = Question(self.screen, self.game_state_manager)
        # self.category = Category(self.screen, self.game_state_manager) not using for now
        self.clue = Clue(self.screen, self.game_state_manager)

        self.states = {
            "main_menu": self.main_menu,
            "rules": self.rules,
            "game_play": self.game_play,
            "game_over": self.game_over,
            # "category" : self.category, not using for now
            "question" : self.question,
            "clue" : self.clue,
            "suspects" : self.suspects # get these from db_utils
        }

        self.event_handler = EventHandler(self.game_state_manager)

    def run(self):
        while True:
            # calls the central event handler for any state
            self.event_handler.handle_events()

            # returns current state and runs that state
            self.states[self.game_state_manager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
