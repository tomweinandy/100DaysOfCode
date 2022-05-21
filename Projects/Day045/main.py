"""
Day 45: Top 250 Movies Web Scraper

The movie list comes from LetterBoxd and is all-around better than the more popular counterpart of IMDB
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Save three web scrapes (since list is spread out over all three movies
response1 = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/')
soup1 = BeautifulSoup(response1.text, 'html.parser')

response2 = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/2/')
soup2 = BeautifulSoup(response2.text, 'html.parser')

response3 = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/3/')
soup3 = BeautifulSoup(response3.text, 'html.parser')

# Prep for loop
soups = [soup1, soup2, soup3]
rank_list = []
title_list = []

# Loop through each movie from each webpage
for soup in soups:
    movies = soup.find_all(class_='poster-container numbered-list-item')

    # Save rank, title for each movie to the repsective list
    for movie in movies:
        rank = int(movie.getText().replace(' ',''))
        rank_list.append(rank)

        title = movie.img['alt']
        title_list.append(title)

# Add results to dataframe and save as csv
df = pd.DataFrame()
df['Rank'] = rank_list
df['Title'] = title_list
df.to_csv('LetterBoxdTop250.csv', index=False)
