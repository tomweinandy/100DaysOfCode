"""
Day 35: SMS Weather Alerts
Hosted on pythonanywhere.com
****** ADD MY_NUMBER! ******
"""
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


# Define variables, set location for Kalamazoo, Michigan, USA
EXCLUDE = 'current,minutely,daily,alerts'
KZOO_LAT = 42.291707
KZOO_LONG = -85.5872286
OW_KEY = 'bb3d90c7270f80ab31f92b04ac03926c'
ACCOUNT_SID = 'ACd33664c2011667f5609c2c403195f392'  # use live creds
AUTH_TOKEN = 'b7191b319cad0fcba4f9b0bff4f1d14d'     # use live creds
PHONE_NUMBER = '+13254137458'
MY_NUMBER = '+1419*******'

# Alternative
# Step 1: Copy below as one line
# export OW_KAY=bb3d90c7270f80ab31f92b04ac03926c;
# export AUTH_TOKEN=b7191b319cad0fcba4f9b0bff4f1d14d;
# python3 main_hosted.py

# Step 2: Uncomment below
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
    # Set credentials
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

    # Send text
    message = client.messages \
                    .create(
                         body="Bring an umbrella",
                         from_=PHONE_NUMBER,
                         to=MY_NUMBER
                     )

    print(message.status)
