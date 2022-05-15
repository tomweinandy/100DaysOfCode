"""
Day 47: Amazon Price Tracker
"""
import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint
import json

mixer_url = 'https://www.amazon.com/KitchenAid-KSM150PSER-Artisan-Tilt-Head-Pouring/dp/B00005UP2P/ref=sr_1_3?crid=3W0N492X9XD4I&keywords=kitchenaid%2Bmixer&qid=1652645519&s=home-garden&sprefix=kitchen%2Cgarden%2C272&sr=1-3&th=1'
accept_language_header = 'en-US,en;q=0.9'
user_agent_header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'


response = requests.get(mixer_url,
                        headers={'Accept-Language': accept_language_header, 'User-Agent': user_agent_header})

soup = BeautifulSoup(response.text, 'lxml')

# pprint(soup)

# Extract price from lxml
card_root = soup.find_all(name='div', class_="cardRoot bucket")
data_components_string = card_root[0]['data-components']
data_components_dict = json.loads(data_components_string)
price_string = data_components_dict['1']['price']['displayString']
price_number_string = price_string[1:]
price_float = float(price_string)

print(price_float)
