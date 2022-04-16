import html.parser

def convert_t_or_f(old_guess):
    """
    Helper function that makes string inputs lowercase (if possible) and converts t (f) to true (false)
    :param old_guess: Input
    :return: formatted input
    """
    if type(old_guess) == str:
        old_guess = old_guess.lower()
    if old_guess == 't':
        new_guess = 'true'
    elif old_guess == 'f':
        new_guess = 'false'
    else:
        new_guess = old_guess
    return new_guess


class QuizBrain:
    def __init__(self, question_list):
        """
        Initialize the class object
        :param question_list: list of initialized questions from question_model.py
        """
        self.question_list = question_list
        self.quiz_number = 0

    def ask_question(self):
        """
        Uses the current quiz_number to generate a question
        :return: The player's guess for that question
        """
        # Define question and answer
        question_object = self.question_list[self.quiz_number]
        question = question_object.text
        question = html.unescape(question)  # resolves html encoding issue

        # Forces answer to be true or false
        guess = 'pass'
        while guess not in ['true', 'false']:
            guess = input(f'Q.{self.quiz_number + 1}: {question} (True/False): ')
            guess = convert_t_or_f(guess)

        return guess


    def check_guess(self, guess):
        """
        Checks if the guess entered matches the answer
        :param guess: The input added from the player about a question
        :type guess: str
        :return: Boolean of whether answer is correct
        """
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
            print(f'   Incorrect. Your final score is {self.quiz_number}.')

        return correct

    def check_end(self):
        """
        Checks whether we are at the last question of the question list
        :return: Boolean
        """
        # Shift number by 1 to account for base-zero of list
        if len(self.question_list) - 1 == self.quiz_number:
            end = True
        else:
            end = False
        return end
