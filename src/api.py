import requests
import html


endpoint = "https://opentdb.com/api.php?amount=10"
response = requests.get(endpoint)
# data = response.json()

# test data
data = {
    'response_code': 0,
    'results': [
        {'type': 'multiple',
         'difficulty': 'medium',
         'category': 'General Knowledge',
         'question': 'What is the Swedish word for &quot;window&quot;?',
         'correct_answer': 'F&ouml;nster',
         'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},

        {'type': 'boolean',
         'difficulty': 'easy',
         'category': 'Science: Computers',
         'question': 'Pointers were not used in the original C programming language; they were added later on in C++.',
         'correct_answer': 'False',
         'incorrect_answers': ['True']}
    ]
}

def decode_strings():

    for question in data["results"]:
        question["category"] = html.unescape(question["category"])
        question["question"] = html.unescape(question["question"])
        question["correct_answer"] = html.unescape(question["correct_answer"])
        question["incorrect_answers"] = [html.unescape(ans) for ans in question["incorrect_answers"]]
    return data


decode_strings()
questions = data["results"]
