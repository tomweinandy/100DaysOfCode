"""
Day 93: T-Rex Run Game Player

The original: https://elgoog.im/t-rex/

Your goal today is to write a Python script to automate the playing of this game. Your program will look at the pixels on the screen to determine when it needs to hit the space bar and play the game automatically.

You might want to look up these two packages:
https://pypi.org/project/Pillow/
https://pyautogui.readthedocs.io/en/latest/
"""
import pyautogui
import webbrowser
import time
import keyboard
import colorgram

SCORE_BOX = 'score_box.png'
SCAN_BOX = 'scan_box.png'


def locate():
    current_mouse_x, current_mouse_y = pyautogui.position()
    print('Current mouse location:', current_mouse_x, current_mouse_y)


# Get the size of the primary monitor
screenWidth, screenHeight = pyautogui.size()
print('Screen size:', screenWidth, screenHeight)  # (1440, 900) for me


url = 'https://elgoog.im/t-rex/'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open_new(url)


# Allow page to render
time.sleep(5)

# todo get this to work or delete
# Move the mouse to XY coordinates
pyautogui.moveTo(100, 150)
locate()

# NOTE: Had to change system preferences to allow my IDE to control the keyboard and take screenshots # todo move note

# Find the position of the game title (used to locate other objects)
title_location = pyautogui.locateOnScreen('title.png')
left, top, width, height = title_location

# Define scan and score boxes (subtract from left to move left, add to top to move down)
scan_box = (left+100, top+500, width-625, height-50)
score_box = (left+475, top+280, width-150, height+50)

last_black_ink = 0
jumps = 0

# Start game
keyboard.send('space')
for i in range(20):
    # time.sleep(0.1) # todo try removing time

    # Take screenshot of area in front of dino
    pyautogui.screenshot(SCAN_BOX, region=scan_box)

    # Find share pixels within scan box that are black (indicates cactus)
    # Extract colors from scan box
    colors = colorgram.extract(SCAN_BOX, 2)
    # Take last (ie, second) color which will always be black
    black_ink = colors[-1].proportion
    print(black_ink)

    # Make dino jump if share of black pixels has changed (indicates screen movement) and meets a threshold
    # if black_ink != last_black_ink and black_ink > 0.03:
    if black_ink > 0.03:
        keyboard.send('space')
        # jumps += 1
        # Take screenshot of score
        # pyautogui.screenshot(f'jump{jumps}.png', region=scan_box)

        print('JUMP')

    last_black_ink = black_ink

pyautogui.screenshot(SCORE_BOX, region=score_box)

# todo Record score

# todo Fine tune jump timing

time.sleep(5)
