"""
Day 50: Automated Tinder Swiper

Don't worry, I didn't swipe right on anyone ;)
"""
import ast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day47Creds.txt') as file:
    creds = file.read()
    creds = ast.literal_eval(creds)

EMAIL = creds['DEV_EMAIL']
PASSWORD = creds['DEV_PASSWORD']

# Set up driver
chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

# Go to Tinder
search_url = 'https://tinder.com/'
driver.get(search_url)
time.sleep(1)

# Log on using Facebook
xpath_log_in = '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
log_in = driver.find_element(by=By.XPATH, value=xpath_log_in)
log_in.click()
time.sleep(1)

xpath_log_in_with_facebook = '//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button'
log_in_with_facebook = driver.find_element(by=By.XPATH, value=xpath_log_in_with_facebook)
log_in_with_facebook.click()
time.sleep(1)

# Switch over to pop-up window and log in
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)
time.sleep(1)

enter_email = driver.find_element(by=By.NAME, value='email')
enter_email.send_keys(EMAIL)

enter_password = driver.find_element(by=By.NAME, value='pass')
enter_password.send_keys(PASSWORD)

log_in = driver.find_element(by=By.NAME, value='login')
log_in.click()
time.sleep(5)

# Switch back to base window (Tinder)
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
print(driver.title)

# Allow location
xpath_allow = '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]'
allow = driver.find_element(by=By.XPATH, value=xpath_allow)
allow.click()
time.sleep(1)

# Do not allow notifications
xpath_not_interested = '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[2]'
not_interested = driver.find_element(by=By.XPATH, value=xpath_not_interested)
not_interested.click()
time.sleep(1)

# Accept trackers
xpath_accept = '//*[@id="q1028785088"]/div/div[2]/div/div/div[1]/div[1]/button'
accept = driver.find_element(by=By.XPATH, value=xpath_accept)
accept.click()
time.sleep(10)  # Takes a little time to load singles

# Swipe left
xpath_dislike = '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'
dislike = driver.find_element(by=By.XPATH, value=xpath_dislike)
for i in range(3):
    dislike.click()
    time.sleep(5)
