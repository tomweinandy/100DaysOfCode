import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 9
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 6

reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_clicked():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# def change_label(new_label):
#     timer_label.config(text=new_label)

def start_timer():
    global reps
    global checkmarks
    reps += 1

    # If reps = 1, 3, 5, 7, 9, 11, 13, 15, 17...
    work_seconds = WORK_MIN

    # If reps = 2, 4, 6, 10, 12, 14...
    short_break_seconds = SHORT_BREAK_MIN

    # If reps = 8, 16...
    long_break_seconds = LONG_BREAK_MIN

    if reps % 8 == 0:
        countdown(long_break_seconds)
        new_label = 'Break Time'
        timer_label.config(text=new_label, fg=RED)

        checkmarks += checkmark + '  '
        checks.config(text=checkmarks)

    elif reps % 2 == 0:
        countdown(short_break_seconds)
        new_label = 'Break Time'
        timer_label.config(text=new_label, fg=PINK)

        checkmarks += checkmark
        checks.config(text=checkmarks)

    else:
        countdown(work_seconds)
        new_label = ' Work Time'
        timer_label.config(text=new_label, fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minutes_left = str(count // 60)
    seconds_left = str(count % 60)
    if len(seconds_left) == 1:
        seconds_left = '0' + seconds_left

    new_time = f'{minutes_left}:{seconds_left}'
    canvas.itemconfig(timer_text, text=new_time)
    if count > 0:
        window.after(1000, countdown, count-1)  # time is in milliseconds
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)  # bg is 'background'


# Add timer label
label = '  Timer   '  #spaces added to match length of other labels
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
