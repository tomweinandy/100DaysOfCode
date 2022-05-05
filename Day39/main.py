"""
Days 39: Cheap Flight Finder
"""
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search
import flight_data
from pprint import pprint

# Get data from prices worksheet
data = data_manager.DataManager()
sheet_data = data.get_sheet_data()
pprint(sheet_data)

sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
            {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
            {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
            {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
            {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
            {'city': 'Kuala Lumpur',
             'iataCode': '',
             'id': 7,
             'lowestPrice': 414},
            {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
            {'city': 'San Francisco',
             'iataCode': '',
             'id': 9,
             'lowestPrice': 260},
            {'city': 'Cape Town',
             'iataCode': '',
             'id': 10,
             'lowestPrice': 378}]}


# Search flight by city (static for now)
search = flight_search.FlightSearch()

# Check if iataCode present and add if empty
for city_dict in sheet_data['prices']:
    if city_dict['iataCode'] == '':
        # Get iata code
        iata_code = search.search_flight(city_dict['city'])
        # Save to dictionary
        city_dict['iataCode'] = iata_code
        # Add to spreadsheet
        data.add_iata_code(city_dict['id'], city_dict['iataCode'])


for city_dict in sheet_data['prices']:
    # Retrieve flight data
    data = flight_data.FlightData()
    best_flight = data.get_flight_data('LON', city_dict['iataCode'])

    print('Best price:', best_flight['cityTo'], str(round(best_flight['price'], 2)))

    lowest_price = city_dict['lowestPrice'] * 2
    if best_flight['price'] < lowest_price:
        depature_date = best_flight['local_departure'].replace('T', ' ').split('.')[0]
        print(f"Deal found! {best_flight['cityFrom']} to {best_flight['cityTo']} for £{best_flight['price']} "
              f"on {depature_date} \n\n {best_flight['deep_link']}\n")
