from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        # Set up driver
        self.chrome_driver_path = Service('/Applications/chromedriver')
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.up = 'pass'
        self.down = 'pass'
        print('checkpoint 0')

    def quit(self):
        """
        Quits the Chrome browser
        """
        self.driver.quit()

    def get_internet_speed(self):
        """
        Tests the internet speed
        :return: Current internet speed in Mbps
        """
        # Opens a website to test the internet speed
        url_speed = 'https://www.speedtest.net'
        self.driver.get(url_speed)
        time.sleep(15)
        print('checkpoint 2')

        # Begins speed test (takes 30-40 seconds to run)
        xpath_go = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        go = self.driver.find_element(by=By.XPATH, value=xpath_go)
        go.click()
        print('checkpoint 3')
        time.sleep(45)
        print('checkpoint 4')

        # Saves the internet download speed value
        xpath_download = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'
        download = self.driver.find_element(by=By.XPATH, value=xpath_download)
        download_speed = download.text
        print('checkpoint 5')

        # Saves the internet upload speed value
        old_xpath_upload = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]'
        xpath_upload = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]'
        xpath_upload = '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'

        upload = self.driver.find_element(by=By.XPATH, value=xpath_upload)
        upload_speed = upload.text
        print('checkpoint 6')

        return download_speed, upload_speed

    def tweet_at_provider(self, username, password, tweet_message):
        """
        Sends tweet with the current internet speed
        :param username: Twitter account
        :param password: Twitter password
        :param tweet_message: Tweet
        """
        # Opens Twitter website
        url_twitter = 'https://www.twitter.com'
        self.driver.get(url_twitter)
        time.sleep(10)
        print('checkpoint 8')

        xpath_sign_in = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a'
        sign_in = self.driver.find_element(by=By.XPATH, value=xpath_sign_in)
        sign_in.click()
        time.sleep(20)
        print('checkpoint 9')

        xpath_username_input = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        username_input = self.driver.find_element(by=By.XPATH, value=xpath_username_input)
        username_input.send_keys(username)
        print('checkpoint 10')

        xpath_next = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
        next = self.driver.find_element(by=By.XPATH, value=xpath_next)
        next.click()
        time.sleep(5)
        print('checkpoint 11')

        xpath_password_input = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        password_input = self.driver.find_element(by=By.XPATH, value=xpath_password_input)
        password_input.send_keys(password)
        print('checkpoint 12')

        xpath_log_in = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div'
        log_in = self.driver.find_element(by=By.XPATH, value=xpath_log_in)
        log_in.click()
        time.sleep(10)
        print('checkpoint 13')


        self.driver.get('https://twitter.com/compose/tweet')
        print('checkpoint 14')
        time.sleep(5)

        xpath_compose_tweet = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        compose_tweet = self.driver.find_element(by=By.XPATH, value=xpath_compose_tweet)
        compose_tweet.send_keys(tweet_message)
        print('checkpoint 15', tweet_message)

        xpath_tweet = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'
        tweet = self.driver.find_element(by=By.XPATH, value=xpath_tweet)
        tweet.click()
