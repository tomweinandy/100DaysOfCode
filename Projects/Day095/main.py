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


# Checklist
# Review OG Google Trends website
#       Recreate this: https://trends.google.com/trends/explore?q=%2Fm%2F02y17j,%2Fm%2F09gms,%2Fm%2F012y1_&date=all
#todo Complete landing page using Google Trends API
#todo Figure out how to add plot to landing page
#todo Complete second webpage using news API
#todo Complete third webpage using Twitter API
#todo Complete fourth webpage with API integration (optional)
#todo Update header file with navigation
#todo Update footer
#todo Remove cafe.db and all cafe mentions
#todo Remove unused files
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

#


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


# WTForm
class Search(FlaskForm):
    topic = StringField("Topic", validators=[DataRequired()])
    enter = SubmitField("Search")


# WTForm
class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Cafe Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField("Cafe Address", validators=[DataRequired()])
    seats = StringField("Approximate Cafe Seats", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    has_toilet = BooleanField("Cafe Has a Toilet")
    has_wifi = BooleanField("Cafe Has Wifi")
    has_sockets = BooleanField("Cafe Has Sockets")
    can_take_calls = BooleanField("Can Take Calls in the Cafe")
    submit = SubmitField("Submit Submission")

    @staticmethod
    def add_to_db(name, map_url, img_url, location, seats, coffee_price, has_toilet, has_wifi, has_sockets,
                  can_take_calls):
        new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, seats=seats,
                        has_toilet=has_toilet, has_wifi=has_wifi, has_sockets=has_sockets,
                        can_take_calls=can_take_calls, coffee_price=coffee_price)
        db.session.add(new_cafe)
        db.session.commit()


# Query all cafés
cafes = db.session.query(Cafe).all()


@app.route("/", methods=['GET', 'POST'])
def home():
    pytrend = TrendReq()
    trending = pytrend.trending_searches()

    search_form = Search()

    print('Checkpoint 2')

    if search_form.validate_on_submit():
        print('Checkpoint 3')
        topic = search_form.topic.data
        print(topic)
        all_cafes = Cafe.query.all()
        # return redirect(url_for("show_test"))
        # return render_template('topic.html', topic=topic)
        return redirect(url_for("show_topic", trend_topic=topic))

    return render_template("index.html", trending=trending, form=search_form)
#todo change image


# HTTP GET - Read Record
@app.route("/topic/<trend_topic>")
def show_topic(trend_topic):
    # Find trends
    print('1', trend_topic)
    trend_topic = trend_topic.replace('+', ' ')
    print('2', trend_topic)
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[trend_topic])

    # Plot historical trends
    historical = pytrend.interest_over_time()[trend_topic]
    plt.figure(figsize=(5, 2.5), dpi=200)
    plt.title(f'Historical Popularity for {trend_topic}', fontsize=12)
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
    plt.title(f'Interest by Region for {trend_topic}', fontsize=12)
    plt.ylabel('Search Index', fontsize=8)
    plt.bar(regions.index, regions[trend_topic])
    plt.savefig('static/img/regions.jpg', bbox_inches='tight')

    # Related queries
    related = pytrend.related_queries()
    related = related[trend_topic]['top']
    print(type(related))


    return render_template("topic.html", topic=trend_topic, related=related)


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
