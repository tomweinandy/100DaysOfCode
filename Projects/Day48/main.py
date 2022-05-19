"""
Day 48: Automated Game Player

Requires download from https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up driver
chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
time.sleep(10)

# Find the big cookie
xpath = '//*[@id="bigCookie"]'
big_cookie = driver.find_element(by=By.XPATH, value=xpath)

# Click cookie
total_clicks = 10**6
for i in range(total_clicks):
    big_cookie.click()

    # Check every 250 clicks
    if i % 250 == 0:
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

    # Check every 2500 clicks
    if i % 2500 == 0:
        remaining = round(100 * i / total_clicks, 2)
        print(f'{remaining}% done')

        # Buy buildings
        for i in range(20, -1, -1):
            try:
                building = driver.find_element(by=By.ID, value=f'product{i}')
                building.click()
            except:
                pass

# Close the web page
# driver.quit()
