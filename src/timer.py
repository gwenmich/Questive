import time
from src.game_config.global_config import MEDIUM_FONT


class Timer:
    def __init__(self, draw):
        self.draw = draw
        self.start_time = None

    # starts the timer when called
    def start_timer(self):
        self.start_time = time.time()

    # draws time remaining to screen counting up
    def draw_timer(self):
        elapsed_time = time.time() - self.start_time
        seconds = int(elapsed_time % 60)
        minutes = seconds // 60  # rounds down to nearest integer

        # displays timer with 2 digits for minutes and seconds
        self.draw.render_text(f"{minutes:02}:{seconds:02}", MEDIUM_FONT, (100, 50))


if __name__ == "__main__":
    pass
