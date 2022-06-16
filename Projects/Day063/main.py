"""
Day 63:
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

db = sqlite3.connect('books-collection.db')

# all_books = []
all_books = [{'title': 'Hatchet', 'author': 'Gary Paulsen', 'rating': '⭐⭐⭐⭐⭐'}]


class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()])
    author = StringField('Book author', validators=[DataRequired()])
    stars = ['⭐️', '⭐⭐️', '⭐⭐⭐️', '⭐⭐⭐⭐️', '⭐⭐⭐⭐⭐']
    rating = SelectField('Book rating', choices=stars, validators=[DataRequired()])
    submit = SubmitField('Submit')

    def add_to_dict(self, title, author, rating):
        book_dict = {'title': title,
                     'author': author,
                     'rating': rating}

        all_books.append(book_dict)
        print(all_books)


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = BookForm()
    print(len(all_books))

    if form.validate_on_submit():
        form.add_to_dict(form.title.data, form.author.data, form.rating.data)
        return redirect(url_for('add'))

    return render_template('add.html', form=form, all_books=all_books)


if __name__ == "__main__":
    app.run(debug=True)

