"""
Day 63
"""
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
import pandas as pd
import numpy as np

#todo pare down these files into just book review site
#todo replace with Day063 directory

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []


class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()])
    author = StringField('Book author', validators=[DataRequired()])
    stars = ['⭐️', '⭐⭐️', '⭐⭐⭐️', '⭐⭐⭐⭐️', '⭐⭐⭐⭐⭐']
    rating = SelectField('Book rating', choices=stars, validators=[DataRequired()])
    submit = SubmitField('Submit')

    def add_to_dict(self, title, author, rating):
        print(title, author, rating)

        book_dict = {'title': title,
                     'author': author,
                     'rating': rating}

        all_books.append(book_dict)
        print(f'Added {book_dict}')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = BookForm()
    print('checkpoint 3')

    if form.validate_on_submit():
        form.add_to_dict(form.title.data, form.author.data, form.rating.data)
        return redirect(url_for('add'))

    print('All books:', all_books)
    return render_template('add.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
