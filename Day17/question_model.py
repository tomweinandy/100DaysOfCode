class Question:
    def __init__(self, text, answer):
        """
        :param text: Text of the quiz question
        :type text: str
        :param answer: Answer of the quiz question ('True'/'False')
        :type answer: str
        """
        self.text = text
        self.answer = answer
