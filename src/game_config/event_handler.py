class EventHandler:
    def __init__(self):
        self.active_clue = ""

    def set_clue(self, clue):
        self.active_clue = clue

    def get_clue(self):
        return self.active_clue
