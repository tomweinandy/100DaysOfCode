"""
Day 45 Sample Code
"""
from bs4 import BeautifulSoup
import requests

# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # Print things
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # Search with find_all()
# all_anchor_tags = soup.find_all(name='a')
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
#
# # Search with find()
# heading = soup.find(name='h1', id='name')
# # print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# # print(section_heading.getText())
#
# company_url = soup.select_one(selector='p a')  # returns all a's within p's
# # print(company_url)
#
# # Search with select()
# headings = soup.select('.heading')
# print(headings)

# Web searching
response = requests.get('http://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

title_links = soup.find_all(name='a', class_='titlelink')

for tag in title_links:
    article_text = tag.text
    article_link = tag.get('href')

    # Get up-votes
    score = soup.find(name='span', class_='score')
    article_upvote = int(score.text.split(' ')[0])
    print(article_text, '\n', article_link, '\n', article_upvote)

    break

