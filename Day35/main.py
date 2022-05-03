"""
Day 35: SMS Weather Alerts

# Doc: https://openweathermap.org/api/one-call-api
"""
import os

import requests
from twilio.rest import Client

# Define variables, set location for Kalamazoo, Michigan, USA
EXCLUDE = 'current,minutely,daily,alerts'
KZOO_LAT = 42.291707
KZOO_LONG = -85.5872286
OW_KEY = 'bb3d90c7270f80ab31f92b04ac03926c'
ACCOUNT_SID = 'ACd33664c2011667f5609c2c403195f392'  # use live creds (not test)
AUTH_TOKEN1 = 'dd697ab918d203f7'
AUTH_TOKEN2 = 'c4523abe594cc409'
AUTH_TOKEN = AUTH_TOKEN1 + AUTH_TOKEN2
PHONE_NUMBER = '+13254137458'


# Get my phone number (saved locally)
file_path = '../../Downloads/my_number.txt'
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
# Step 1: In terminal set 'export OW_KAY=bb3d90c7270f80ab31f92b04ac03926c'
# Step 2: In terminal set 'export AUTH_TOKEN=*****'
# Step 3: Uncomment below
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
                         to=my_number
                     )

    print(message.status)



