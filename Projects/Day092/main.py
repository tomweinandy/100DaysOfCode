"""
Day 92: Craft Beer Web Scraper
"""
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time
import pandas as pd
import numpy as np
import re

# todo restart scrape with 1min sleep between products (if it keeps stopping at 24, change the sleep time back to 20s)


def extract_text(scrape: str):
    """
    Extract text out of scraped html using BeautifulSoup
    :param scrape: A string of the scraped html
    :return: The extracted text
    """
    try:
        txt = scrape.text
        txt = txt.replace('\n', '')
        txt = txt.replace('\t', '')
        txt = txt.strip()  # removes leading and trailing whitespaces
    except AttributeError:
        txt = np.nan

    return txt


def get_dynamic_soup(url_to_scrape: str, pause=60) -> BeautifulSoup:
    """
    Adds a delay within the scraper to allow for page rendering (5s is good) and throttle prevention (20s was too
    little; the website seems okay with a 60s delay).
    :param url_to_scrape: webpage with products
    :param pause: delay
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url_to_scrape)
        time.sleep(pause)
        chowder = BeautifulSoup(page.content(), "html.parser")
        browser.close()
        return chowder


url = 'https://www.target.com/c/craft-beer-wine-liquor-grocery/-/N-o3thc'

# Scrape html
soup = get_dynamic_soup(url)

# Extract the number of items from the search (two separate approaches)
try:
    raw_results = soup.find_all(class_='cDsKNn')[-1]
    results = extract_text(raw_results)
    print(results)
    num_only = re.sub(r'[^0-9]', '', results)
    num_results = int(num_only)
except ValueError:
    raw_results = soup.find_all(class_='h-margin-b-tiny')[0]
    results = extract_text(raw_results)
    num_results = int(results.split()[0])


# Target only displays 24 products at a time, so page 2 begins with the 25th product (but includes "Nao=24" in url)
# Take number of results and make a list of 24-item intervals for each page (e.g., n=49 becomes [0, 24, 48])
n = (num_results - 1) // 24
page_intervals = [i*24 for i in range(n+1)]
print(page_intervals) #todo remove testing prints

# Create empty dataframe and counter
df = pd.DataFrame()
counter = 0

print(f'Will scrape {len(page_intervals)} page(s) of {num_results} products\n')

# Loop through all pages
for interval in page_intervals:
    print(f'Finished scraping {num_results} products\n')

    # Re-scrape after the first page
    if interval != 0:
        # Scrape html
        url = f'https://www.target.com/c/craft-beer-wine-liquor-grocery/-/N-o3thc?Nao={interval}'
        soup = get_dynamic_soup(url)

    print('URL:', url)

    # Find all product cards
    product_wrapper_list = soup.find_all('div', {'data-test': '@web/site-top-of-funnel/ProductCardWrapper'})

    if len(product_wrapper_list) == 0:
        print('No products found on page.')

    # Loop through all products
    for product in product_wrapper_list:
        # Get image URLs
        product_url = product.select(selector='div div h3 a')[0]['href']
        product_url = product_url.split('#')[0]
        long_url = 'https://target.com' + product_url

        # Scrape entire product page from long_url
        p_soup = get_dynamic_soup(long_url)

        # Get name
        raw_name = p_soup.find('h1')
        name = extract_text(raw_name)

        # Get price
        raw_price = p_soup.find('span', {'data-test': 'product-price'})
        price = extract_text(raw_price)

        # Get items from Specifications section
        specifications = p_soup.find('div', {'data-test': 'item-details-specifications'})
        list_specifications = specifications.select(selector='div')
        dict = {}

        # Loop through each specification and add to dictionary
        for spec in list_specifications:
            long_spec = extract_text(spec)
            list_spec = long_spec.split(':')
            key = list_spec[0].strip()
            value = list_spec[-1].strip()
            dict[key] = value

        # Store item as variable, if it exists
        try:
            alcohol = dict['Alcohol Percentage']
        except KeyError:
            alcohol = np.nan

        try:
            region = dict['Region']
        except KeyError:
            region = np.nan

        try:
            quantity = dict['Package Quantity']
        except KeyError:
            quantity = np.nan

        try:
            weight = dict['Net weight']
        except KeyError:
            weight = np.nan

        try:
            country = dict['Country of Origin']
        except KeyError:
            country = np.nan

        try:
            upc = dict['UPC']
        except KeyError:
            upc = np.nan

        # Get stars and ratings
        try:
            raw_reviews = p_soup.find('span', class_=lambda value: value and value.startswith('utils__ScreenReaderOnly'))
            string_reviews = extract_text(raw_reviews)
            list_reviews = string_reviews.split(' ')
            stars = float(list_reviews[0])
            rating = int(list_reviews[-2])
        except (ValueError, AttributeError):
            stars = np.nan
            rating = np.nan

        # Get description
        raw_description = p_soup.find('div', {'data-test': 'item-details-description'})
        description = extract_text(raw_description)

        # Get highlights
        raw_highlights_list = p_soup.find_all('div', class_='lnzSpN')
        highlights_list = []
        for highlight in raw_highlights_list:
            highlights_list.append(extract_text(highlight))
        highlights = str(highlights_list)

        # Add it all to a dataframe
        df_product = pd.DataFrame(data={'name': [name],
                                        'price': [price],
                                        'alcohol': [alcohol],
                                        'region': [region],
                                        'quantity': [quantity],
                                        'weight': [weight],
                                        'country': [country],
                                        'upc': [upc],
                                        'stars': [stars],
                                        'rating': [rating],
                                        'url': [long_url],
                                        'description': [description],
                                        'highlights': [highlights]
                                        })
        # Print product name and current progress
        print(df_product.name)
        counter += 1
        progress = round(100*(counter/num_results), 2)
        print(f'Scraped {num_results} products ({progress}% complete)\n')

        # Add single-product dataframe to all-product dataframe
        df = df.append(df_product)

# Save dataframe to csv
df.reset_index(drop=True)
df.to_csv('crafty.csv', index=False)
