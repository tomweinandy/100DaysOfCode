"""
Day 45: Top 100 Movies Web Scraper
"""
from bs4 import BeautifulSoup
import requests

# Web searching
response1 = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/')
soup1 = BeautifulSoup(response1.text, 'html.parser')

response2 = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/2/')
soup2 = BeautifulSoup(response2.text, 'html.parser')

response3 = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/3/')
soup3 = BeautifulSoup(response3.text, 'html.parser')

soups = [soup1, soup2, soup3]

for soup in soups:
    movies = soup.find_all(class_='poster-container numbered-list-item')

    for movie in movies:
        rank = int(movie.getText().replace(' ',''))
        title = movie.img['alt']


