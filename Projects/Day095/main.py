"""
Day 95: Google Trends Website

Improvement on the notebook using static data: https://github.com/tomweinandy/100DaysOfCode/tree/master/Projects/Day074
Google Trends API documentation: https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
Sample Code 1 (Daily Data): https://github.com/GeneralMills/pytrends/blob/master/pytrends/dailydata.py
Sample Code 2 (Exploration): https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
"""
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
import random
from pytrends.request import TrendReq
import json
import requests
import datetime as dt
import tweepy
from string import Template
import matplotlib.pyplot as plt
from markupsafe import Markup


# Checklist
#todo Update header file with navigation
#todo Update footer
#todo Remove cafe.db and all cafe mentions
#todo Remove unused files
#todo make links blue
#todo Clean up code and comment

# Initialize Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry; where key is column name and value is column value
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# Create search box
class Search(FlaskForm):
    topic = StringField("", validators=[DataRequired()])
    # submit_value = Markup('<span class_="navbar-brand">Submit</span>')
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
#todo change image
#todo add links to main page


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
    plt.plot(historical.index, historical.values, c='crimson', linewidth=2)
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

        timestamp = t['created_at']
        timestamp = timestamp.replace('+0000 ', '')

        twuple = (timestamp,
                  f"https://twitter.com/{t['user']['screen_name']}/status/{t['id_str']}",
                  t['user']['screen_name'],
                  t['user']['name'],
                  t['user']['location'],
                  t['text'])
        twuple_list.append(twuple)

    print(twuple_list)

    return render_template("topic.html", topic=trend_topic, related=related, news=top_articles, tweets=twuple_list, form=search_form)


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random():
    random_cafe = random.choice(cafes)
    return redirect(url_for("show_cafe", cafe_id=random_cafe.id))


# HTTP GET - Read all records
@app.route("/cafes", methods=['GET'])
def get_all():
    all_cafes = Cafe.query.all()
    return render_template("cafes.html", all_cafes=all_cafes)


# HTTP POST - Create Record
@app.route("/add-cafe", methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        form.add_to_db(form.name.data, form.map_url.data, form.img_url.data, form.location.data, form.seats.data,
                       form.coffee_price.data, form.has_toilet.data, form.has_wifi.data, form.has_sockets.data,
                       form.can_take_calls.data)
        return redirect(url_for('add_another_cafe'))

    return render_template('add-cafe.html', form=form)


# HTTP POST - Create Record
@app.route("/add-another-cafe", methods=['GET', 'POST'])
def add_another_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        form.add_to_db(form.name.data, form.map_url.data, form.img_url.data, form.location.data, form.seats.data,
                       form.coffee_price.data, form.has_toilet.data, form.has_wifi.data, form.has_sockets.data,
                       form.can_take_calls.data)
        return redirect(url_for('add_another_cafe'))

    return render_template('add-another-cafe.html', form=form)


# HTTP GET - Read Record
@app.route("/cafe/<int:cafe_id>")
def show_cafe(cafe_id):
    requested_cafe = Cafe.query.get(cafe_id)
    return render_template("cafe.html", cafe=requested_cafe)


# HTTP PUT/PATCH - Update Record
@app.route("/edit-cafe/<int:cafe_id>", methods=['GET', 'POST'])
def edit_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    edit_form = CafeForm(
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        seats=cafe.seats,
        coffee_price=cafe.coffee_price,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        has_sockets=cafe.has_sockets,
        can_take_calls=cafe.can_take_calls
    )
    if edit_form.validate_on_submit():
        cafe.name = edit_form.name.data
        cafe.map_url = edit_form.map_url.data
        cafe.img_url = edit_form.img_url.data
        cafe.location = edit_form.location.data
        cafe.seats = edit_form.seats.data
        cafe.coffee_price = edit_form.coffee_price.data
        cafe.has_toilet = edit_form.has_toilet.data
        cafe.has_wifi = edit_form.has_wifi.data
        cafe.has_sockets = edit_form.has_sockets.data
        cafe.can_take_calls = edit_form.can_take_calls.data
        db.session.commit()
        return redirect(url_for("show_cafe", cafe_id=cafe_id))
    return render_template("add-cafe.html", form=edit_form, is_edit=True)


# HTTP DELETE - Delete Record
@app.route("/delete-cafe/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('get_all'))


if __name__ == '__main__':
    app.run(debug=True)
