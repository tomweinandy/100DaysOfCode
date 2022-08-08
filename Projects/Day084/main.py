"""
Day 84: Desktop App that Adds Image Watermarks

Reference:
https://pypi.org/project/Pillow/
https://docs.python.org/3/library/tkinter.html
"""
from watermark import watermark
import tkinter
# import find_image

# Configurations
# Color pallet and hex codes come from colorhunt.co
TAN = '#FCF8E8'
BROWN = '#ECB390'
DARK_GREEN = '#94B49F'

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_SECONDS = 25 * 60
SHORT_BREAK_SECONDS = 5 * 60
LONG_BREAK_SECONDS = 20 * 60

def start_timer():
    print('start timer')

def reset_clicked():
    print('reset clicked')

# Create window
window = tkinter.Tk()
window.title('Make Your Watermark on the World')
window.config(padx=100, pady=50, bg=TAN)

# Add label
label = 'Add Pie Logo'
timer_label = tkinter.Label(text=label, bg=TAN, fg=BROWN, font=(FONT_NAME, 36))
timer_label.grid(row=0, column=1)

# Show pie logo
canvas = tkinter.Canvas(width=376, height=376, bg=TAN, highlightthickness=0)
pie_img = tkinter.PhotoImage(file='pie.png')
canvas.create_image(200, 200, image=pie_img)
canvas.grid(row=1, column=1)

# # Add timer text over tomato
# timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

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

# # Add reset button
# start_button = tkinter.Run(text='Reset', command=watermark, font=FONT_NAME)
# start_button.grid(row=3, column=1)


from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg'), ('Image Files', '*png')])
    if file_path is not None:
        print(file_path.name)
        watermark(file_path.name)

    success = 'Image uploaded successfully! Check the source folder of the original image.'
    success_label = tkinter.Label(text=success, bg=TAN, fg=BROWN, font=(FONT_NAME, 16))
    success_label.grid(row=5, column=1, pady=20)


def upload_file():
    pb1 = Progressbar(
        window,
        orient=HORIZONTAL,
        length=300,
        mode='determinate',
    )
    pb1.grid(row=5, columnspan=3, pady=20)
    for i in range(5):
        window.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(window,
          text='Image uploaded successfully! Check your downloads folder.',
          foreground=DARK_GREEN,
          background=TAN)\
        .grid(row=6, columnspan=3, pady=10)


# Add Instructions
instructions = 'Upload image to be watermarked (must be jpg, jpeg, or png)'
instructions_label = tkinter.Label(text=instructions, bg=TAN, fg=DARK_GREEN, font=(FONT_NAME, 16))
instructions_label.grid(row=3, column=1, pady=20)

image_button = Button(window, text='Upload Image', command=lambda: open_file())
image_button.grid(row=4, column=1)

# upload_button = Button(window, text='Upload Files', command=lambda: upload_file())
# upload_button.grid(row=4, column=1, pady=10)

# ws.mainloop()








# Keep window open
window.mainloop()
