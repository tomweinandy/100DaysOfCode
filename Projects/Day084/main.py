"""
Day 84: Add Watermarks to Pictures

Reference:
https://pypi.org/project/Pillow/
https://docs.python.org/3/library/tkinter.html
"""

from PIL import Image
import numpy as np


img = Image.open('../../../../Downloads/Eli.png')
logo_black = Image.open('pie.png')

# Convert logo to white
logo_black = logo_black.convert('RGBA')
data = np.array(logo_black)                             # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T                        # Temporarily unpack the bands for readability
black_areas = (red == 0) & (blue == 0) & (green == 0)   # Replace black with white... (leaves alpha values alone...)
data[..., :-1][black_areas.T] = (255, 255, 255)         # Transpose back needed
logo_white = Image.fromarray(data)
# logo_white.show()

# print(img.size, logo.size)
#
img.paste(logo_white, (0, 0), logo_white)
img.show()
# img.save('watermark.png')

