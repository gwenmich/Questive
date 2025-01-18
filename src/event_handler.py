import sys
import pygame


# central event handler that manages all state key and mouse options
class EventHandler:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if self.game_state_manager.get_state() == "main_menu":
                    if event.key == pygame.K_RETURN:
                        self.game_state_manager.set_state("question")

                elif self.game_state_manager.get_state() == "question":
                    if event.key == pygame.K_BACKSPACE:
                        self.game_state_manager.set_state("main_menu")


if __name__ == "__main__":
    pass
