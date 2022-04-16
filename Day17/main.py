from question_model import Question
from data import question_data

question_list = []
for q in question_data:
    question_list.append(Question(q['text'], q['answer']))

print(question_list)