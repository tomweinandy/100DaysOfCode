import tkinter

THEME_COLOR = "#375362"
SCORE_FONT = ('Arial', 16, 'normal')
QUESTION_FONT = ('Arial', 20, 'italic')

TRUE_IMAGE_PATH = 'images/true.png'
FALSE_IMAGE_PATH = 'images/false.png'


class QuizInterface:

    def __init__(self):
        # Initialize window and canvas
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, bg=THEME_COLOR)
        self.canvas = tkinter.Canvas(width=300, height=250)

        # Add score
        self.score_text = tkinter.Label(text=f'Score: ', fg='white', bg=THEME_COLOR, pady=20, font=SCORE_FONT)
        self.score_text.grid(row=0, column=1)

        # Add canvas with question
        self.question_text = self.canvas.create_text(100, 100, text='Question', font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Add true, false buttons
        self.true_image = tkinter.PhotoImage(file=TRUE_IMAGE_PATH)
        self.true_button = tkinter.Button(image=self.true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)

        self.false_image = tkinter.PhotoImage(file=FALSE_IMAGE_PATH)
        self.false_button = tkinter.Button(image=self.false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)

        # Keep popup open
        self.window.mainloop()

    def click_true(self):
        print('True clicked')

    def click_false(self):
        print('False clicked')
