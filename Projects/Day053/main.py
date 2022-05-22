"""
Day 53: Zillow Data Entry Job Automation
"""
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import numpy as np

# Scrape Zillow data
url_zillow = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22users' \
             'SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.303896' \
             '32177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3' \
             'Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afals' \
             'e%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B' \
             '%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D' \
             '%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%' \
             '22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isList' \
             'Visible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
# url_trulia = 'https://www.trulia.com/for_rent/San_Francisco,CA/1p_beds/0-3000_price/'

# Define header info so Zillow doesn't think I am a bot
accept_language = 'en-US,en;q=0.9'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' \
                    '(KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'

response = requests.get(url_zillow, headers={'Accept-Language': accept_language, 'User-Agent': user_agent})
soup = BeautifulSoup(response.text, 'html.parser')

# Extract json within html cast as string
results_string_bracketed = soup.find_all(type='application/json')[1].text

# Remove first and last characters creating brackets
results_string = results_string_bracketed[4:-3]

# Load as dictionary
results_dict = json.loads(results_string)

# Find list results within
results_list = results_dict['cat1']['searchResults']['listResults']

# Create dataframe
df = pd.DataFrame(columns=['price', 'address', 'url'])

# Loop through results, adding them to a dataframe
# result = results_list[0]
for i in range(len(results_list)):
    result = results_list[i]

    # 1) Try adding the price
    try:
        price = result['unformattedPrice']
    except:
        # If 'unformattedPrice' not present, the address may be multi-unit, requiring additional parsing
        try:
            # Extract the min price from list of units
            min_price = 999999999
            for unit in result['units']:
                price_string_with_characters = unit['price']
                # Remove non-numeric characters before casting as integer
                price_string = re.sub(r'[^0-9]', '', price_string_with_characters)
                price_int = int(price_string)
                if price_int < min_price:
                    min_price = price_int
            price = min_price
        except:
            price = np.nan

    # 2) Try adding address
    try:
        # This one is rather straight-forward
        address = result['address']
    except:
        address = ''

    # 3) Try adding url
    try:
        url = result['detailUrl']
        # Add domain to address if it is missing
        if url[0:5] != 'https':
            url = 'https://www.zillow.com' + url
    except:
        url = ''

    # Append results to dataframe
    result_df = pd.DataFrame({
                            'price': [price],
                            'address': [address],
                            'url': [url]
                            })
    df = df.append(result_df, ignore_index=True)

df.to_csv('data.csv')

# todo fill out form
url_form = 'https://forms.gle/X7JE2Je17GqGKfyd6'
# todo go to Google Sheet
