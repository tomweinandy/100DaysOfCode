"""
Day 92:
"""
import time

from bs4 import BeautifulSoup
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
    return txt


url = 'https://www.target.com/c/craft-beer-wine-liquor-grocery/-/N-o3thc'
url = 'https://www.target.com/c/craft-beer-wine-liquor-grocery/-/N-o3thc?Nao=0'

from playwright.sync_api import sync_playwright


def get_dynamic_soup(url: str) -> BeautifulSoup:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        time.sleep(5)
        soup = BeautifulSoup(page.content(), "html.parser")
        browser.close()
        return soup


soup = get_dynamic_soup(url)

# # Save web scrapes
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())





#
# # Scrape songs and add to a list
# scraped_songs = soup.select(selector='li h3')
#
# song_list = []
# for s in scraped_songs[0:100]:
#     song = extract_text(s)
#     song_list.append(song)
#
# # Scrape artists, taking into account first artist is in a different format
# scraped_first_artist = soup.find_all(
#     class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')
#
# scraped_other_artists = soup.find_all(
#     class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')
#
# # Create list and add the first artist to it
# artist_list = []
# first_artist = extract_text(scraped_first_artist[0])
# artist_list.append(first_artist)
#
# # Loop through other artists and add them to the list
# for a in scraped_other_artists:
#     artist = extract_text(a)
#     artist_list.append(artist)
#
# # Build dataframe of result
# df = pd.DataFrame()
# df['Rank'] = range(1, 101)
# df['Song'] = song_list
# df['Artist'] = artist_list
#
# # Optional: save results
# # df.to_csv(f'Top100_{input_date}.csv', index=False)
#
# # print(f'Here are on the top 100 songs for {input_date}:')
# # print(df)
#
#
