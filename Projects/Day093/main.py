"""
Day 93: T-Rex Run Game Player

The original: https://elgoog.im/t-rex/
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


def jump():
    keyboard.press('space')
    time.sleep(0.01)
    keyboard.release('space')
    print('JUMP!')


# Get the size of the primary monitor
screenWidth, screenHeight = pyautogui.size()
print('Screen size:', screenWidth, screenHeight)  # (1440, 900) for me

# Open webpage
url = 'https://elgoog.im/t-rex/'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open_new(url)

# Allow page to render
time.sleep(5)

# NOTE: Had to change system preferences to allow my IDE to control the keyboard and take screenshots # todo move note

# Find the position of the game title (used to locate other objects)
title_location = pyautogui.locateOnScreen('title.png', grayscale=True, confidence=0.8)
left, top, width, height = title_location

# print(width, height)

# Define scan and score boxes (subtract from left to move left, add to top to move down)
# scan_box = (left+100, top+500, width-600, height-0)
scan_box = (left+150, top+560, 200, 1)
w, h = 500, 1000
# scan_box = (0, 0, w, h)
# score_box = (left+475, top+280, width-150, height+50)

last_black_ink = 0
no_jumps = 0

# Start game
keyboard.send('space')
for i in range(10000):
    if no_jumps == 15:
        jump()
        no_jumps = 0

    # Take screenshot of area in front of dino
    # scan = pyautogui.screenshot(f'this_{i}.png', region=scan_box)
    scan = pyautogui.screenshot(region=scan_box)

    # Find share pixels within scan box that are black (indicates cactus)
    # Extract colors from scan box
    colors = colorgram.extract(scan, 2)
    # Take last (ie, second) color which will always be black
    # black_ink = colors[-1].proportion
    # print(black_ink)

    # Make dino jump if share of black pixels has changed (indicates screen movement) and meets a threshold
    # if black_ink != last_black_ink and black_ink > 0.03:
    # if black_ink > 0.06:
    if len(colors) == 2:
        jump()
        no_jumps = 0
        # jumps += 1
        # Take screenshot of score
        # pyautogui.screenshot(f'jump{jumps}.png', region=scan_box)
    else:
        no_jumps += 1
    # last_black_ink = black_ink

pyautogui.screenshot(SCAN_BOX, region=scan_box)
# pyautogui.screenshot(SCORE_BOX, region=score_box)


# time.sleep(5)
