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

# Initialize bot
bot = TwitterBot.InternetSpeedTwitterBot()
print('checkpoint 1')

# Retrieve current download speed
download_speed = bot.get_internet_speed()[0]
print('checkpoint 7')

# Send out mean tweet
message = f"Dear internet provider, my upload speed is only {download_speed}Mbps. I'm not mad, just disappointed"
bot.tweet_at_provider(TWITTER_USERNAME, TWITTER_PASSWORD, message)
print('checkpoint 16')
