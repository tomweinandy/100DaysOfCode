import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
# Color pallet and hex codes come from colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_clicked():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_clicked():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)  # bg is 'background'

# Add timer label
timer = tkinter.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36))
timer.grid(row=0, column=1)

# Add tomato
# The tkinter canvas widget lets us overlay objects on top of each other
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Add start button
start_button = tkinter.Button(text='Start', command=start_clicked, font=FONT_NAME)
start_button.grid(row=2, column=0)

# Add reset button
start_button = tkinter.Button(text='Reset', command=reset_clicked, font=FONT_NAME)
start_button.grid(row=2, column=2)

# Add checkmarks
checkmark = '✅'
checks_string = ''
checks = tkinter.Label(text=checks_string, bg=YELLOW)
checks.grid(row=3, column=1)

# Add main while loop to keep window open
window.mainloop()
