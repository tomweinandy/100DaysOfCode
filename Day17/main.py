from question_model import Question
from data import question_data
from quiz_brain import *

question_list = []
for q in question_data:
    question_list.append(Question(q['text'], q['answer']))


quiz = Quiz(question_list)

quiz.ask_question(0)