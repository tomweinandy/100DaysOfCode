"""
Day 85: Typing Speed Desktop App
"""
import tkinter
from tkinter import scrolledtext
import re

# ---------------------------- VARIABLES ------------------------------- #
ORANGE = "#ed7014"
FONT_NAME = "Arial"
TIME = 120


with open("arrested_development_synopses.txt") as file:
    synopses = file.read()


# ---------------------------- PROCESS TEXT ------------------------------- #
def wordify(txt):
    # Remove apostrophes
    txt = txt.replace('\'', '')

    # Remove all characters except letters and whitespaces
    txt = re.sub(r'[^a-zA-Z ]', ' ', txt)

    txt = txt.lower()
    word_list = txt.split()

    return word_list


# ---------------------------- SCORE TEXT ------------------------------- #
def score_typing(attempted_text, original_text):
    matches = 0

    original = wordify(original_text)
    attempted = wordify(attempted_text)

    # Assign a point for each matched word between lists
    for i in range(len(attempted)):
        if attempted[i] == original[i]:
            matches += 1

    # Divide matches by two (the minutes to complete the task) to get words per minute
    score = matches/2
    display_results(score)


# ---------------------------- SHOW SCORE ------------------------------- #
def display_results(n):
    global start_button, score_label

    # Clear objects on UI
    synopses_label.destroy()
    text_area.destroy()

    # Add Try Again button
    start_button = tkinter.Button(text='Try Again', command=start_timer, font=FONT_NAME)
    start_button.grid(row=2, columnspan=2)

    # Display results
    score_text = f'You type at a speed of {n} words per minute.'
    score_label = tkinter.Label(text=score_text, bg='white', fg=ORANGE, font=(FONT_NAME, 18))
    score_label.grid(row=3, columnspan=2)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global text_area, synopses_label

    # Clear items in UI
    start_button.destroy()
    try:
        score_label.destroy()
    except:
        pass

    # Give user two minutes to complete the task
    countdown(TIME)

    # Add text from story to be copied
    synopses_label = tkinter.Label(text=synopses, bg='white', fg='black', pady=10, font=(FONT_NAME, 15))
    synopses_label.grid(row=3, column=0)

    # Add text box
    text_area = scrolledtext.ScrolledText(window,
                                          wrap=tkinter.WORD,
                                          width=60,
                                          height=32,
                                          background='white',
                                          font=(FONT_NAME, 15))

    text_area.grid(row=3, column=1, pady=10, padx=10)

    # Placing cursor in the text area
    text_area.focus()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """
    Changes the countdown timer
    :param count: How many seconds to count down from
    """
    global timer

    minutes_left = str(count // 60)
    seconds_left = str(count % 60)
    if len(seconds_left) == 1:
        seconds_left = '0' + seconds_left

    new_time = f'{minutes_left}:{seconds_left}'
    canvas.itemconfig(timer_text, text=new_time)
    if count > 0:
        timer = window.after(1000, countdown, count-1)  # time is in milliseconds, so 1000ms = 1 second
    else:
        # Score input after time runs out
        input = text_area.get("1.0", "end-1c")
        score_typing(input, synopses)


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Typing Speed Test')
window.config(padx=10, pady=10, bg='white')  # bg is 'background'


# Add timer label
label = 'Type as much as you can in two minutes. Spelling counts.\n' \
        'There is no penalty for missed punctuation or capitalization.\n' \
        'Press "start" to reveal text and begin.'
timer_label = tkinter.Label(text=label, bg='white', fg=ORANGE, font=(FONT_NAME, 18))
timer_label.grid(row=0, columnspan=2)
canvas = tkinter.Canvas(width=1200, height=75, bg='white', highlightthickness=0)

# Add timer text
timer_text = canvas.create_text(600, 30, text='2:00', fill=ORANGE, font=(FONT_NAME, 36))
canvas.grid(row=1, columnspan=2)

# Add start button
start_button = tkinter.Button(text='Start', command=start_timer, font=FONT_NAME)
start_button.grid(row=2, columnspan=2)

# Add main while loop to keep window open
window.mainloop()
