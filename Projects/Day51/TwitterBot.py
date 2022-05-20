from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class InternetSpeedTwitterBot:
    def __init__(self):
        # Set up driver
        self.chrome_driver_path = Service('/Applications/chromedriver')
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.up = 'pass'
        self.down = 'pass'

    def get_internet_speed(self):
        """
        Internet speed should be at least 30mbps
        :return:
        """
        return 25

    def tweet_at_provider(self):
        pass

