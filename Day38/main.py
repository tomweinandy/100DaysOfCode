"""
Day 38:
"""
import ast
import requests
import datetime as dt


# Step 1: Register for APIs and define variables
APP_ID = '76070878'
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/456c319d2f35d2bab1e1810abb7f6056/myWorkouts/workouts'

GENDER = 'male'
WEIGHT_KG = 74.8
HEIGHT_CM = 180.3
AGE = 33

# Read in credential string and save as a dictionary
with open('../../../Dropbox/100DaysOfCodePRIVATE/Day38Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
API_KEY = creds['API_KEY']
SHEETY_KEY = creds['SHEETY_KEY']


# Step 2: Sample request from NutritionIX
query = 'Ran for 4 miles'
# query = input('Tell me which exorcise you did: ')

api_config = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

# Submit request and retrieve workout data
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=api_config, headers=headers)
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