"""
Day 84: Add Watermarks to Pictures

Reference:
https://pypi.org/project/Pillow/
https://docs.python.org/3/library/tkinter.html
"""
from PIL import Image

# Load images
filename = 'Eli.png'
filename = input('What image in your downloads folder would you like to watermark?: ')
img = Image.open(f'../../../../Downloads/{filename}')
logo_black = Image.open('pie.png')

# Set opacity
opacity = 0.65
logo = logo_black.convert("RGBA")
datas = logo.getdata()

# Change colors and make semi-transparent
newData = []
for item in datas:
    new_opacity = int(item[3]*opacity)

    # If rbg is black (0,0,0) then make it white (255, 255, 255) and opaque
    if item[0:3] == (0, 0, 0):
        newData.append((255, 255, 255, new_opacity))

    # Otherwise, keep colors but make it transparent
    else:
        newData.append((item[0], item[1], item[2], 0))

logo.putdata(newData)

# Place watermark in the bottom-right corner
x_placement = img.size[0] - logo.size[0]
y_placement = img.size[1] - logo.size[1]
logo_placement = (x_placement, y_placement)
img.paste(logo, logo_placement, logo)
img.show()
img.save('watermark.png')

