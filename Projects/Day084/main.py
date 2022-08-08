"""
Day 84: Desktop App that Adds Image Watermarks

Reference:
https://pypi.org/project/Pillow/
https://docs.python.org/3/library/tkinter.html
"""
import tkinter
import helper_functions

# Configurations
# Color pallet and hex codes come from colorhunt.co
TAN = '#FCF8E8'
BROWN = '#ECB390'
DARK_GREEN = '#94B49F'
FONT_NAME = "Arial"

# Create window
window = tkinter.Tk()
window.title('Make Your Watermark on the World')
window.config(padx=100, pady=50, bg=TAN)

# Add label
label = 'Add a Pie Logo to an Image'
timer_label = tkinter.Label(text=label, bg=TAN, fg=BROWN, font=(FONT_NAME, 36))
timer_label.grid(row=0, columnspan=2)

# Show pie logo
canvas = tkinter.Canvas(width=376, height=376, bg=TAN, highlightthickness=0)
pie_img = tkinter.PhotoImage(file='pie.png')
canvas.create_image(200, 200, image=pie_img)
canvas.grid(row=1, columnspan=2, column=0)

# Add Instructions
instructions = 'Upload image to be watermarked (must be jpg, jpeg, or png)'
instructions_label = tkinter.Label(text=instructions, bg=TAN, fg=DARK_GREEN, font=(FONT_NAME, 16))
instructions_label.grid(row=2, columnspan=2, pady=20)

# Build buttons to select file
image_button = tkinter.Button(window, text='Add White Watermark', command=lambda: helper_functions.mark_file('white'))
image_button.grid(row=3, column=0)

image_button = tkinter.Button(window, text='Add Black Watermark', command=lambda: helper_functions.mark_file('black'))
image_button.grid(row=3, column=1)

# Keep window open
window.mainloop()
