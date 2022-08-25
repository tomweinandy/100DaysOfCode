"""
Day 89: Disappearing Writing App
"""
import time
import tkinter
from tkinter import scrolledtext

# todo detect if there is writing
# todo set second timer if writing stops
# todo add warning and timer if writing stops
# todo add post-start instructions
# todo save results to downloads after end of session
# todo clear mentions of reps, checks

# ---------------------------- VARIABLES ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
FONT_NAME = 'Arial'
NAVY = '#1C3879'
BLUE = '#607EAA'
BEIGE = '#F9F5EB'
# BEIGE = '#EAE3D2'
SAND = '#EAE3D2'
# SAND = '#F9F5EB'

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GRACE_TIME = 0.1 * 60
WARNING_TIME = 0.1 * 60

previous_wordcount = 0
seconds_without_writing = 0
reps = 0
session_minutes = 60
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked():
    """
    Resets global variables and features of timer
    """
    # global reps, checkmarks
    # reps = 0
    # checkmarks = ''
    window.after_cancel(timer)
    # timer_label.config(text='Timer', fg=BLUE)
    canvas.itemconfig(timer_text, text='00:00:00')
    # checks.config(text=checkmarks)


def stop_bomb_timer():
    window.after_cancel(bomb_timer)
    bomb_timer_label.destroy()
    motivate()
    # bomb_canvas.itemconfig(bomb_timer_text, text='00:00:00')



# ---------------------------- CHECK PROGRESS ------------------------------- #
def check_progress():
    global previous_wordcount, seconds_without_writing

    current = notepad.get('1.0', tkinter.END)
    current_wordcount = len(current)
    progress = current_wordcount - previous_wordcount
    # print(current, current_wordcount, progress, seconds_without_writing)
    print(seconds_without_writing)

    previous_wordcount = current_wordcount

    if progress == 0:
        seconds_without_writing += 1
    else:
        seconds_without_writing = 0

        try:
            stop_bomb_timer()
        except:
            pass

    if seconds_without_writing == GRACE_TIME:
        start_bomb_timer()


