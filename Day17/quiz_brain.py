

def convert_t_or_f(old_guess):
    if old_guess == 't':
        new_guess = 'true'
    elif old_guess == 'f':
        new_guess = 'false'
    else:
        new_guess = old_guess
    return new_guess

class Quiz:
    def __init__(self, question_list):
        self.question_list = question_list
        self.quiz_number = 0

    # todo ask questions
    def ask_question(self, quiz_number):
        question_object = self.question_list[quiz_number]
        question = question_object.text
        guess = input(f'{question} (True/False): ').lower()
        guess = convert_t_or_f(guess)

        while guess not in ['true', 'false']:
            guess = input(f'{question} (True/False): ').lower()
            guess = convert_t_or_f(guess)


# todo checking if the answer is correct


# todo checking if at the end of the quiz