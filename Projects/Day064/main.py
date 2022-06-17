"""
Day 64: Top 10 Movie Website
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import requests

# Create database
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silences warnings
Bootstrap(app)
db = SQLAlchemy(app)


# Create movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String, nullable=True)

    def __repr__(self):
        movie_dict = {'id': id,
                      'title': title,
                      'year': year,
                      'description': description,
                      'rating': rating,
                      'ranking': ranking,
                      'review': review,
                      'img_url': img_url}
        return movie_dict


db.create_all()


# Create movie submission form
class MovieForm(FlaskForm):
    # id = IntegerField('ID')
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating')
    ranking = IntegerField('Ranking', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField()

    def add_to_db(self, title, year, description, ranking, review, img_url, rating=0):
        new_movie = Movie(title=title, year=year, description=description, ranking=ranking,
                          review=review, img_url=img_url, rating=rating)
        db.session.add(new_movie)
        db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        form.add_to_db(form.title.data, form.year.data, form.description.data, form.ranking.data,
                       form.review.data, form.img_url.data, form.rating.data)

        return redirect(url_for('home'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
