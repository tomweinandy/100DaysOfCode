from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class InstaFollowers:
    def __init__(self):
        # Set up driver
        self.chrome_driver_path = Service('/Applications/chromedriver')
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)

    def login(self, username, password):
        # Log in
        url = f'https://www.instagram.com'
        self.driver.get(url)
        time.sleep(5)

        # Add usernames and password
        username_field = self.driver.find_element(by=By.NAME, value='username')
        username_field.send_keys(username)

        password_field = self.driver.find_element(by=By.NAME, value='password')
        password_field.send_keys(password)

        xpath_log_in = '//*[@id="loginForm"]/div/div[3]/button/div'
        log_in = self.driver.find_element(by=By.XPATH, value=xpath_log_in)
        log_in.click()
        time.sleep(2.5)

        # Do not save password now
        try:
            xpath_save_not_now = '//*[@id="react-root"]/section/main/div/div/div/div/button'
            save_not_now = self.driver.find_element(by=By.XPATH, value=xpath_save_not_now)
            save_not_now.click()
            time.sleep(2.5)
        except:
            pass

        # Do allow notifications
        try:
            xpath_notify_not_now = '/html/body/div[5]/div/div/div/div[3]/button[2]'
            notify_not_now = self.driver.find_element(by=By.XPATH, value=xpath_notify_not_now)
            notify_not_now.click()
            time.sleep(2.5)
        except:
            pass

    def find_followers(self, account):
        # Go to target account
        url = f'https://www.instagram.com/{account}'
        self.driver.get(url)
        time.sleep(2.5)

        # Select followers
        xpath_followers = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'
        followers = self.driver.find_element(by=By.XPATH, value=xpath_followers)
        followers.click()

    def follow(self):
        pass
