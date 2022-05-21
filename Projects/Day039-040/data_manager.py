import ast
import requests


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    Doc: https://sheety.co/docs/requests
    """
    def __init__(self):
        # Read in credential string and save as a dictionary
        with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day39Creds.txt') as file:
            creds_str = file.read()
            creds = ast.literal_eval(creds_str)

        # Save tokens as variables
        self.SHEETY_ENDPOINT = creds['SHEETY_ENDPOINT']
        self.SHEETY_KEY = creds['SHEETY_KEY']
        self.headers = {'Authorization': f'Bearer {self.SHEETY_KEY}'}

        # Read data from prices sheet
        get_response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.headers)
        get_response.raise_for_status()
        self.sheet_data = get_response.json()

    def add_iata_code(self, row_id, iata_code):
        """
        Adds the found IATA code to Google Sheets
        :param row_id: Row index on Google Sheets
        :param iata_code: Three-digit city code
        :return:
        """
        # NOTE: the worksheet name is 'prices' but Sheety only accepts 'price'
        row_edit_json = {
            'price': {
                'iataCode': iata_code
            }
        }

        row_edit_url = f'{self.SHEETY_ENDPOINT}/{row_id}'

        put_request = requests.put(url=row_edit_url, json=row_edit_json, headers=self.headers)
        print(put_request.raise_for_status())
