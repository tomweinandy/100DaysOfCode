"""
Day 93: T. Rex Run Game Player

NOTE: Had to change system preferences to allow my IDE to control the keyboard and take screenshots
"""
import pyautogui
import webbrowser
import time
import keyboard
import colorgram


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

# Find the position of the game title (used to locate other objects)
title_location = pyautogui.locateOnScreen('title.png', grayscale=True, confidence=0.8)
left, top, width, height = title_location

"""
Define scan box relative to the tile. The relative position allows the scan box to be consistent across different
sized screens. This is only theoretical, as it was only tested on one screen. The scan box parameters are (in order)
x_position, y_position, width, height. Subtract from left to move left; add to top to move down.

This solution, though satisfactory, is inferior to just directly reading the pixel color from the screen. Unfortunately,
I did not manage to disable the security blocks on my computer that preventing screen reading. The current approach 
relies on screenshots which apparently are fine.
"""
scan_box = (left+150, top+560, 200, 1)
score_box = (left+475, top+280, width-150, height+50)

# Start game
no_jumps = 0
keyboard.send('space')

# Continue for number of intervals stated in range
for i in range(10000):
    # Take screenshot of area in front of dino
    scan = pyautogui.screenshot(region=scan_box)

    # Extract up to two colors from scan box
    colors = colorgram.extract(scan, 2)

    # Make dino jump if there are two colors (second color indicates there is a cactus within the scan box)
    if len(colors) == 2:
        jump()
        no_jumps = 0
    else:
        no_jumps += 1

    # Jump if the dino has been inactive for 15 intervals
    if no_jumps == 15:
        jump()
        no_jumps = 0

# Optional: Save a picture of the scan box
# pyautogui.screenshot('scan_box.png', region=scan_box)

# Optional: Save a screenshot of the score
# pyautogui.screenshot('score_box.png', region=score_box)
