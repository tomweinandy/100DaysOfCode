"""
Day 63: Book Review Site with SQLite and SQLAlchemy
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silences warnings
Bootstrap(app)

# ** Code commented out because code is supplanted by SQLAlchemy **
# # Create a database and cursor
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
#
# # Create table and add entry
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Hatchet', 'Gary Paulsen', '⭐⭐⭐⭐⭐')")


# Create new database
db = SQLAlchemy(app)


# Create books table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return {"id": self.id, "title": self.title, "author": self.author, "rating": self.rating}


db.create_all()

# # Create a new record
# # Alternatively, id is optional and will be auto-generated if excluded
# new_book = Book(id=1, title='Hatchet', author='Gary Paulsen', rating=10)
# db.session.add(new_book)
# db.session.commit()

# Read all records
all_books = db.session.query(Book).all()

# # Read a particular book
# book = Book.query.filter_by(title='Hatchet').first()

# # Update a particular record by query
# book_to_update = Book.query.filter_by(title='Hatchet').first()
# book_to_update.title = "Brian's Winter"
# db.session.commit()

# # Update a record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = 'The River'
# db.session.commit()

# # Delete a particular record by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.commit()


class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()])
    author = StringField('Book author', validators=[DataRequired()])
    rating = IntegerField('Book rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def add_to_db(self, title, author, rating):
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = BookForm()
    print(len(all_books))

    if form.validate_on_submit():
        form.add_to_db(form.title.data, form.author.data, form.rating.data)
        return redirect(url_for('home'))

    return render_template('add.html', form=form, all_books=all_books)


if __name__ == "__main__":
    app.run(debug=True)
