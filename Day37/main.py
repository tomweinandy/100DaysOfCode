"""
Day 37: Pixela Habit Tracker
"""
import requests

# Define variables
USERNAME = 'lord-of-the-rings'
TOKEN = 'jrr_token'
ENDPOINT = 'https://pixe.la/v1/users'


# Step 1: Create a new account
first_time_creating_account = False
if first_time_creating_account:

    # Define parameters
    user_params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    # Post request to create new account
    response = requests.post(url=ENDPOINT, json=user_params)
    print(response.text)

# Step 2: Create a new graph
first_time_creating_graph = False
if first_time_creating_graph:
    # Define graph endpoint, configurations, header
    graph_endpoint = f'{ENDPOINT}/{USERNAME}/graphs'

    graph_config = {
        'id': 'graph1',
        'name': 'Commitment',
        'unit': 'Github contributions',
        'type': 'int',
        'color': 'sora'
    }

    headers = {
        'X-USER-TOKEN': TOKEN
    }

    # Post request to beuild a graph
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

