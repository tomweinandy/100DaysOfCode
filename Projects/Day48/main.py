"""
Day 48: Automated Game Player

Requires download from https://chromedriver.chromium.org/downloads
"""
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import datetime as dt

# Set up driver
chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
time.sleep(10)

# Find the big cookie
xpath = '//*[@id="bigCookie"]'
big_cookie = driver.find_element(by=By.XPATH, value=xpath)

# Open the stats tab (necessary to find total cookie count)
stats = driver.find_element(by=By.ID, value='statsButton')
stats.click()

# Click cookie
total_clicks = 10**6
for i in range(total_clicks):
    big_cookie.click()

    # Check every 200 clicks
    if i % 200 == 0:
        # Try to buy the first upgrade
        try:
            upgrade = driver.find_element(by=By.ID, value='upgrade0')
            upgrade.click()
        except:
            pass

        # Try to click the golden cookie
        try:
            golden_cookie = driver.find_element(by=By.CLASS_NAME, value='shimmer')
            golden_cookie.click()
        except:
            pass

    # Check every 5000 clicks
    if i % 5000 == 0:
        # Find total cookie count
        try:
            xpath_cookie = '//*[@id="menu"]/div[3]/div[3]/div'
            cookies = driver.find_element(by=By.XPATH, value=xpath_cookie)
            cookie_count = cookies.text

        # Common error is that stats page was closed; click to reopen
        except:
            stats = driver.find_element(by=By.ID, value='statsButton')
            stats.click()

        # Print status
        remaining = round(100 * i / total_clicks, 2)
        now = dt.datetime.now()
        print(f'{remaining}% done with {cookie_count} cumulative cookies baked as of {now}')

        # Buy buildings
        for j in range(20, -1, -1):
            try:
                building = driver.find_element(by=By.ID, value=f'product{j}')
                building.click()
            except:
                pass

# Close the web page
# driver.quit()
