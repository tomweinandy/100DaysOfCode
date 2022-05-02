import tkinter
from quiz_brain import QuizBrain

# Define variables
THEME_COLOR = "#375362"
SCORE_FONT = ('Arial', 16, 'normal')
QUESTION_FONT = ('Arial', 20, 'italic')
TRUE_IMAGE_PATH = 'images/true.png'
FALSE_IMAGE_PATH = 'images/false.png'


class QuizInterface:
    """
    Build UI class to generate and update the popup window
    """
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Initialize window and canvas
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, bg=THEME_COLOR)
        self.canvas = tkinter.Canvas(width=300, height=250)

        # Add score
        self.score_text = tkinter.Label(text=f'Score: {quiz_brain.score}', fg='white', bg=THEME_COLOR, pady=20, font=SCORE_FONT)
        self.score_text.grid(row=0, column=1)

        # Add canvas with question
        self.question_text = self.canvas.create_text(150, 125, width=280, text='Question', font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Add true, false buttons
        true_image = tkinter.PhotoImage(file=TRUE_IMAGE_PATH)
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file=FALSE_IMAGE_PATH)
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)

        # Get next question
        self.get_next_question()

        # Keep popup open
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def click_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
        self.score_text.config(text=f'Score: {self.quiz.score}')

    def click_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        self.score_text.config(text=f'Score: {self.quiz.score}')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
