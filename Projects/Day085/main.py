"""
Day 85: Typing Speed Desktop App
"""
# with open("the_cask_of_amontillado.txt") as file:
with open("arrested_development_synopses.txt") as file:
    synopses = file.read()

import tkinter
from tkinter import scrolledtext
import re


# ---------------------------- VARIABLES ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
YELLOW = "white"
ORANGE = "#ed7014"
FONT_NAME = "Arial"

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked():
    """
    Resets global variables and features of timer
    """
    global reps, checkmarks
    reps = 0
    checkmarks = ''
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    checks.config(text=checkmarks)


def wordify(txt):
    txt = txt.replace('\'', '')
    txt = re.sub(r'[^a-zA-Z0-9 ]', ' ', txt)
    txt = txt.lower()

    word_list = txt.split()
    return word_list


def score_typing(attempted_text, original_text):
    matches = 0

    original = wordify(original_text)
    attempted = wordify(attempted_text)

    for i in range(len(attempted)):
        if attempted[i] == original[i]:
            matches += 1

    return matches/2


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Tracks reps and begins timer according to current rep
    """
    # global reps, checkmarks
    # reps += 1

    # # If reps = 8, 16...
    # if reps % 8 == 0:
    #     countdown(100)
    #     new_label = 'Break Time'
    #     timer_label.config(text=new_label, fg=RED)
    #
    #     checkmarks += checkmark + '\n'
    #     checks.config(text=checkmarks)

    # # If reps = 2, 4, 6, 10, 12, 14...
    # elif reps % 2 == 0:
    #     countdown(10)
    #     new_label = 'Break Time'
    #     timer_label.config(text=new_label, fg=PINK)
    #
    #     checkmarks += checkmark
    #     checks.config(text=checkmarks)

    # If reps = 1, 3, 5, 7, 9, 11, 13, 15, 17...
    # else:
    countdown(12)
    # new_label = 'Begin!'
    # timer_label.config(text=new_label, fg=GREEN)

    # Add text from story to be copied
    synopses_label = tkinter.Label(text=synopses, bg=YELLOW, fg='black', pady=10, font=(FONT_NAME, 15))
    synopses_label.grid(row=3, column=0)

    # Add text box
    global text_area
    text_area = scrolledtext.ScrolledText(window,
                                          wrap=tkinter.WORD,
                                          width=60,
                                          height=32,
                                          background=YELLOW,
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
        # start_timer()
        print('Time to score.')
        input = text_area.get("1.0", "end-1c")
        print(input)
        score = score_typing(input, synopses)
        print(score)


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Typing Speed Test')
window.config(padx=10, pady=10, bg=YELLOW)  # bg is 'background'


# Add timer label
label = 'Type as much as you can in two minutes. Spelling counts.\n' \
        'There is no penalty for missed punctuation or capitalization.\n' \
        'Press "start" to reveal text and begin.'
timer_label = tkinter.Label(text=label, bg=YELLOW, fg=ORANGE, font=(FONT_NAME, 18))
timer_label.grid(row=0, columnspan=2)

# # Add tomato
# # The tkinter canvas widget lets us overlay objects on top of each other
canvas = tkinter.Canvas(width=1200, height=75, bg=YELLOW, highlightthickness=0)
# tomato_img = tkinter.PhotoImage(file='tomato.png')
# canvas.create_image(100, 112, image=tomato_img)

# Add timer text
timer_text = canvas.create_text(600, 30, text='2:00', fill=ORANGE, font=(FONT_NAME, 36))
canvas.grid(row=1, columnspan=2)


# # Add text
# checkmark = '✅'
# checkmarks = ''
# checks = tkinter.Label(text=checkmarks, bg=YELLOW)
# checks.grid(row=3, column=1)

# Add start button
start_button = tkinter.Button(text='Start', command=start_timer, font=FONT_NAME)
start_button.grid(row=2, columnspan=2)

# Add main while loop to keep window open
window.mainloop()
