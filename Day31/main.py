"""
Day 31: Flashcard
"""
import tkinter

BACKGROUND_COLOR = "#B1DDC6"

FRONT_IMAGE_PATH = 'images/card_front.png'
RIGHT_IMAGE_PATH = 'images/right.png'
WRONG_IMAGE_PATH = 'images/wrong.png'

TITLE_TEXT_FONT = ('Ariel', 40, 'italic')
WORD_TEXT_FONT = ('Ariel', 60, 'bold')


def mark_right():
    pass


def mark_wrong():
    pass


# Initialize window and canvas
window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Add card front image
front_image = tkinter.PhotoImage(file=FRONT_IMAGE_PATH)
canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Add buttons
wrong_image = tkinter.PhotoImage(file=WRONG_IMAGE_PATH)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=mark_right)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file=RIGHT_IMAGE_PATH)
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=mark_right)
right_button.grid(row=1, column=1)

# Add text
title_label = tkinter.Label(text='French', justify='center', font=TITLE_TEXT_FONT)
title_label.place(x=330, y=150)

word = 'Word'
x_offset = 380 - 13.5*len(word)  # offset a function of word length
title_label = tkinter.Label(text=word, justify='center', font=WORD_TEXT_FONT)
title_label.place(x=x_offset, y=263)




tkinter.mainloop()