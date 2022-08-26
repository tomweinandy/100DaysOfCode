"""
Day 89: Disappearing Writing App
"""
import tkinter
from tkinter import scrolledtext
import datetime

# todo clear mentions of reps, checks
# todo move helper functions to separate document
# todo clean up code, comment

# ---------------------------- VARIABLES ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
FONT_NAME = 'Arial'
NAVY = '#1C3879'
BLUE = '#607EAA'
SAND = '#EAE3D2'
FILEPATH = '../../../../Downloads/'
MINUTES_BEFORE_BOMB = 5

grace_time = MINUTES_BEFORE_BOMB * 0.2 * 60
warning_time = MINUTES_BEFORE_BOMB * 0.8 * 60
previous_wordcount = 0
seconds_without_writing = 0
# reps = 0
# session_minutes = 60
# timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked():
    """
    Resets global variables and features of timer
    """
    global seconds_without_writing
    seconds_without_writing = 0

    print('Reset clicked')
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00:00')
    stop_bomb_timer()


def stop_bomb_timer():
    global bomb_timer_label

    window.after_cancel(bomb_timer)
    bomb_timer_label.destroy()
    motivate()


# ---------------------------- CHECK PROGRESS ------------------------------- #
def check_progress():
    global previous_wordcount, seconds_without_writing
    # print(seconds_without_writing)

    current = notepad.get('1.0', tkinter.END)
    current_wordcount = len(current)
    progress = current_wordcount - previous_wordcount

    previous_wordcount = current_wordcount

    if progress == 0:
        seconds_without_writing += 1
    else:
        seconds_without_writing = 0

        try:
            stop_bomb_timer()
            print('stop bomb timer')
        except:
            pass
            print('pass')

    if seconds_without_writing == grace_time:
        start_bomb_timer()


# ---------------------------- SESSION TIMER MECHANISM ------------------------------- #
def start_clicked():
    """
    Tracks reps and begins timer according to current rep
    """
    print('Start clicked')
    if bomb_timer_label in globals():
        stop_bomb_timer()

    session_length_in_minutes = session_length_entry.get()
    # Multiply minutes by 60, cut off to the nearest second
    session_length_in_seconds = ((float(session_length_in_minutes) * 60) // 1)

    session_length_entry.delete(0, 999)
    countdown(session_length_in_seconds)


# ---------------------------- BOMB TIMER MECHANISM ------------------------------- #
def start_bomb_timer():
    print('Bombs away!')
    global bomb_timer_label
    bomb_timer_label = tkinter.Label(text='', bg=SAND, fg=BLUE, font=(FONT_NAME, 16)) #todo do i need this?
    bomb_timer_label.grid(row=4, columnspan=3)
    bomb_countdown(warning_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def strint(n):
    return str(int(n))


def motivate():
    global bomb_timer_label, bomb_timer_text
    seconds_without_writing = 0

    if 'bomb_canvas' in globals():
        bomb_canvas.delete(bomb_timer_text)

    bomb_timer_label = tkinter.Label(text='', bg=SAND, fg=BLUE, font=(FONT_NAME, 16))
    bomb_timer_label.grid(row=4, columnspan=3)


def bomb_countdown(count):
    """
    Changes the countdown timer
    :param count: How many seconds to count down from
    """
    global bomb_timer, bomb_timer_label, bomb_canvas, bomb_timer_text

    bomb_minutes = strint((count // 60) % 60)   # Cut off to the nearest minute, remove whole hours
    bomb_seconds = strint(count % 60)           # Remove whole minutes

    # Give single-digit time units a leading 0
    if len(bomb_minutes) == 1:
        bomb_minutes = '0' + bomb_minutes
    if len(bomb_seconds) == 1:
        bomb_seconds = '0' + bomb_seconds

    # Clear timer
    bomb_timer_label.destroy()

    # Add bomb timer label
    bomb_timer_label_text = '⏳ Time before all work is deleted:'
    bomb_timer_label = tkinter.Label(text=bomb_timer_label_text, bg=SAND, fg=NAVY, font=(FONT_NAME, 24, 'bold'))
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
        print('Bomb detonated')
        notepad = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=100, height=25, font=(FONT_NAME, 14))
        notepad.grid(row=5, columnspan=5, pady=10, padx=10)


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
    else:
        save_results()


def save_results():
    global bomb_timer_label

    current_writing = notepad.get('1.0', tkinter.END)

    if len(current_writing) > 0:
        print('Saving results...')
        timestamp = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M')
        try:
            text_file = open(f'{FILEPATH}writers_clock_{timestamp}.txt', 'w')
            text_file.write(current_writing)
        except:
            text_file = open(f'writers_clock_{timestamp}.txt', 'w')
            text_file.write(current_writing)
        text_file.close()

        bomb_timer_label = tkinter.Label(text='Work saved in Downloads folder', bg=SAND, fg=BLUE, font=(FONT_NAME, 24, 'bold'))
        bomb_timer_label.grid(row=4, columnspan=3)

# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Disappearing Notepad')
window.config(padx=100, pady=50, bg=SAND)  # bg is 'background'

# Add header
label = '   Writer\'s Clock   '  # spaces added to match length of other labels
timer_label = tkinter.Label(text=label, bg=SAND, fg=BLUE, font=(FONT_NAME, 36))
timer_label.grid(row=0, columnspan=5)

# Add instructions
instructions_text = 'INSTRUCTIONS: Set the timer for your session and begin writing below. All work will be saved to ' \
                    'your downloads folder \nat the end of the session. But beware! If you stop writing for ' \
                    f'{MINUTES_BEFORE_BOMB} minutes, ALL WORK WILL BE DELETED forever.'
timer_label = tkinter.Label(text=instructions_text, bg=SAND, fg=BLUE, font=(FONT_NAME, 16, 'italic'))
timer_label.grid(row=1, columnspan=5)

# Add input label
set_time_text = 'Select the number of minutes for this session:'
set_time_label = tkinter.Label(text=set_time_text, bg=SAND, fg=BLUE, font=(FONT_NAME, 16))
set_time_label.grid(row=2, columnspan=2)

# Adds entry
session_length_entry = tkinter.Entry(width=5, bg='white', font=FONT_NAME)
session_length_entry.insert(tkinter.END, string='0')
session_length_entry.grid(row=2, column=2, pady=20)

# Add start button
start_button = tkinter.Button(text='Start', command=start_clicked, font=FONT_NAME)
start_button.grid(row=2, column=3)

# Add reset button
reset_button = tkinter.Button(text='Reset', command=reset_clicked, font=FONT_NAME)
reset_button.grid(row=2, column=4)

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

#
notepad = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=100, height=25, font=(FONT_NAME, 14))
notepad.grid(row=5, columnspan=5, pady=10, padx=10)

# Add main while loop to keep window open
window.mainloop()
