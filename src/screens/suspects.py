import pygame
from db.db_utils import DbConnection
from src.game_config.global_config import SMALL_FONT


class Suspects:
    def __init__(self, screen, game_state_manager, draw, murderer):
        self.screen = screen
        self.game_state_manager = game_state_manager
        self.draw = draw
        self.murderer = murderer
        self.suspects = DbConnection().get_suspects()

    def draw_suspect(self, suspect, x, y, n):
        self.draw.render_text(suspect["name"], SMALL_FONT, (x, y))
        suspect_img = pygame.image.load(f"assets/images/suspects/{n}.png").convert_alpha()
        suspect_img.set_alpha(suspect["alpha"])  # draw suspect with current alpha value
        suspect_img_rect = suspect_img.get_rect(topleft=(x - 60, y - 140))
        self.screen.blit(suspect_img, suspect_img_rect)
        return suspect_img_rect

    # method also used in arrest_suspect
    def draw_suspects(self):
        n = 0
        x_starting_pos = 235
        x = x_starting_pos
        y = 350
        suspects_per_row = 5

        for suspect in self.suspects:
            if n < suspects_per_row:
                pass
            elif n == 5:
                x, y = x_starting_pos, 550

            suspect_img_rect = self.draw_suspect(suspect, x, y, n)
            x += 200
            n += 1

            suspect["suspect_img_rect"] = suspect_img_rect
        pygame.display.update()

    # Checks if user clicks on image
    def check_button_pressed(self):
        position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for suspect in self.suspects:
                    if suspect["suspect_img_rect"].collidepoint(position):
                        if self.game_state_manager.get_state() == "correct_answer":
                            self.suspect_press(suspect)
                        elif self.game_state_manager.get_state() == "arrest_suspect":
                            self.murderer_guess(suspect, position)

    # Changes transparency when suspect clicked
    @staticmethod
    def suspect_press(suspect):
        if suspect["alpha"] == 255:
            suspect["alpha"] = 100  # Fade the suspect
        else:
            suspect["alpha"] = 255  # Bring the suspect back to full opacity

    # Checks if player has arrested the murderer
    def murderer_guess(self, suspect, position):
        if suspect["suspect_img_rect"].collidepoint(position):
            if self.murderer[0]["suspect_id"] == suspect["suspect_id"]:
                print("The murder has been caught!")
                self.game_state_manager.set_state("game_won")
            else:
                print("Incorrect arrest")
                self.game_state_manager.set_state("game_lost")


if __name__ == "__main__":
    pass
