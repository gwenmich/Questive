import sys
import pygame


# central event handler that manages all state key and mouse options
class EventHandler:
    def __init__(self, game_state_manager, timer, suspects):
        self.game_state_manager = game_state_manager
        self.timer = timer
        self.suspects = suspects

        # mouse position and pressed status
        self.mouse_position = pygame.mouse.get_pos()
        self.mouse_pressed = pygame.mouse.get_pressed()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # probably don't need most of this code below - maybe put event handler logic
            # in main.py run method? To discuss tomorrow

            # ----- CHANGE TO MOUSE/BUTTON PRESSES-------
            if event.type == pygame.KEYDOWN:
                if self.game_state_manager.get_state() == "main_menu":
                    if event.key == pygame.K_RETURN:
                        self.game_state_manager.set_state("rules")

                elif self.game_state_manager.get_state() == "rules":
                    if event.key == pygame.K_RETURN:
                        self.game_state_manager.set_state("question")
                        self.timer.start_timer()

                elif self.game_state_manager.get_state() == "question":
                    if event.key == pygame.K_BACKSPACE:
                        self.game_state_manager.set_state("main_menu")
                    if event.key == pygame.K_RETURN:
                        self.game_state_manager.set_state("suspects")

                elif self.game_state_manager.get_state() == "suspects":
                    if event.key == pygame.K_RETURN:
                        self.suspects.active_clue = ""
                        self.game_state_manager.set_state("question")
                # added temporarily until discussion
                elif self.game_state_manager.get_state() == "wrong_answer":
                    if event.key == pygame.K_RETURN:
                        self.suspects.active_clue = ""
                        self.game_state_manager.set_state("question")


if __name__ == "__main__":
    pass
