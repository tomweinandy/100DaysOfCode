"""
Day 91: Website to

One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.
https://flatuicolors.com/palette/defo
It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and use it in my CSS or any design software.
On day 76, you learnt about image processing with NumPy. Using this knowledge and your developer skills (that means Googling), build a website where a user can upload an image and you will tell them what are the top 10 most common colours in that image.
This is a good example of this functionality:
http://www.coolphptools.com/color_extract#demo
"""
import colorgram

# todo build stand-along website (look at day 87, sample.html)
# todo add photo upload

# Convert rbg colors to hex
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


# Extract colors from the jpg
colorgram_list = []
colors = colorgram.extract('kill_bill.jpeg', 10)

# Convert colors to a list of RGB values
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    colorgram_list.append(tup)

hex_list = [rgb_to_hex(c) for c in colorgram_list]

print(hex_list)

