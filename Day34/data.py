# Data comes from https://opentdb.com
import requests

# Build parameters to API
parameters = {
    'amount': '10',
    'type': 'boolean',
    'category': '',  # See https://opentdb.com/api_config.php for category codes
    'difficulty': '',
}

# Build API with parameters
base_url = 'https://opentdb.com/api.php'
url = base_url
if len(parameters) > 0:
    url += '?'
    for key, value in parameters.items():
        url += key + '=' + value + '&'
    # Remove the last character (i.e., an extra '&')
    url = url[:-1]
print(url)

# Request question data form API
response = requests.get(url)
response.raise_for_status()
question_data = response.json()['results']
