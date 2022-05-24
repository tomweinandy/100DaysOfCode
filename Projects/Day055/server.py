"""
Day 55: HTML & URL parsing in Flask

Quickstart documentation: https://flask.palletsprojects.com/en/2.1.x/quickstart/
"""
from flask import Flask
import random

app = Flask(__name__)

# def make_bold(function):
#     def bold_wrapper():
#         return f"<b>{function()}</b>"
#     return bold_wrapper

guess_gif = 'https://media2.giphy.com/media/3o6vXUgVMtK64QAezK/giphy.gif'
correct_gif = 'https://media.giphy.com/media/pwBi3YrGypMyI/giphy.gif'
wrong_gifs = ['https://media.giphy.com/media/l0MYH5mkQJAxVShqM/giphy.gif',
              'https://media.giphy.com/media/3ohzdRmJspKrpKjL5C/giphy.gif',
              'https://media.giphy.com/media/3ohze456U9AIzUbex2/giphy.gif',
              'https://media.giphy.com/media/nWCf6ZPW0mRMY/giphy.gif',
              'https://media.giphy.com/media/99tonvXLKv3vG/giphy.gif',
              'https://media.giphy.com/media/l4FGqFsIccGAiLmkE/giphy.gif']
random_number = random.choice(range(0, 10))


def check_answer(number, guess):
    if guess < number:
        html = "<h1>Your guess was too low. Try again." \
               "<br></br>" \
               f"<center><img src={random.choice(wrong_gifs)} width=400</img></center>"

    elif guess > number:
        html = "<h1>Your guess was too high. Try again." \
               "<br></br>" \
               f"<center><img src={random.choice(wrong_gifs)} width=400</img></center>"

    elif guess == number:
        html = "<h1>Correct. You nailed it!" \
               "<br></br>" \
               f"<center><img src={correct_gif} width=400</img></center>"

    else:
        html = "<h1>Invalid input. Please try again with a number from 0-9." \
               "<br></br>" \
                f"<center><img src={random.choice(wrong_gifs)} width=400</img></center>"

    return html


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<p>In the browser, type '/' followed by your guess to see if you are right </p>" \
           "<br></br>" \
           "<br></br>" \
           f"<center><img src={guess_gif} width=400</img></center>"


@app.route("/<guess>")
def check_answer(guess):
    return f"Hello there, {guess}!"


if __name__ == '__main__':
    app.run(debug=True)

# # Create the logging_decorator() function 👇
# def logging_decorator(function):
#     def wrapper(*args):
#         print(f'You called: {function.__name__}')
#         result = function(args[0], args[1], args[2])
#         print(f'It returned: {result}')

#     return wrapper


# # Use the decorator 👇
# @logging_decorator
# def a_function(a, b, c):
#     return a + b + c


# a_function(1, 2, 3)
