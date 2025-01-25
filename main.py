from db.db_utils import DbConnection
from src.clues import Clues
from src.game_config.utils import *
from src.game_state_manager import GameStateManager
from src.game_config.global_config import *
from src.screens.arrest_suspect import ArrestSuspect
from src.screens.game_lost import GameLost
from src.screens.game_won import GameWon
from src.screens.main_menu import MainMenu
from src.screens.rules import Rules
from src.screens.questions import Question
from src.screens.suspects import Suspects
from src.timer import Timer
from src.screens.wrong_answer import WrongAnswer


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Questive")
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager("main_menu")

        self.murderer = DbConnection().get_murderer()
        self.clues = Clues(self.murderer)
        self.draw = Draw(self.screen)
        self.button_handler = ButtonHandler(self.game_state_manager, self.screen)
        self.timer = Timer(self.draw)

        self.main_menu = MainMenu(self.screen, self.game_state_manager, self.draw)
        self.rules = Rules(self.screen, self.game_state_manager, self.draw, self.timer)
        self.question = Question(self.screen, self.game_state_manager, self.draw, self.timer)
        self.wrong_answer = WrongAnswer(self.screen, self.game_state_manager, self.draw, self.timer, self.question,
                                        self.button_handler)
        self.suspects = Suspects(self.screen, self.game_state_manager, self.draw, self.timer, self.question, self.clues,
                                 self.murderer,
                                 self.button_handler)
        self.arrest_suspect = ArrestSuspect(self.screen, self.game_state_manager, self.draw, self.timer,
                                            self.button_handler, self.suspects)
        self.game_lost = GameLost(self.screen, self.game_state_manager, self.draw)
        self.game_won = GameWon(self.screen, self.game_state_manager, self.draw)

        self.states = {
            "main_menu": self.main_menu,
            "rules": self.rules,
            "question": self.question,
            "wrong_answer": self.wrong_answer,
            "suspects": self.suspects,
            "arrest_suspect": self.arrest_suspect,
            "game_won": self.game_won,
            "game_lost": self.game_lost
        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_app()

            self.screen.fill(BLACK)

            # returns current state and runs that state
            self.states[self.game_state_manager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
