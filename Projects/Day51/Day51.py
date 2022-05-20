"""
Day 51: Internet Speed Twitter Complaint Bot

Requires download from https://chromedriver.chromium.org/downloads
"""
import json
import TwitterBot

# Load and set credentials
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day51Creds.json') as file:
    creds = json.loads(file.read())

TWITTER_USERNAME = creds['TWITTER_USERNAME']
TWITTER_PASSWORD = creds['TWITTER_PASSWORD']
INTERNET_USERNAME = creds['INTERNET_USERNAME']
INTERNET_PASSWORD = creds['INTERNET_PASSWORD']

bot = TwitterBot.InternetSpeedTwitterBot()

bot
