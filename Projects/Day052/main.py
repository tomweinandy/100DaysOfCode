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

insta = InstaFollower.InstaFollowers()
insta.login(USERNAME, PASSWORD)



