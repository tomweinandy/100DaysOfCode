"""
Day 31: Flash Card App
"""
import tkinter
import pandas as pd
import random

# Define constant variables
BACKGROUND_COLOR = "#B1DDC6"

FRONT_IMAGE_PATH = 'images/card_front.png'
RIGHT_IMAGE_PATH = 'images/right.png'
WRONG_IMAGE_PATH = 'images/wrong.png'
DATA_PATH = 'data/french_words.csv'

FRONT_TITLE_TEXT = 'French'
BACK_TITLE_TEXT = 'English'

TITLE_TEXT_FONT = ('Ariel', 40, 'italic')
ITEM_TEXT_FONT = ('Ariel', 60, 'bold')


# Set definitions
def add_data(data_path):
    data = pd.read_csv(data_path)
    data['Status'] = 'Unknown'
    return data


def select_random_unknown_item(data):
    front_card_col = df.columns[0]
    back_card_col = df.columns[1]
    data_unknown = data[data['Status'] == 'Unknown']

    random_idx = random.randint(0, len(data_unknown)-1)
    random_item = df.iloc[random_idx]

    random_front_item = random_item[front_card_col]
    random_back_item = random_item[back_card_col]

    return random_idx, random_front_item, random_back_item


def mark_right():
    idx, front_item, back_item = select_random_unknown_item(df)
    canvas.itemconfig(front_item_text, text=front_item)


def mark_wrong():
    idx, front_item, back_item = select_random_unknown_item(df)
    canvas.itemconfig(front_item_text, text=front_item)


# Read in dataset
df = add_data(DATA_PATH)
idx, front_item, back_item = select_random_unknown_item(df)
print(idx)
print(front_item)
print(back_item)


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

# Add text
front_title_text = canvas.create_text(400, 150, text=FRONT_TITLE_TEXT, font=TITLE_TEXT_FONT)
front_item_text = canvas.create_text(400, 263, text=front_item, font=ITEM_TEXT_FONT)

# Add buttons
wrong_image = tkinter.PhotoImage(file=WRONG_IMAGE_PATH)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=mark_right)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file=RIGHT_IMAGE_PATH)
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=mark_right)
right_button.grid(row=1, column=1)






tkinter.mainloop()