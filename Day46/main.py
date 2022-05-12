from bs4 import BeautifulSoup
import requests
import pandas as pd

# Save three web scrapes (since list is spread out over all three movies
response = requests.get('https://www.billboard.com/charts/hot-100/2000-08-12')
soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.find_all(name='h3', id='title-of-a-story')
songs = soup.select(selector='li h3')

#
song_list = []
for s in songs[0:100]:
    song = s.text
    song = song.replace('\n', '')
    song = song.replace('\t', '')
    song_list.append(song)