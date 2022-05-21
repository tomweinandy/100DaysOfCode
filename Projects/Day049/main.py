"""
Day 49: Automate LinkedIn Job Application

Requires download from https://chromedriver.chromium.org/downloads
"""
import ast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day49Creds.txt') as file:
    creds = file.read()
    creds = ast.literal_eval(creds)

EMAIL = creds['EMAIL']
PASSWORD = creds['PASSWORD']

# Set up driver
chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

search_url = 'https://www.linkedin.com/jobs/search/' \
             '?f_AL=true' \
             '&f_CR=103644278' \
             '&f_JT=F' \
             '&f_WT=2' \
             '&geoId=92000000' \
             '&keywords=economist' \
             '&location=Worldwide' \
             '&sortBy=R'
driver.get(search_url)

sign_in = driver.find_element(by=By.CLASS_NAME, value='nav__button-secondary')
sign_in.click()
time.sleep(1)

# Go through the steps to apply for a job
enter_email = driver.find_element(by=By.ID, value='username')
enter_email.send_keys(EMAIL)

enter_password = driver.find_element(by=By.ID, value='password')
enter_password.send_keys(PASSWORD)

sign_in2 = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in2.click()

easy_apply = driver.find_element(by=By.CLASS_NAME, value='jobs-apply-button--top-card')
easy_apply.click()
time.sleep(5)

next_class = 'artdeco-button artdeco-button--2 artdeco-button--primary ember-view'
xpath = '//*[@id="ember442"]'
next = driver.find_element(by=By.XPATH, value='//*[@id="ember442"]')
next.click()

# I am stopping here because I do not actually want to apply to a job automatically
