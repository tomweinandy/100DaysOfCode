import ast
import requests


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self):
        # Read in credential string and save as a dictionary
        with open('../../../Dropbox/100DaysOfCodePRIVATE/Day39Creds.txt') as file:
            creds_str = file.read()
            creds = ast.literal_eval(creds_str)

        # Save tokens as variables
        self.SHEETY_ENDPOINT = creds['SHEETY_ENDPOINT']
        self.SHEETY_KEY = creds['SHEETY_KEY']

        # Read data from prices sheet
        get_response = requests.get(url=self.SHEETY_ENDPOINT)
        # get_response.raise_for_status()
        self.sheet_data = get_response.json()

    def get_sheet_data(self):
        return self.sheet_data

    def add_iata_code(self, row_id, iata_code):
        # NOTE: the worksheet name is 'prices' but Sheety only accepts 'price'
        row_edit_json = {
            'price': {
                'iataCode': iata_code
            }
        }

        headers = {
            'Authorization': f'Bearer {self.SHEETY_KEY}'
        }
        row_edit_url = f'{self.SHEETY_ENDPOINT}/{row_id}'

        put_request = requests.put(url=row_edit_url, json=row_edit_json, headers=headers)
        # print(put_request.raise_for_status())
