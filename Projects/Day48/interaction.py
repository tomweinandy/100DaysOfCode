from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

# url = 'https://en.wikipedia.org/wiki/Main_Page'
# driver.get(url)

# # Click article count
# css = '#articlecount a'
# article_count = driver.find_element(by=By.CSS_SELECTOR, value=css)
# print(article_count.text)
# article_count.click()

# # Click another link
# content_portals = driver.find_element(by=By.LINK_TEXT, value='Content portals')
# content_portals.click()

# # Use search bar
# search_bar = driver.find_element(by=By.CLASS_NAME, value='vector-search-box-input')
# search_bar.send_keys('Python')
# search_bar.send_keys(Keys.ENTER)

# Fill out form
lab_report_url = 'https://secure-retreat-92358.herokuapp.com/'
driver.get(lab_report_url)

first_name = driver.find_element(by=By.NAME, value='fName')
first_name.send_keys('Thomas')

last_name = driver.find_element(by=By.NAME, value='lName')
last_name.send_keys('Weinandy')

email = driver.find_element(by=By.NAME, value='email')
email.send_keys('test@email.com')

sign_up = driver.find_element(by=By.CSS_SELECTOR, value='button')
sign_up.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()
