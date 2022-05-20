"""
Day 51: Internet Speed Twitter Complaint Bot

Requires download from https://chromedriver.chromium.org/downloads
"""
import json
import TwitterBot
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Load and set credentials
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day51Creds.json') as file:
    creds = json.loads(file.read())

TWITTER_USERNAME = creds['TWITTER_USERNAME']
TWITTER_PASSWORD = creds['TWITTER_PASSWORD']

bot = TwitterBot.InternetSpeedTwitterBot()
upload_speed = bot.get_internet_speed()[0]
print()
print('checkpoint 7')

message = f'Dear internet provider, my upload speed is only {upload_speed}Mbps!'
bot.tweet_at_provider(TWITTER_USERNAME, TWITTER_PASSWORD, message)

print('checkpoint X')

