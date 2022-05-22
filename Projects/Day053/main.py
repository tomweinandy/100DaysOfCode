"""
Day 53: Zillow Data Entry Job Automation
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

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
response = requests.get(url_zillow)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

# todo create a list of links
# todo create a list of prices
# todo create a list of addresses
# todo fill out form
url_form = 'https://forms.gle/X7JE2Je17GqGKfyd6'
# todo go to Google Sheet
