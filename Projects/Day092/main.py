"""
Day 92:
"""
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time
import requests
import pandas as pd


def extract_text(scrape: str):
    """
    Extract text out of scraped html using BeautifulSoup
    :param scrape: A string of the scraped html
    :return: The extracted text
    """
    txt = scrape.text
    txt = txt.replace('\n', '')
    txt = txt.replace('\t', '')
    txt = txt.strip()  # removes leading and trailing whitespaces
    return txt


def get_dynamic_soup(url: str) -> BeautifulSoup:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        time.sleep(5)   # gives time for page to render
        soup = BeautifulSoup(page.content(), "html.parser")
        browser.close()
        return soup


url = 'https://www.target.com/c/craft-beer-wine-liquor-grocery/-/N-o3thc'
url = 'https://www.target.com/c/craft-beer-wine-liquor-grocery/-/N-o3thc?Nao=0'

# Scrape html
soup = get_dynamic_soup(url)

# Extract the number of items from the search
raw_results = soup.find_all(class_='h-margin-b-tiny')[0]
results = extract_text(raw_results)
num_results = int(results.split()[0])

# Target only displays 24 products at a time, so page 2 begins with the 25th product (but includes "Nao=24" in url)
# Take number of results and make a list of 24-item intervals for each page (e.g., n=49 becomes [0, 24, 48])
n = (num_results - 1) // 24
page_intervals = [i*24 for i in range(n+1)]

# Find all product cards
product_wrapper_list = soup.find_all('div', {'data-test': '@web/site-top-of-funnel/ProductCardWrapper'})

n# Create empty dataframe
df = pd.DataFrame()

for product in product_wrapper_list:
    # Get image URLs
    product_url = product.select(selector='div div h3 a')[0]['href']
    product_url = product_url.split('#')[0]
    long_url = 'https://target.com' + product_url
    # product_list.append(long_url)

    # Scrape entire product page from long_url
    p_soup = get_dynamic_soup(long_url)

    # Get name
    raw_name = p_soup.find('h1')
    name = extract_text(raw_name)

    # Get price
    raw_price = p_soup.find('span', {'data-test': 'product-price'})
    price = extract_text(raw_price)

    # Get stars and ratings
    raw_reviews = p_soup.find('span', class_=lambda value: value and value.startswith('utils__ScreenReaderOnly'))
    string_reviews = extract_text(raw_reviews)
    list_reviews = string_reviews.split(' ')
    stars = float(list_reviews[0])
    rating = int(list_reviews[-2])

    # Add it all to a dataframe
    df_product = pd.DataFrame(data={'name': [name],
                                    'price': [price],
                                    'stars': [stars],
                                    'rating': [rating],
                                    'url': [long_url]
                                    })
    df_product






#
# # Optional: save results
# # df.to_csv(f'Top100_{input_date}.csv', index=False)
#
# # print(f'Here are on the top 100 songs for {input_date}:')
# # print(df)
#
#
