import ast
import requests
import datetime as dt


class FlightData:
    """
    This class is responsible for structuring the flight data.
    Doc: https://tequila.kiwi.com/portal/docs/tequila_api/search_api
    """
    def __init__(self):
        # Read in credential string and save as a dictionary
        with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day39Creds.txt') as file:
            creds_str = file.read()
            creds = ast.literal_eval(creds_str)

        self.TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
        self.TEQUILA_KEY = creds['TEQUILA_KEY']

    def get_flight_data(self, fly_from_iata_code, fly_to_iata_code):
        """
        Find the best flights between two cities from tomorrow to six months in the future
        :param fly_from_iata_code: Three-letter code of source city
        :param fly_to_iata_code: Three-letter code of destination city
        :return: A json of the lowest-cost flight that meets the stated criteria
        """
        tomorrow_dt = dt.datetime.today() + dt.timedelta(1)
        six_months_dt = dt.datetime.today() + dt.timedelta(6 * 30)
        tomorrow = tomorrow_dt.strftime('%d/%m/%Y')
        six_months = six_months_dt.strftime('%d/%m/%Y')

        flight_data_url = f'{self.TEQUILA_ENDPOINT}' \
                          f'?fly_from={fly_from_iata_code}' \
                          f'&fly_to={fly_to_iata_code}' \
                          f'&date_from={tomorrow}' \
                          f'&date_to={six_months}' \
                          f'&nights_in_dst_from=6' \
                          f'&nights_in_dst_to=27' \
                          f'&flight_type=round' \
                          f'&one_for_city=0' \
                          f'&one_per_date=0' \
                          f'&adults=1' \
                          f'&selected_cabins=M' \
                          f'&adult_hold_bag=1' \
                          f'&adult_hand_bag=1' \
                          f'&partner_market=us' \
                          f'&curr=GBP' \
                          f'&max_stopovers=0' \
                          f'&limit=1'

        headers = {'apikey': self.TEQUILA_KEY}
        response = requests.get(url=flight_data_url, headers=headers)
        # response.raise_for_status()

        best_flight_returned = response.json()['data'][0]
        return best_flight_returned
