"""
Day 47: Amazon Price Tracker
"""
import requests
from bs4 import BeautifulSoup
import json
import smtplib

# Set url and headers
product_url = 'https://www.amazon.com/KitchenAid-KSM150PSER-Artisan-Tilt-Head-Pouring/dp/B00005UP2P/ref=sr_1_3' \
            '?crid=3W0N492X9XD4I&keywords=kitchenaid%2Bmixer' \
            '&qid=1652645519&s=home-garden' \
            '&sprefix=kitchen%2Cgarden%2C272&sr=1-3&th=1'
accept_language_header = 'en-US,en;q=0.9'
user_agent_header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit' \
                    '/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'

# Scrape website
response = requests.get(product_url,
                        headers={'Accept-Language': accept_language_header, 'User-Agent': user_agent_header})

# Initialize response in BS class
soup = BeautifulSoup(response.text, 'lxml')

# Extract price from lxml
card_root = soup.find_all(name='div', class_="cardRoot bucket")
data_components_string = card_root[0]['data-components']
data_components_dict = json.loads(data_components_string)
price_string = data_components_dict['1']['price']['displayString']
price_number_string = price_string[1:]
price_float = float(price_number_string)
print(price_float)

# Compare price against reservation price
reservation_price = 399
if price_float <= reservation_price:
    # If reservation price is lower, email myself the url
    # Load credentials
    with open('../../../Dropbox/100DaysOfCodePrivate/Day47Creds.txt') as file:
        text = file.read()
        creds = json.loads(text)
    DEV_EMAIL = creds['DEV_EMAIL']
    DEV_PASSWORD = creds['DEV_PASSWORD']
    PERSONAL_EMAIL = creds['PERSONAL_EMAIL']

    # Set up SMTP connection
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Start Transfer Layer Security encryption
        connection.starttls()
        connection.login(user=DEV_EMAIL, password=DEV_PASSWORD)
        connection.sendmail(from_addr=DEV_EMAIL,
                            to_addrs=PERSONAL_EMAIL,
                            msg=f'Subject: Reservation Price met!'
                                f'\n\nCheck out the deal at {product_url}')
    print('Email sent.')

else:
    print('No email sent.')