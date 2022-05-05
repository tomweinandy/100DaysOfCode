import ast
import requests


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """

    def __init__(self):
        # Read in credential string and save as a dictionary
        with open('../../../Dropbox/100DaysOfCodePRIVATE/Day39-40Creds.txt') as file:
            creds_str = file.read()
            creds = ast.literal_eval(creds_str)

        # Save tokens as variables
        self.TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'
        self.TEQUILA_KEY = creds['TEQUILA_KEY']

    def search_flight(self, term):
        city = term.lower().replace(' ', '%20')
        search_url = f'{self.TEQUILA_ENDPOINT}' \
                     f'?term={city}' \
                     f'&locale=en-US' \
                     f'&location_types=airport' \
                     f'&limit=1' \
                     f'&active_only=true'

        headers = {'apikey': self.TEQUILA_KEY}

        flight_response = requests.get(url=search_url, headers=headers)
        flight_data = flight_response.json()['locations']



        iata_code = flight_data[0]['city']['code']

        return iata_code
