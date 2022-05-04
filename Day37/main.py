"""
Day 37: Pixela Habit Tracker
"""
import requests

# Define variables
USERNAME = 'lord-of-the-rings'
TOKEN = 'jrr_token'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Create a new by setting variable to True
first_time_creating_account = False

if first_time_creating_account:
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

