"""
Day 37: Pixela Habit Tracker
"""
import requests
import datetime as dt

# Define variables
USERNAME = 'lord-of-the-rings'
TOKEN = 'jrr_token'
ENDPOINT = 'https://pixe.la/v1/users'
HEADERS = {'X-USER-TOKEN': TOKEN}
GRAPH_NAME = 'graph1'


# Step 1: Create a new account
# https://docs.pixe.la/entry/post-user
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
# https://docs.pixe.la/entry/post-graph
first_time_creating_graph = False
if first_time_creating_graph:
    # Define graph endpoint, configurations, header
    graph_endpoint = f'{ENDPOINT}/{USERNAME}/graphs'

    graph_config = {
        'id': GRAPH_NAME,
        'name': 'Commitment',
        'unit': 'Github contributions',
        'type': 'int',
        'color': 'sora'
    }

    # Post request to build a graph
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(response.text)


# Step 3: Add a pixel
# https://docs.pixe.la/entry/post-pixel
adding_pixel = False
if adding_pixel:

    # Input information
    quantity = 2
    day = dt.datetime(year=2022, month=1, day=2).strftime('%Y%m%d')
    # day = dt.datetime.today().strftime('%Y%m%d')

    # Define endpoint and configuration
    add_pixel_endpoint = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}'
    add_pixel_config = {
        'date': day,
        'quantity': str(quantity)
    }

    # Post pixel data
    response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=HEADERS)
    print(response.text)


# Step 4: Update a pixel
# https://docs.pixe.la/entry/put-pixel
updating_pixel = False
if updating_pixel:

    # Input information
    quantity = 10
    day = dt.datetime(year=2022, month=1, day=2).strftime('%Y%m%d')
    # day = dt.datetime.today().strftime('%Y%m%d')

    # Define endpoint and configuration
    update_pixel_endpoint = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}/{day}'
    update_pixel_config = {
        'quantity': str(quantity)
    }

    # Update pixel data
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=HEADERS)
    print(response.text)


# Step 5: Delete a pixel
# https://docs.pixe.la/entry/delete-pixel
deleting_pixel = False
if deleting_pixel:

    # Input information
    day = dt.datetime(year=2022, month=1, day=2).strftime('%Y%m%d')
    # day = dt.datetime.today().strftime('%Y%m%d')

    # Define endpoint and configuration
    delete_pixel_endpoint = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}/{day}'

    # Update pixel data
    response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
    print(response.text)
