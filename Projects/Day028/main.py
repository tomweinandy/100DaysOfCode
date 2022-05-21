"""
Day 28: Pomodoro Time Tracker
"""
import tkinter

# ---------------------------- VARIABLES ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SECONDS = 25 * 60
SHORT_BREAK_SECONDS = 5 * 60
LONG_BREAK_SECONDS = 20 * 60

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


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Tracks reps and begins timer according to current rep
    """
    global reps, checkmarks
    reps += 1

    # If reps = 8, 16...
    if reps % 8 == 0:
        countdown(LONG_BREAK_SECONDS)
        new_label = 'Break Time'
        timer_label.config(text=new_label, fg=RED)

        checkmarks += checkmark + '\n'
        checks.config(text=checkmarks)

    # If reps = 2, 4, 6, 10, 12, 14...
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_SECONDS)
        new_label = 'Break Time'
        timer_label.config(text=new_label, fg=PINK)

        checkmarks += checkmark
        checks.config(text=checkmarks)

    # If reps = 1, 3, 5, 7, 9, 11, 13, 15, 17...
    else:
        countdown(WORK_SECONDS)
        new_label = ' Work Time'
        timer_label.config(text=new_label, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """
    Changes the countdown timer
    :param count: How many seconds to count down from
    :return:
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
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)  # bg is 'background'


# Add timer label
label = '  Timer   '  # spaces added to match length of other labels
timer_label = tkinter.Label(text=label, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36))
timer_label.grid(row=0, column=1)

# Add tomato
# The tkinter canvas widget lets us overlay objects on top of each other
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)

# Add timer text over tomato
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

# Add checkmarks
checkmark = '✅'
checkmarks = ''
checks = tkinter.Label(text=checkmarks, bg=YELLOW)
checks.grid(row=3, column=1)

# Add start button
start_button = tkinter.Button(text='Start', command=start_timer, font=FONT_NAME)
start_button.grid(row=2, column=0)

# Add reset button
start_button = tkinter.Button(text='Reset', command=reset_clicked, font=FONT_NAME)
start_button.grid(row=2, column=2)

# Add main while loop to keep window open
window.mainloop()
