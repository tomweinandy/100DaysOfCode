"""
Day 87: Café Website with REST API & SQLite Database

On day 66, we create an API that serves data on cafes with wifi and good coffee. Today, you're going to use the data from that project to build a fully-fledged website to display the information.
Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.
Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It should display the cafes, but it could also allow people to add new cafes or delete cafes.
For example, this startup in London has a website that does exactly this:
https://laptopfriendly.co/london

Resources:
* Day 62: cafe website
* Day 66: REST API
* Day 67: Blog with SQLite
"""
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL

import random


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


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random():
    random_cafe = random.choice(cafes)
    return jsonify(random_cafe.to_dict())


@app.route("/cafes", methods=['GET'])
def get_all():
    all_cafes = Cafe.query.all()
    return render_template("cafes.html", all_cafes=all_cafes)


@app.route("/search", methods=['GET'])
def search():
    location = request.args.get('loc')
    all_cafes_in_location = db.session.query(Cafe).filter_by(location=location).all()
    if all_cafes_in_location:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes_in_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add-cafe", methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        form.add_to_db(form.name.data, form.map_url.data, form.img_url.data, form.location.data, form.seats.data,
                       form.has_toilet.data, form.has_wifi.data, form.has_sockets.data, form.can_take_calls.data,
                       form.coffee_price.data)
        return redirect(url_for('add_another_cafe'))

    return render_template('add-cafe.html', form=form)


## HTTP POST - Create Record
@app.route("/add-another-cafe", methods=['GET', 'POST'])
def add_another_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        # today = date.today().strftime('%B %d, %Y')
        form.add_to_db(form.name.data, form.map_url.data, form.img_url.data, form.location.data, form.seats.data,
                       form.has_toilet.data, form.has_wifi.data, form.has_sockets.data, form.can_take_calls.data,
                       form.coffee_price.data)
        return redirect(url_for('add_another_cafe'))

    return render_template('add-another-cafe.html', form=form)


@app.route("/cafe/<int:cafe_id>")
def show_cafe(cafe_id):
    requested_cafe = Cafe.query.get(cafe_id)
    return render_template("cafe.html", cafe=requested_cafe)


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    # cafe.coffee_price = new_price
    # db.session.commit()
    #
    # new_price = request.args.get("new_price")
    # cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "NothingGoldCanStay":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
