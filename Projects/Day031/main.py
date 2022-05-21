"""
Day 31: Flash Card App
"""
import tkinter
import pandas as pd
import random
from tkinter import messagebox

# Define variables
BACKGROUND_COLOR = "#B1DDC6"

FRONT_IMAGE_PATH = 'images/card_front.png'
BACK_IMAGE_PATH = 'images/card_back.png'
WRONG_IMAGE_PATH = 'images/wrong.png'
VIEW_IMAGE_PATH = 'images/view.png'
RIGHT_IMAGE_PATH = 'images/right.png'
DATA_PATH = 'data/french_words.csv'

FRONT_TITLE_TEXT = 'French'
BACK_TITLE_TEXT = 'English'

TITLE_TEXT_FONT = ('Ariel', 40, 'italic')
ITEM_TEXT_FONT = ('Ariel', 60, 'bold')

card_status_front = True


# Set definitions
def add_data(data_path):
    """
    Read in data and create a column where the status of each item is 'Unknown'
    :param data_path: path to csv file with first column as the item to be placed on the front of the card and the
    second column the item to be placed on the back.
    :return: Dataframe with a 'Status' column (if one did not previously exist)
    """
    data = pd.read_csv(data_path)

    if 'Status' not in data.columns:
        data['Status'] = 'Unknown'

    return data


def select_random_unknown_item(data):
    """
    Select a random item from the dataframe that has an 'Unknown' status
    :param data: dataframe read in using add_data()
    :return: 1) randomly selected index, 2) corresponding item for the card front, 3) corresponding item for card back
    """
    front_card_col = df.columns[0]
    back_card_col = df.columns[1]
    data_unknown = data[data['Status'] == 'Unknown']
    data_unknown = data_unknown.reset_index(drop=True)

    random_idx = random.randint(0, len(data_unknown)-1)
    random_item = df.iloc[random_idx]

    random_front_item = random_item[front_card_col]
    random_back_item = random_item[back_card_col]

    return random_idx, random_front_item, random_back_item


def flip_card():
    """
    Flips the card to back (if on front) or front (if on back). Changes card_status_front accordingly.
    """
    global card_status_front

    if card_status_front:
        canvas.itemconfig(canvas_image, image=back_image)
        canvas.itemconfig(title_text, text=BACK_TITLE_TEXT, fill='white')
        canvas.itemconfig(item_text, text=back_item, fill='white')
        card_status_front = False

    else:
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(title_text, text=FRONT_TITLE_TEXT, fill='black')
        canvas.itemconfig(item_text, text=front_item, fill='black')
        card_status_front = True


def get_new_card():
    """
    Selects a new item from the dataframe and shows the front of the card.
    """
    global idx, front_item, back_item, card_status_front
    idx, front_item, back_item = select_random_unknown_item(df)

    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, text=FRONT_TITLE_TEXT, fill='black')
    canvas.itemconfig(item_text, text=front_item, fill='black')
    card_status_front = True


def mark_right():
    """
    Changes the status of that item to 'Known' and gets next card. NOTE: result is only saved into csv if prompted at
    end of session.
    """
    # Mark word as 'known'
    global idx, DATA_PATH
    df.iloc[idx]['Status'] = 'Known'
    get_new_card()


def quit_app():
    """
    Prompts the user if they want to save the session's results, then quits the window.
    """
    # Ask if results today should be saved
    save_results = messagebox.askyesno(message='Want to save your progress?')
    if save_results:
        df.to_csv(DATA_PATH)
        print('Saved progress')
    else:
        print('Did not save progress')

    window.destroy()


# Read in dataset
df = add_data(DATA_PATH)
idx, front_item, back_item = select_random_unknown_item(df)

# Initialize window and canvas
window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Define front and back image
front_image = tkinter.PhotoImage(file=FRONT_IMAGE_PATH)
back_image = tkinter.PhotoImage(file=BACK_IMAGE_PATH)

# Add front image
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=1, column=0, columnspan=3)

# Add front text
title_text = canvas.create_text(400, 150, text=FRONT_TITLE_TEXT, font=TITLE_TEXT_FONT)
item_text = canvas.create_text(400, 263, text=front_item, font=ITEM_TEXT_FONT)

# Add wrong button
wrong_image = tkinter.PhotoImage(file=WRONG_IMAGE_PATH)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=get_new_card)
wrong_button.grid(row=2, column=0)

# Add view button
view_image = tkinter.PhotoImage(file=VIEW_IMAGE_PATH)
view_button = tkinter.Button(image=view_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=flip_card)
view_button.grid(row=2, column=1)

# Add right button
right_image = tkinter.PhotoImage(file=RIGHT_IMAGE_PATH)
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=mark_right)
right_button.grid(row=2, column=2)

# Add quit button
quit_button = tkinter.Button(text='Quit', bg=BACKGROUND_COLOR, highlightthickness=0, command=quit_app)
quit_button.grid(row=0, column=4)

tkinter.mainloop()
