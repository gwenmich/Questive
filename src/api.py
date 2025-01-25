import requests
import html


# class ApiData:

    # def __init__(self):
    #     self.endpoint = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy"
    #     self.response = requests.get(self.endpoint)
    #     self.data = self.response.json()

endpoint = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy"
response = requests.get(endpoint)
data = response.json()


def decode_strings():
    for question in data["results"]:
        question["question"] = html.unescape(question["question"])
        question["correct_answer"] = html.unescape(question["correct_answer"])
        question["incorrect_answers"] = [html.unescape(ans) for ans in question["incorrect_answers"]]
    return data


# test data
# data = {
#     'response_code': 0,
#     'results': [
#         {'type': 'multiple',
#          'difficulty': 'medium',
#          'category': 'General Knowledge',
#          'question': 'What is the Swedish word for &quot;window&quot; and what is the most famous swedish outlet for buying furniture?',
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
