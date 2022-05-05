"""
Day 38: Workout Activity Tracker

A copy of main that can be run on Replit
"""
import requests
import datetime as dt
import os

# Step 1: Add environment variables
# Doc: https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
SHEETY_KEY = os.environ['SHEETY_KEY']

NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'


GENDER = 'male'
WEIGHT_KG = 74.8
HEIGHT_CM = 180.3
AGE = 33


# Step 2: Sample request from NutritionIX
# Doc: https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/preview
# query = 'Ran for 4 miles'  # sample
query = input('Tell me which exercise you did: ')

api_config = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

# Submit request and retrieve workout data
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=api_config, headers=nutritionix_headers)
workout_data = response.json()

# Parse response
workout = workout_data['exercises'][0]
exercise = workout['name']
duration = workout['duration_min']
calories = workout['nf_calories']

# Get date, time
date = dt.datetime.now().strftime('%d/%m/%Y')
time = dt.datetime.now().strftime('%H:%M:%S')


# Step 3 post results to Google Sheets
# Doc: https://sheety.co/docs/authentication.html
# 'workout' is the name of the active sheet
row_addition = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_KEY}'
}

# Post row to Google Sheet
response = requests.post(url=SHEETY_ENDPOINT, json=row_addition, headers=sheety_headers)
print(response.text)

# See resulting spreadsheet: https://docs.google.com/spreadsheets/d/1czHipPbDaMxBIr6yUKaS_2ADZrnvlbX7lZsWb4W3hCU/
