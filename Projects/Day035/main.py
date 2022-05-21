"""
Day 35: SMS Weather Alerts

# Doc: https://openweathermap.org/api/one-call-api
"""
import ast
import requests
from twilio.rest import Client

# Define variables, set location for Kalamazoo, Michigan, USA
EXCLUDE = 'current,minutely,daily,alerts'
KZOO_LAT = 42.291707
KZOO_LONG = -85.5872286

# Read in credential string and save as a dictionary
with open('../../../Dropbox/100DaysOfPython_PRIVATE/Day35Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
OW_KEY = creds['OW_KEY']
ACCOUNT_SID = creds['ACCOUNT_SID']  # use live creds (not test)
AUTH_TOKEN = creds['AUTH_TOKEN']
PHONE_NUMBER = creds['TWILIO_NUMBER']
MY_NUMBER = creds['TOMS_NUMBER']

# Get my phone number (saved locally)
file_path = '../../Dropbox/100DaysOfCodePRIVATE/my_number.txt'
with open(file_path) as file:
    my_number = file.read()

print(type(my_number))

# Set credentials
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Alternative 1 for setting environmental variables in the console. See http://twil.io/secure
# account_sid = os.environ['ACCOUNT_SID']
# auth_token = os.environ['AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# Alternative 2
# Step 1: In terminal set 'export OW_KEY=******'
# Step 2: In terminal set 'export AUTH_TOKEN=*****'
# Step 3: Uncomment below
# import os
# OW_KEY = os.environ.get('OW_KEY')
# AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

# Build URL
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={KZOO_LAT}&lon={KZOO_LONG}&exclude={EXCLUDE}&appid={OW_KEY}'
print(url)

# Get results and print status
response = requests.get(url)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()

# Determine if it will rain in the next 12 hours
will_rain = False
for i in range(12):
    hour_weather_id = weather_data['hourly'][i]['weather'][0]['id']
    if hour_weather_id < 700:
        will_rain = True

# Send SMS if it will rain
if will_rain:
    message = client.messages \
                    .create(
                         body="Bring an umbrella",
                         from_=PHONE_NUMBER,
                         to=MY_NUMBER
                     )

    print(message.status)
