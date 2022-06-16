"""
Day 63:
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silences warnings
Bootstrap(app)

# Create new database
db = SQLAlchemy(app)


# Create books table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# Add new entry
book1 = Book(id=1, title='Hatchet', author='Gary Paulsen', rating=10)
db.session.add(book1)
db.session.commit()


# ** Code commented out because code is supplanted by SQLAlchemy **
# # Create a database and cursor
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
#
# # Create table and add entry
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Hatchet', 'Gary Paulsen', '⭐⭐⭐⭐⭐')")

# all_books = [{'title': 'Hatchet', 'author': 'Gary Paulsen', 'rating': '⭐⭐⭐⭐⭐'}]


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

