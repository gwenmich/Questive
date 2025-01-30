import time
from src.game_config.global_config import MEDIUM_FONT


class Timer:
    def __init__(self, draw):
        self.draw = draw
        self.start_time = None
        self.current_time = ""
        self.timer_running = False

    # starts the timer when called
    def start_timer(self):
        self.start_time = time.time()
        self.timer_running = True

    # draws time remaining to screen counting up
    def draw_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            seconds = int(elapsed_time % 60)
            minutes = int(elapsed_time // 60)  # rounds down to nearest integer
            self.current_time = f"{minutes:02}:{seconds:02}"
            # displays timer with 2 digits for minutes and seconds
        self.draw.render_text(str(self.current_time), MEDIUM_FONT, (100, 50))
        self.set_time(self.current_time)

    def set_time(self, current_time):
        self.current_time = current_time

    def get_time(self):
        return self.current_time


if __name__ == "__main__":
    pass
