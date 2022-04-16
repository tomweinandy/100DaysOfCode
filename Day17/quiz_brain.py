

def convert_t_or_f(old_guess):
    if old_guess == 't':
        new_guess = 'true'
    elif old_guess == 'f':
        new_guess = 'false'
    else:
        new_guess = old_guess
    return new_guess


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.quiz_number = 0

    def ask_question(self):
        # Define question and answer
        question_object = self.question_list[self.quiz_number]
        question = question_object.text

        guess = input(f'Q.{self.quiz_number + 1}: {question} (True/False): ').lower()
        guess = convert_t_or_f(guess)

        while guess not in ['true', 'false']:
            guess = input(f'Q.{quiz_number}: {question} (True/False): ').lower()
            guess = convert_t_or_f(guess)

        return guess


    def check_guess(self, guess):
        # Define answer
        question_object = self.question_list[self.quiz_number]
        answer = question_object.answer
        answer = answer.lower()

        # Check if answer is correct
        if guess == answer:
            correct = True
            self.quiz_number += 1
            print(f'   Correct! Your score is {self.quiz_number}.')
        else:
            correct = False
            print(f'   Incorrect. Your score is {self.quiz_number}.')

        return correct

    # todo checking if at the end of the quiz
    def check_end(self):
        if len(self.question_list) - 1 == self.quiz_number:
            end = True
        else:
            end = False
        return end
