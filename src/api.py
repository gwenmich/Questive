import requests
import html


class ApiData:

    def __init__(self, no_questions, difficulty):
        self.endpoint = f"https://opentdb.com/api.php?amount={no_questions}&category=9&difficulty={difficulty}"
        self.response = requests.get(self.endpoint)
        self.data = self.response.json()

    def decode_strings(self):
        for question in self.data["results"]:
            question["question"] = html.unescape(question["question"])
            question["correct_answer"] = html.unescape(question["correct_answer"])
            question["incorrect_answers"] = [html.unescape(ans) for ans in question["incorrect_answers"]]
        return self.data


# test data
# data = {
#     'response_code': 0,
#     'results': [
#         {'type': 'multiple',
#          'difficulty': 'medium',
#          'category': 'General Knowledge',
#          'question': 'Dihydrogen monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water what do you think?',
#          'correct_answer': 'F&ouml;nster which is the equivalent of window in swedish and I love Ikea',
#          'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},
#
#         {'type': 'boolean',
#          'difficulty': 'easy',
#          'category': 'Science: Computers',
#          'question': 'Pointers were not used in the original C programming language; they were added later on in C++.',
#          'correct_answer': 'False',
#          'incorrect_answers': ['True']}
#     ]
# }


if __name__ == "__main__":
    pass
