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



opacity_level = 170 # Opaque is 255, input between 0-255
opacity = 0.67 # Opaque is 255, input between 0-255

logo = logo_white.convert("RGBA")
datas = logo.getdata()

newData = []
for item in datas:
    new_opacity = int(item[3]*opacity)
    newData.append((item[0], item[1], item[2], new_opacity))

logo.putdata(newData)



x_placement = img.size[0] - logo.size[0]
y_placement = img.size[1] - logo.size[1]
logo_placement = (x_placement, y_placement)
img.paste(logo, logo_placement, logo)
img.show()
# img.save('watermark.png')

