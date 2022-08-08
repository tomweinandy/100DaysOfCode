from PIL import Image
import tkinter
from tkinter.filedialog import askopenfile

# Configurations
# Color pallet and hex codes come from colorhunt.co
TAN = '#FCF8E8'
BROWN = '#ECB390'
DARK_GREEN = '#94B49F'
FONT_NAME = "Arial"


def watermark(filepath, black_or_white='white', opacity=0.65, output_filename='default'):
    # Load images
    img = Image.open(filepath)
    logo_black = Image.open('pie.png')

    # Set opacity
    logo = logo_black.convert("RGBA")
    datas = logo.getdata()

    # Change colors and make semi-transparent
    new_data = []
    for item in datas:
        new_opacity = int(item[3] * opacity)

        # If 'white' is selected
        if black_or_white == 'white':
            # If rbg is black (0,0,0) then make it white (255, 255, 255) and opaque
            if item[0:3] == (0, 0, 0):
                new_data.append((255, 255, 255, new_opacity))

            # Otherwise, keep colors but make it transparent
            else:
                new_data.append((item[0], item[1], item[2], 0))

        # Otherwise, assume 'black' is selected
        else:
            # If rbg is black (0,0,0) then keep it black but make opaque
            if item[0:3] == (0, 0, 0):
                new_data.append((0, 0, 0, new_opacity))

            # Otherwise, keep colors but make it transparent
            else:
                new_data.append((item[0], item[1], item[2], 0))

    logo.putdata(new_data)

    # Place watermark in the bottom-right corner
    x_placement = img.size[0] - logo.size[0]
    y_placement = img.size[1] - logo.size[1]
    logo_placement = (x_placement, y_placement)
    img.paste(logo, logo_placement, logo)

    # Show image
    img.show()

    # Select the filename from everything after the last backslash
    filename = filepath.split('/')[-1]

    # Return the partial filepath as everything before the filename
    partial_filepath = filepath[:-len(filename)]

    # Save image
    if output_filename == 'default':
        name_split = filename.split('.')
        output_filename = name_split[0] + '_watermarked.' + name_split[1]
    img.save(partial_filepath + output_filename)


def mark_file(color):
    # Identify the filepath of the selected file
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg'), ('Image Files', '*png')])
    if file_path is not None:
        print(file_path.name)

        # Add watermark
        watermark(file_path.name, black_or_white=color)

    # On completion or cancellation, guide user where new file is saved
    success = 'Check the source folder of the original image.'
    success_label = tkinter.Label(text=success, bg=TAN, fg=DARK_GREEN, font=(FONT_NAME, 16))
    success_label.grid(row=4, columnspan=2, pady=20)