# ---------------------------- SESSION TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Tracks reps and begins timer according to current rep
    """
    # global reps, checkmarks
    # reps += 1

    session_length_in_minutes = session_length_entry.get()     # In minutes
    print(session_length_in_minutes)
    session_length_in_seconds = ((float(session_length_in_minutes) * 60) // 1)     # Multiply minutes by 60, cut off to the nearest second

    session_length_entry.delete(0, 999)
    countdown(session_length_in_seconds)


# ---------------------------- BOMB TIMER MECHANISM ------------------------------- #
def start_bomb_timer():
    print('bombs away!')
    bomb_countdown(WARNING_TIME)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def strint(n):
    return str(int(n))


def motivate():
    # Placeholder space where lethal countdown starts
    bomb_timer_label = tkinter.Label(text='Keep up the good work!', bg=SAND, fg=NAVY, font=(FONT_NAME, 24))
    bomb_timer_label.grid(row=4, columnspan=3)


def bomb_countdown(count):
    """
    Changes the countdown timer
    :param count: How many seconds to count down from
    """
    global bomb_timer, bomb_timer_label

    bomb_minutes = strint((count // 60) % 60)   # Cut off to the nearest minute, remove whole hours
    bomb_seconds = strint(count % 60)           # Remove whole minutes

    # Give single-digit time units a leading 0
    if len(bomb_minutes) == 1:
        bomb_minutes = '0' + bomb_minutes
    if len(bomb_seconds) == 1:
        bomb_seconds = '0' + bomb_seconds

    # Add bomb timer label
    bomb_timer_label_text = 'Time before all work is deleted:'
    bomb_timer_label = tkinter.Label(text=bomb_timer_label_text, bg=SAND, fg=NAVY, font=(FONT_NAME, 24))
    bomb_timer_label.grid(row=4, columnspan=3)

    # The tkinter canvas widget lets us overlay objects on top of each other
    bomb_canvas = tkinter.Canvas(width=200, height=50, bg=SAND, highlightthickness=0)
    bomb_canvas.grid(row=4, column=3)
    bomb_timer_text = bomb_canvas.create_text(100, 25, text='X:XX', fill=NAVY, font=(FONT_NAME, 24, 'bold'))

    bomb_new_time = f'{bomb_minutes}:{bomb_seconds}'
    bomb_canvas.itemconfig(bomb_timer_text, text=bomb_new_time)
    if count > 0:
        bomb_timer = window.after(1000, bomb_countdown, count-1)  # time is in milliseconds, so 1000ms = 1 second
    else:
        bomb_timer = 'NA'
        print('Bomb detonated')

def countdown(count):
    """
    Changes the countdown timer
    :param count: How many seconds to count down from
    """
    global timer

    hours = strint(count // (60 * 60))     # Cut off to the nearest hour
    minutes = strint((count // 60) % 60)   # Cut off to the nearest minute, remove whole hours
    seconds = strint(count % 60)           # Remove whole minutes

    # Give single-digit time units a leading 0
    if len(hours) == 1:
        hours = '0' + hours
    if len(minutes) == 1:
        minutes = '0' + minutes
    if len(seconds) == 1:
        seconds = '0' + seconds

    new_time = f'{hours}:{minutes}:{seconds}'
    canvas.itemconfig(timer_text, text=new_time)
    if count > 0:
        timer = window.after(1000, countdown, count-1)  # time is in milliseconds, so 1000ms = 1 second
        check_progress()


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Disappearing Notepad')
window.config(padx=100, pady=50, bg=SAND)  # bg is 'background'

# Add header
label = '   Writers UN-block   '  # spaces added to match length of other labels
timer_label = tkinter.Label(text=label, bg=SAND, fg=BLUE, font=(FONT_NAME, 36))
timer_label.grid(row=0, columnspan=5)

# Add instructions
instructions_text = 'INSTRUCTIONS: Set the timer for your session and begin writing below. All work will be saved to ' \
                    'your downloads folder \nat the end of the session. But beware! If you stop writing for 5 ' \
                    'minutes, ALL WORK WILL BE DELETED forever.'
timer_label = tkinter.Label(text=instructions_text, bg=SAND, fg=NAVY, font=(FONT_NAME, 16, 'italic'))
timer_label.grid(row=1, columnspan=5)

# Add input label
set_time_text = 'Select the number of minutes for this session:'
set_time_label = tkinter.Label(text=set_time_text, bg=SAND, fg=BLUE, font=(FONT_NAME, 16))
set_time_label.grid(row=2, columnspan=2)

# Adds entry
session_length_entry = tkinter.Entry(width=5, bg=BEIGE, font=FONT_NAME)
session_length_entry.insert(tkinter.END, string='0')
session_length_entry.grid(row=2, column=2, pady=20)

# Add start button
start_button = tkinter.Button(text='Start', command=start_timer, font=FONT_NAME)
start_button.grid(row=2, column=3)

# Add reset button
start_button = tkinter.Button(text='Reset', command=reset_clicked, font=FONT_NAME)
start_button.grid(row=2, column=4)

# Add timer label
timer_label_text = 'Time remaining for this session:'
timer_label = tkinter.Label(text=timer_label_text, bg=SAND, fg=BLUE, font=(FONT_NAME, 16))
timer_label.grid(row=3, columnspan=3)

# The tkinter canvas widget lets us overlay objects on top of each other
canvas = tkinter.Canvas(width=200, height=50, bg=SAND, highlightthickness=0)
canvas.grid(row=3, column=3)
timer_text = canvas.create_text(100, 25, text='00:00:00', fill=BLUE, font=(FONT_NAME, 16, 'bold'))

# Placeholder space where lethal countdown starts
motivate()


# -----
# # Add bomb timer label
# bomb_timer_label_text = 'Time before all work is deleted:'
# bomb_timer_label = tkinter.Label(text=bomb_timer_label_text, bg=SAND, fg=NAVY, font=(FONT_NAME, 24, 'bold'))
# bomb_timer_label.grid(row=4, columnspan=3)
#
# # The tkinter canvas widget lets us overlay objects on top of each other
# bomb_canvas = tkinter.Canvas(width=200, height=50, bg=SAND, highlightthickness=0)
# bomb_canvas.grid(row=4, column=3)
# bomb_timer_text = bomb_canvas.create_text(100, 25, text='X:XX', fill=NAVY, font=(FONT_NAME, 24, 'bold'))

notepad = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=100, height=25, font=(FONT_NAME, 14))
notepad.grid(row=5, columnspan=5, pady=10, padx=10)

# Add main while loop to keep window open
window.mainloop()
