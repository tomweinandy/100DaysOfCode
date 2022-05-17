"""
Day 48

Requires download from https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# # Deprecated method
# chrome_driver_path = '/Applications/chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver_path = Service('/Applications/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)


product_url = 'https://www.amazon.com/KitchenAid-KSM150PSER-Artisan-Tilt-Head-Pouring/dp/B00005UP2P/ref=sr_1_3' \
            '?crid=3W0N492X9XD4I&keywords=kitchenaid%2Bmixer' \
            '&qid=1652645519&s=home-garden' \
            '&sprefix=kitchen%2Cgarden%2C272&sr=1-3&th=1'

url = 'https://www.python.org/'
driver.get(url)

events_dict = {}

for i in range(1, 6):
    xpath_date = f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time'
    date = driver.find_element(by=By.XPATH, value=xpath_date).text
    xpath_event = f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/a'
    event = driver.find_element(by=By.XPATH, value=xpath_event).text

    try:
        events_dict[date].append(event)
    except KeyError:
        events_dict[date] = [event]

print(events_dict)
# time.sleep(20)

# Close the web page
driver.close()
# driver.quit()

