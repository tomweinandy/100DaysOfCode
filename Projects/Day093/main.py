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


def locate():
    currentMouseX, currentMouseY = pyautogui.position()
    print('Current mouse location:', currentMouseX, currentMouseY)


# Get the size of the primary monitor
screenWidth, screenHeight = pyautogui.size()
print('Screen size:', screenWidth, screenHeight)  # (1440, 900) for me


url = 'https://elgoog.im/t-rex/'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open_new(url)


# Allow page to render
time.sleep(10)

# todo get this to work or delete
# Move the mouse to XY coordinates
pyautogui.moveTo(100, 150)
locate()

# Find the position of the game title (used to locate other objects)
title_location = pyautogui.locateOnScreen('title.png')
print(title_location)

# NOTE: Had to change system preferences to allow my IDE to control the keyboard
# Jump every second
for i in range(5):
    keyboard.send('space')
    time.sleep(1)

# Take screenshot of browser
pyautogui.screenshot('screenshot.png')

# todo locate pixels within image


# todo fine tune jump timing

time.sleep(5)