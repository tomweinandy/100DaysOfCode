"""
Day 89: Disappearing Writing App
"""
import time
import tkinter

# ---------------------------- VARIABLES ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
FONT_NAME = 'Arial'
NAVY = '#1C3879'
BLUE = '#607EAA'
BEIGE = '#EAE3D2'
SAND = '#F9F5EB'

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_SECONDS = 25 * 60
SHORT_BREAK_SECONDS = 5 * 60
LONG_BREAK_SECONDS = 20 * 60

reps = 0
session_minutes = 60
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
    timer_label.config(text='Timer', fg=BLUE)
    canvas.itemconfig(timer_text, text='00:00')
    checks.config(text=checkmarks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Tracks reps and begins timer according to current rep
    """
    global reps, checkmarks
    reps += 1

    session_length_in_minutes = session_length_entry.get()     # In minutes
    print(session_length_in_minutes)
    session_length_in_seconds = ((float(session_length_in_minutes) * 60) // 1)     # Multiply minutes by 60, cut off to the nearest second

    session_length_entry.delete(0, 999)
    countdown(session_length_in_seconds)

# todo detect if there is writing

# todo set second timer if writing stops

# todo add warning and timer if writing stops

# todo add pre-start instructions

# todo add post-start instructions

# todo save results to downloads after end of session


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def strint(n):
    return str(int(n))


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
    # else:
    #     start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window #todo update
window = tkinter.Tk()
# window.geometry("1000x500")
window.title('Disappearing Notepad')
window.config(padx=100, pady=50, bg=SAND)  # bg is 'background'

# Add timer label
label = '   Writers UN-block   '  # spaces added to match length of other labels
timer_label = tkinter.Label(text=label, bg=SAND, fg=BLUE, font=(FONT_NAME, 36))
timer_label.grid(row=0, columnspan=5)

# # Add checkmarks
# checkmark = '✅'
# checkmarks = ''
# checks = tkinter.Label(text=checkmarks, bg=SAND)
# checks.grid(row=3, column=1)

# Add input label
set_time_text = 'Select the number of minutes for this session:'
set_time_label = tkinter.Label(text=set_time_text, bg=SAND, fg=BLUE, font=(FONT_NAME, 16))
set_time_label.grid(row=1, columnspan=3)

# Adds entry
session_length_entry = tkinter.Entry(width=5, bg=BEIGE, font=FONT_NAME)
session_length_entry.insert(tkinter.END, string='0')
session_length_entry.grid(row=1, column=3, pady=20)

# Add start button
start_button = tkinter.Button(text='Start', command=start_timer, font=FONT_NAME)
start_button.grid(row=1, column=4)

# # Add reset button
# start_button = tkinter.Button(text='Reset', command=reset_clicked, font=FONT_NAME)
# start_button.grid(row=2, column=2)

# Add timer label
timer_text = 'Time remaining for this session:'
timer_label = tkinter.Label(text=timer_text, bg=SAND, fg=BLUE, font=(FONT_NAME, 16))
timer_label.grid(row=2, columnspan=3)

# The tkinter canvas widget lets us overlay objects on top of each other
canvas = tkinter.Canvas(width=200, height=50, bg=SAND, highlightthickness=0)
canvas.grid(row=2, column=3)
timer_text = canvas.create_text(100, 25, text='00:00:00', fill=BLUE, font=(FONT_NAME, 16, 'bold'))


# The tkinter canvas widget lets us overlay objects on top of each other
canvas2 = tkinter.Canvas(width=200, height=50, bg=SAND, highlightthickness=0)
canvas2.grid(row=3, column=3)

bomb_timer_text = canvas2.create_text(100, 25, text='00:00:00', fill=NAVY, font=(FONT_NAME, 24, 'bold'))
bomb_timer_text = 'Time before all work is deleted:'
bomb_timer_label = tkinter.Label(text=bomb_timer_text, bg=SAND, fg=NAVY, font=(FONT_NAME, 24, 'bold'))
bomb_timer_label.grid(row=3, columnspan=3)



#todo add text box
notepad = tkinter.Entry(window, width=50)
notepad.grid(row=4, columnspan=5)

# Add main while loop to keep window open
window.mainloop()
