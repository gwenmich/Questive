class GettersSetters:
    def __init__(self):
        self.active_clue = ""
        self.wrong_answer_text = ""

    def set_clue(self, clue):
        self.active_clue = clue

    def get_clue(self):
        return self.active_clue

    def set_wrong_answer_text(self, text):
        self.wrong_answer_text = text

    def get_wrong_answer_text(self):
        return self.wrong_answer_text
