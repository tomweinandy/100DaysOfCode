"""
Day 52: Instagram Follower Bot
"""
import json
import InstaFollower

# Load and set credentials
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day52Creds.json') as file:
    creds = json.loads(file.read())

USERNAME = creds['USERNAME']
PASSWORD = creds['PASSWORD']

# Log into Instagram
insta = InstaFollower.InstaFollowers()
insta.login(USERNAME, PASSWORD)

# Find followers in target account
target_account = input('Target account to follow followers: ')
insta.find_followers(target_account)

# Follow 144 accounts
insta.follow(144)
