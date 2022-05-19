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

# First log directly into Facebook to enable account
url = 'https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1652967176022%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ad66b803338bc%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff125cecd260d9a8%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Df18a091cd9119d%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e4f88588d8d5%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff125cecd260d9a8%2526relation%253Dopener%2526frame%253Df34c1d42ce356%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e4f88588d8d5%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff125cecd260d9a8%26relation%3Dopener%26frame%3Df34c1d42ce356%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0'
driver.get(url)
time.sleep(1)

enter_email = driver.find_element(by=By.NAME, value='email')
enter_email.send_keys(EMAIL)

enter_password = driver.find_element(by=By.NAME, value='pass')
enter_password.send_keys(PASSWORD)

log_in = driver.find_element(by=By.NAME, value='login')
log_in.click()
time.sleep(1)

# Not log into Tinder
search_url = 'https://tinder.com/'
driver.get(search_url)
time.sleep(1)

# todo fix issue of not logging into fb
xpath_log_in = '//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
log_in = driver.find_element(by=By.XPATH, value=xpath_log_in)
log_in.click()
time.sleep(5)

xpath_log_in_with_facebook = '//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button'
log_in_with_facebook = driver.find_element(by=By.XPATH, value=xpath_log_in_with_facebook)
log_in_with_facebook.click()
time.sleep(5)

xpath_allow = '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]'
allow = driver.find_element(by=By.XPATH, value=xpath_allow)
allow.click()
time.sleep(2)

xpath_not_interested = '//*[@id="q-699595988"]/div/div/div/div/div[3]/button[2]'
not_interested = driver.find_element(by=By.XPATH, value=xpath_not_interested)
not_interested.click()
