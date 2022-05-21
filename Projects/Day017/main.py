"""
Day 17: True/False Quiz

This is currently set up to support geography-related questions. See Day034 for Part II.
"""
from question_model import Question
from data import *
from quiz_brain import *
import random

# Continue for multiple games, if desired
proceed = True
while proceed:

    # Generate list of initialized questions
    question_list = []
    for q in question_data_geography['results']:
        question_list.append(Question(q['question'], q['correct_answer']))
    random.shuffle(question_list)

    # Initialize Quiz
    quiz = QuizBrain(question_list)
    correct = True

    # Begin quiz
    while correct and not quiz.check_end():
        guess = quiz.ask_question()
        correct = quiz.check_guess(guess)

    # Ask if player wants to play again
    play_again = input('\nPlay again? (True/False): ')
    print('\n')
    play_again = convert_t_or_f(play_again)

    if play_again == 'false':
        proceed = False

print('The end.')
