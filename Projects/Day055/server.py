"""
Day 55: High Low Game using HTML & URL parsing in Flask

Quickstart documentation: https://flask.palletsprojects.com/en/2.1.x/quickstart/
"""
from flask import Flask
import random

app = Flask(__name__)

# Define gifs and random number
guess_gif = 'https://media2.giphy.com/media/3o6vXUgVMtK64QAezK/giphy.gif'
correct_gif = 'https://media.giphy.com/media/pwBi3YrGypMyI/giphy.gif'
wrong_gifs = ['https://media.giphy.com/media/l0MYH5mkQJAxVShqM/giphy.gif',
              'https://media.giphy.com/media/3ohzdRmJspKrpKjL5C/giphy.gif',
              'https://media.giphy.com/media/3ohze456U9AIzUbex2/giphy.gif',
              'https://media.giphy.com/media/nWCf6ZPW0mRMY/giphy.gif',
              'https://media.giphy.com/media/99tonvXLKv3vG/giphy.gif',
              'https://media.giphy.com/media/l4FGqFsIccGAiLmkE/giphy.gif']
number = random.choice(range(0, 10))


@app.route("/")
def hello_world():
    """
    Generates a landing page for the number guessing game.
    :return: html code to generate the page
    """
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<p>In the browser, type '/' followed by your guess to see if you are right </p>" \
           "<br></br>" \
           "<br></br>" \
           f"<center><img src={guess_gif} width=400</img></center>"


@app.route("/<guess_string>")
def check_answer(guess_string):
    """
    Generates a saying whether a guess was too low, too high, correct, or invalid
    :param guess_string: the numeric guess
    :return: html to generate the page
    """
    guess = int(guess_string)
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


# Run Flask
if __name__ == '__main__':
    app.run(debug=True)
