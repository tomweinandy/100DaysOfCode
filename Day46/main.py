from bs4 import BeautifulSoup
import requests
import pandas as pd

#%%
def extract_text(scrape: str):
    txt = scrape.text
    txt = txt.replace('\n', '')
    txt = txt.replace('\t', '')
    return txt

# Save three web scrapes (since list is spread out over all three movies
response = requests.get('https://www.billboard.com/charts/hot-100/2000-08-12')
soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.select(selector='li h3')

#
song_list = []
for s in songs[0:100]:
    song = extract_text(s)
    song_list.append(song)


# Loop through each movie from each webpage
scrape_first_artist = soup.find_all(class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')

scrape_other_artists = soup.find_all(class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')



artist_list = []

first_artist = extract_text(scrape_first_artist[0])
artist_list.append(first_artist)

for a in scrape_other_artists:
    artist = extract_text(a)
    artist_list.append(artist)