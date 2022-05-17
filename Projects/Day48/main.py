"""
Day 48

Requires download from https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
time.sleep(30)

xpath = '//*[@id="bigCookie"]'
big_cookie = driver.find_element(by=By.XPATH, value=xpath)

# Click cookie
for i in range(100):
    big_cookie.click()

# Buy cursor
cursor = driver.find_element(by=By.ID, value='product0')
cursor.click()


# time.sleep(100)

# Close the web page
# driver.close()
# driver.quit()

