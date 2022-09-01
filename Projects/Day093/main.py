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

# NOTE: Had to change system preferences to allow my IDE to control the keyboard
# Jump every second
while True:
    keyboard.send('space')
    time.sleep(1)





# pyautogui.click()          # Click the mouse.
# pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
#
# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.doubleClick()     # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
#
# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
#
# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#     pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# # Shift key is released automatically.
#
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
#
# pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

# todo take screenshot of browser
# todo locate pixels within image
# todo fine tune jump timing

time.sleep(5)
