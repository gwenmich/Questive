import random

from db.db_utils import DbConnection


class Clues:

    def __init__(self):
        # self.murderer_id = murderer - this needs to be passed in from suspects and details accessed from db
        self.murderer = DbConnection().get_random_suspect()  # this line needs to be removed, and somehow use self.murderer (suspect_id) instead--------

        print(self.murderer[0]["name"])
        print(self.murderer[0]["name"].split())
        print(len(self.murderer[0]["name"].split()[0]))

        self.clues = {
            1: f"The murderers lucky number is {len(self.murderer[0]["name"].split()[0])} like their name length",
            2: f"The murderer has {self.murderer[0]["hair_colour"]} hair",
            3: f"The murderer has {self.murderer[0]["eye_colour"]} eyes",
            4: f"The murderer {self.murderer[0]["wears_glasses"]}",
            5: f"The murderer wears a {self.murderer[0]["shirt_colour"]} shirt",
            6: f"The murderer has {self.murderer[0]["trouser_colour"]} trousers",
            7: f"The murderer has {self.murderer[0]["shoe_colour"]} shoes",
            8: f"The murderer {self.murderer[0]["wears_a_hat"]}",
            9: "Unhelpful clue 1",
            10: "Unhelpful clue 2",
            11: "Unhelpful clue 3",
            12: "Unhelpful clue 4"
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
