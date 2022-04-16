from question_model import Question
from data import question_data
from quiz_brain import *

question_list = []
for q in question_data:
    question_list.append(Question(q['text'], q['answer']))


quiz = QuizBrain(question_list)
correct = True

while correct and not quiz.check_end():

    guess = quiz.ask_question()
    correct = quiz.check_guess(guess)
