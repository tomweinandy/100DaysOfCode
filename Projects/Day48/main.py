"""
Day 48

Requires download from https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# # Deprecated method
# chrome_driver_path = '/Applications/chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
#
# driver.get(product_url)
# price = driver.find_element('priceblock_ourprice')
# print(price.text)
# print(driver.find_element())

# time.sleep(20)

# Close the web page
# driver.close()
driver.quit()

