"""
Day 95: Trending Topics Website

Built with APIs of Google searches, news articles and tweets
"""
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from pytrends.request import TrendReq
import json
import requests
import datetime as dt
import tweepy
import matplotlib.pyplot as plt

# Initialize Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


# Create search box
class Search(FlaskForm):
    topic = StringField("", validators=[DataRequired()])
    enter = SubmitField("Submit")


# Read in credential string and save as a dictionary
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day95Creds.json') as file:
    creds = json.loads(file.read())
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = creds['NEWS_API']

# API keys that yous saved earlier
api_key = creds['TWITTER_KEY']
api_secrets = creds['TWITTER_SECRET']
access_token = creds['ACCESS_TOKEN']
access_secret = creds['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Twitter authentication')
except:
    print('Failed Twitter authentication')


@app.route("/", methods=['GET', 'POST'])
def home():
    # Get trending searches
    pytrend = TrendReq()
    trending = pytrend.trending_searches()

    # Enable search in nav bar
    search_form = Search()
    if search_form.validate_on_submit():
        topic = search_form.topic.data
        return redirect(url_for("show_topic", trend_topic=topic))

    return render_template("index.html", trending=trending, form=search_form)


# HTTP GET - Read Record
@app.route("/topic/<trend_topic>", methods=['GET', 'POST'])
def show_topic(trend_topic):
    # Enable search in nav bar
    search_form = Search()
    if search_form.validate_on_submit():
        topic = search_form.topic.data
        return redirect(url_for("show_topic", trend_topic=topic))

    # Add back whitespaces removed for url
    trend_topic = trend_topic.replace('+', ' ')
    trend_topic = trend_topic.replace('%20', ' ')

    # Find trends
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[trend_topic])

    # Plot historical trends
    historical = pytrend.interest_over_time()[trend_topic]
    plt.figure(figsize=(5, 2.5), dpi=200)
    plt.title(f'Historical Popularity for "{trend_topic}"', fontsize=10)
    plt.yticks(fontsize=8)
    plt.xticks(fontsize=8)
    plt.ylabel('Search Index', fontsize=8)
    plt.plot(historical.index, historical.values, linewidth=2)
    plt.savefig('static/img/historical.jpg', bbox_inches='tight')

    # Plot interest by region
    regions = pytrend.interest_by_region()
    regions = regions.sort_values(by=trend_topic, ascending=False)
    regions = regions[0:10]
    plt.figure(figsize=(5, 2.5), dpi=200)
    plt.xticks(fontsize=8, rotation=30)
    plt.yticks(fontsize=8)
    plt.title(f'Interest by Region for "{trend_topic}"', fontsize=10)
    plt.ylabel('Search Index', fontsize=8)
    plt.bar(regions.index, regions[trend_topic])
    plt.savefig('static/img/regions.jpg', bbox_inches='tight')

    # Related queries
    related = pytrend.related_queries()
    related = related[trend_topic]['top']
    print(type(related))

    # Fetch top three articles that mention the query
    today = dt.datetime.today().strftime('%Y-%m-%d')
    news_url = f'{NEWS_ENDPOINT}?q={trend_topic.lower()}&from={today}&sortBy=publishedAt&apiKey={NEWS_KEY}&language=en'
    response = requests.get(news_url)

    # Print status, return data
    print('News response status code:', response.status_code)
    response.raise_for_status()
    news_data = response.json()
    news = news_data['articles']

    # Save select info from top five articles
    top_articles = []
    if len(news) > 5:
        for i in range(0, 5):
            article_tuple = (news[i]['title'], news[i]['url'], news[i]['description'])
            top_articles.append(article_tuple)
    # If not more than five articles, return how ever many there are
    else:
        for i in range(0, len(news)):
            article_tuple = (news[i]['title'], news[i]['url'], news[i]['description'])
            top_articles.append(article_tuple)

    # Get tweets
    max_tweets = 20
    searched_tweets = [status for status in tweepy.Cursor(api.search_tweets, q=trend_topic).items(max_tweets)]
    twuple_list = []
    for i in range(len(searched_tweets)):
        t = searched_tweets[i]._json

        # Remove extra characters from timestamp
        timestamp = t['created_at']
        timestamp = timestamp.replace('+0000 ', '')

        # Add select tweet elements to a tuple
        twuple = (timestamp,
                  f"https://twitter.com/{t['user']['screen_name']}/status/{t['id_str']}",
                  t['user']['screen_name'],
                  t['user']['name'],
                  t['user']['location'],
                  t['text'])
        twuple_list.append(twuple)

    return render_template("topic.html", topic=trend_topic, related=related, news=top_articles, tweets=twuple_list, form=search_form)


if __name__ == '__main__':
    app.run(debug=True)
