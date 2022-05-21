"""
Day 33: ISS Overhead Notifier
"""
import requests
import datetime as dt
from dateutil import tz
import smtplib
import time

# Define variables, set location for Kalamazoo, Michigan, USA
KZOO_LAT = 42.291707
KZOO_LONG = -85.5872286
KZOO_POSITION = (KZOO_LAT, KZOO_LONG)

# Add dummy email account used to send email
my_username = 'ignorethistest2022'
my_domain = '@gmail.com'
my_email = my_username + my_domain

# Add password for dummy account
file_path = 'not_very_secure.txt'
with open(file_path) as file:
    my_password = file.read()

# Add destination email
destination_email = my_email

def localize(input_datetime, utc=True):
    """
    Converts datetime to local time and makes datetime off-set aware
    :param input_datetime: A datetime of interest
    :param utc: True if datetime in UTC, False if datetime already is local
    :return: The local, off-set aware datetime
    """
    # Hardcode time zones
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')

    # # Alternatively, can auto-detect time zones
    # from_zone = tz.tzutc()
    # to_zone = tz.tzlocal()

    if utc:
        # Tell the datetime object that it's in UTC time zone since
        input_datetime = input_datetime.replace(tzinfo=from_zone)

    # Convert time zone
    local_datetime = input_datetime.astimezone(to_zone)
    return local_datetime


def get_sun(sunrise_or_sunset):
    """
    Fetches the sunrise time or sunset time for Kalamazoo, Michigan
    :param sunrise_or_sunset: 'sunrise' or 'sunset'
    :return: Sunrise or sunset datetime
    """
    sun_full = sun_data['results'][sunrise_or_sunset]

    # Only uses up to the second
    sun_string = sun_full.split('+')[0]

    # Converts the returned string to datetime
    sun = dt.datetime.strptime(sun_string, '%Y-%m-%dT%H:%M:%S')
    return sun


def send_email():
    """
    Sends an email to look up.
    Had to reduce security level detailed here:
    https://www.udemy.com/course/100-days-of-code/learn/lecture/21712834#questions/13766454
    """
    # Set up SMTP connection
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Start Transfer Layer Security encryption
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=destination_email,
                            msg=f'Subject: Look Up!'
                                f'\n\nThe ISS is near Kalamazoo, Michigan! Look at {distance_lat}, {distance_long}.')


# Runs loop continuously every minute
while True:
    # Get data of local sunrise and sunset times
    parameters = {
        'lat': KZOO_LAT,
        'lng': KZOO_LONG,
        'formatted': 0
    }
    sun_response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    # Returns specific time strings and converts to local datetimes
    sunrise = get_sun('sunrise')
    kzoo_sunrise = localize(sunrise)
    sunset = get_sun('sunset')
    kzoo_sunset = localize(sunset)

    # Get local time
    # Although the datetime.now() method does return local time, it still needs to be run through localize().
    # This designates it as an off-set aware which allows for comparisons with the local sunrise/set times.
    # Execute print(kzoo_sunrise < dt.datetime.now() < kzoo_sunset) for error message
    # Doc: https://docs.python.org/2/library/datetime.html#module-datetime
    now_offset_naive = dt.datetime.now()
    now_offset_aware = localize(now_offset_naive, utc=False)

    # Determines if it is daylight
    is_daylight = kzoo_sunrise < now_offset_aware < kzoo_sunset

    # Gets location of the ISS
    # Docs: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')

    # Print issues
    iss_response.raise_for_status()

    # Return iss latitude/longitude
    iss_data = iss_response.json()
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_long = float(iss_data['iss_position']['longitude'])
    iss_position = (iss_lat, iss_long)

    # Compares ISS distance from Kalamazoo, Michigan
    distance_lat = iss_lat - KZOO_LAT
    distance_long = iss_long - KZOO_LONG

    # Determines if ISS is near Kalamazoo, Michigan
    iss_near_kzoo = abs(distance_lat) <= 5 and abs(distance_long) <= 5

    # Prints some output
    print()

    # Sends email if it is dark and the ISS is nearby
    if iss_near_kzoo and not is_daylight:
        send_email()
        print(f'Sent email at {dt.datetime.now()}')
    else:
        print(f'Did not send email at {dt.datetime.now()}'
              f'\n    Daylight right now: {is_daylight}'
              f'\n    ISS near Kalamazoo: {iss_near_kzoo}'
              f'\n    Current ISS location: {distance_lat}, {distance_long}')

    time.sleep(60)