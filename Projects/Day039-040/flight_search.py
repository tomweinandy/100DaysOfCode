import ast
import requests


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    Doc: https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
    """

    def __init__(self):
        # Read in credential string and save as a dictionary
        with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day39Creds.txt') as file:
            creds_str = file.read()
            creds = ast.literal_eval(creds_str)

        # Save tokens as variables
        self.TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'
        self.TEQUILA_KEY = creds['TEQUILA_KEY']

    def search_flight(self, term):
        """
        Finds the IATA code for a natural-language input
        :param term: The term to be searched for by the API (in this case, a destination city).
        :return: The three-letter city IATA code
        """
        city = term.lower().replace(' ', '%20')
        search_url = f'{self.TEQUILA_ENDPOINT}' \
                     f'?term={city}' \
                     f'&locale=en-US' \
                     f'&location_types=airport' \
                     f'&limit=1' \
                     f'&active_only=true'

        headers = {'apikey': self.TEQUILA_KEY}

        flight_response = requests.get(url=search_url, headers=headers)
        flight_response.raise_for_status()
        flight_search = flight_response.json()['locations']

        iata_code = flight_search[0]['city']['code']

        return iata_code
