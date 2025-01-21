import random


class Clues:

    def __init__(self, murderer):
        self.murderer = murderer

        self.clues = {
            1: f"The murderer has {self.murderer[0]["hair_colour"]} hair",
            2: f"The murderer has {self.murderer[0]["eye_colour"]} eyes",
            3: f"The murderer {self.murderer[0]["wears_glasses"]}",
            4: f"The murderer wears a {self.murderer[0]["shirt_colour"]} shirt",
            5: f"The murderer has {self.murderer[0]["trouser_colour"]} trousers",
            6: f"The murderer has {self.murderer[0]["shoe_colour"]} shoes",
            7: f"The murderer {self.murderer[0]["wears_a_hat"]}",
            8: "The murderer likes to sing in the shower",
            9: "The murderer has a rubber duck",
            10: "The murderer is allergic to peanuts",
        }

        self.remaining_clues = self.clues

    def get_clue(self):
        if self.remaining_clues != {}:
            random_clue_no = random.choice(list(self.remaining_clues))
            selected_clue = self.remaining_clues[random_clue_no]

            # deletes dictionary key:value pair from list of remaining clues
            del self.remaining_clues[random_clue_no]

            # used for testing/debugging
            print("Clues remaining:", self.remaining_clues.keys())
            print(f"CLUE {random_clue_no}: {selected_clue}")
            return selected_clue
        else:
            return "NO MORE CLUES!"


if __name__ == "__main__":
    pass
