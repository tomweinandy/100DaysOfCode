"""
Day 35: SMS Weather Alerts

# Doc: https://openweathermap.org/api/one-call-api
"""
import requests
import os
from twilio.rest import Client

# Define variables, set location for Kalamazoo, Michigan, USA
EXCLUDE = 'current,minutely,daily,alerts'
KZOO_LAT = 42.291707
KZOO_LONG = -85.5872286
OW_KEY = 'bb3d90c7270f80ab31f92b04ac03926c'
ACCOUNT_SID = 'ACfcebc83853ac47dce4bf328af90994ac'
AUTH_TOKEN = 'ACd33664c2011667f5609c2c403195f392'
PHONE_NUMBER = '+13254137458'

# Get my phone number (saved locally)
file_path = '../../Downloads/my_number.txt'
with open(file_path) as file:
    my_number = file.read()

print(type(my_number))

# Build URL
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={KZOO_LAT}&lon={KZOO_LONG}&exclude={EXCLUDE}&appid={OW_KEY}'
print(url)

# # Get results and print status
# response = requests.get(url)
# print(response.status_code)
# response.raise_for_status()
# weather_data = response.json()
#
# # Determine if it will rain in the next 12 hours
# will_rain = False
# for i in range(12):
#     hour_weather_id = weather_data['hourly'][i]['weather'][0]['id']
#     if hour_weather_id < 700:
#         will_rain = True
# if will_rain:
#     print('Bring an umbrella')

# Set the environment variables. See http://twil.io/secure
# account_sid = os.environ['ACCOUNT_SID']
# auth_token = os.environ['AUTH_TOKEN']
# client = Client(account_sid, auth_token)
client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=PHONE_NUMBER,
                     to=my_number
                 )

print(message.status)



