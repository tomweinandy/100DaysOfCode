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


def get_sun_local(sunrise_or_sunset):
    sun_full = data['results'][sunrise_or_sunset]
    sun_string = sun_full.split('+')[0]
    sun_utc = dt.datetime.strptime(sun_string, '%Y-%m-%dT%H:%M:%S')

    # Hardcode time zones
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')

    # # Alternatively, can auto-detect time zones
    # from_zone = tz.tzutc()
    # to_zone = tz.tzlocal()

    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    sun_utc = sun_utc.replace(tzinfo=from_zone)

    # Convert time zone
    sun_local = sun_utc.astimezone(to_zone)

    return sun_local



# # Docs: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response.status_code)
#
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (latitude, longitude)

parameters = {
    'lat': KZOO_LAT,
    'lng': KZOO_LONG,
    'formatted': 0
}

sunrise_response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
sunrise_response.raise_for_status()
data = sunrise_response.json()

sun = get_sun_local('sunrise')



print(sun)

