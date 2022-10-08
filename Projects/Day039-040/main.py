"""
Days 39-40: Cheap Flight Finder
"""
import data_manager
import flight_search
import flight_data
import notification_manager

# Get data from prices worksheet
data = data_manager.DataManager()
sheet_data = data.sheet_data
# pprint(sheet_data)

# Search flight by city (static for now)
search = flight_search.FlightSearch()

# Check if iataCode present and add if empty
for city_dict in sheet_data['prices']:
    if city_dict['iataCode'] == '':  # consider using city_dict.get('iataCode', False) which is better in if conditions
        # Get iata code
        iata_code = search.search_flight(city_dict['city'])
        # Save to dictionary
        city_dict['iataCode'] = iata_code
        # Add to spreadsheet
        data.add_iata_code(city_dict['id'], city_dict['iataCode'])

# Find the best flight to each city from London
for city_dict in sheet_data['prices']:
    # Retrieve flight data
    data = flight_data.FlightData()
    best_flight = data.get_flight_data('LON', city_dict['iataCode'])

    print('Best price:', best_flight['cityTo'], str(round(best_flight['price'], 2)))

    # Check if the best-priced flight is below the reservation price set on the Google Sheet
    lowest_price = city_dict['lowestPrice']
    if best_flight['price'] < lowest_price:
        departure_date = best_flight['local_departure'].replace('T', ' ').split('.')[0]
        message_to_send = f"Deal found! {best_flight['cityFrom']}-{best_flight['flyFrom']} to {best_flight['cityTo']}" \
                          f"-{best_flight['flyTo']} for £{best_flight['price']} on {departure_date}" \
                          f"\n\n {best_flight['deep_link']}"

        # Send message if condition met
        # Change running_locally=False if running code on the cloud
        sms = notification_manager.NotificationManager(running_locally=True)
        sms.send_message(message_to_send)
