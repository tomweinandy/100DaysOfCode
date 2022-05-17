from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

url = 'https://en.wikipedia.org/wiki/Main_Page'
driver.get(url)

xpath = '//*[@id="articlecount"]/a[1]'
n = driver.find_element(by=By.XPATH, value=xpath)
print(n.text)

driver.close()
