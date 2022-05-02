"""
Day 33: ISS Overhead Notifier
"""
import requests
import datetime as dt
from dateutil import tz


# Define variables, set location for Kalamazoo, Michigan, USA
KZOO_LAT = 42.291707
KZOO_LONG = -85.5872286
KZOO_POSITION = (KZOO_LAT, KZOO_LONG)


def localize(input_datetime, utc=True):
    # Hardcode time zones
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')

    # # Alternatively, can auto-detect time zones
    # from_zone = tz.tzutc()
    # to_zone = tz.tzlocal()

    if utc:
        # Tell the datetime object that it's in UTC time zone since
        # datetime objects are 'naive' by default
        input_datetime = input_datetime.replace(tzinfo=from_zone)

    # Convert time zone
    local_datetime = input_datetime.astimezone(to_zone)

    return local_datetime


def get_sun(sunrise_or_sunset):
    sun_full = sun_data['results'][sunrise_or_sunset]
    sun_string = sun_full.split('+')[0]
    sun = dt.datetime.strptime(sun_string, '%Y-%m-%dT%H:%M:%S')

    return sun


# Get time of local sunrise and sunset
parameters = {
    'lat': KZOO_LAT,
    'lng': KZOO_LONG,
    'formatted': 0
}

sun_response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = get_sun('sunrise')
kzoo_sunrise = localize(sunrise)
sunset = get_sun('sunset')
kzoo_sunset = localize(sunset)

# Although the datetime.now() method does return local time, it still needs to be run through localize().
# This designates it as an off-set aware which allows for comparisons with the local sunrise/set times.
# Execute print(kzoo_sunrise < dt.datetime.now() < kzoo_sunset) for error message
# Doc: https://docs.python.org/2/library/datetime.html#module-datetime
now_offset_naive = dt.datetime.now()
now_offset_aware = localize(now_offset_naive, utc=False)


print(kzoo_sunrise < now_offset_aware < kzoo_sunset)


# Docs: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')

# Print issues
print(iss_response.status_code)
iss_response.raise_for_status()

# Return iss lat/long
iss_data = iss_response.json()
iss_lat = float(iss_data['iss_position']['latitude'])
iss_long = float(iss_data['iss_position']['longitude'])
iss_position = (iss_lat, iss_long)

distance_lat = iss_lat - KZOO_LAT
distance_long = iss_long - KZOO_LONG

iss_near_kzoo = abs(distance_lat) < 5 and abs(distance_long) < 5

print(distance_lat, distance_long, iss_near_kzoo)
