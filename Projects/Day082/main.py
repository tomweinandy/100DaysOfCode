"""
Day 82: Portfolio Website
"""
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from forms import CreatePostForm, RegisterForm, LoginForm, FlaskForm, CKEditorField, SubmitField, DataRequired
from flask_gravatar import Gravatar
from functools import wraps
import csv

# todo get contact form to work
# todo update final/project photo?
# todo remove unused files (esp. photos)
# todo update stats
# todo deploy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# Connect to the CSV with project details
with open('projects.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_dicts = []
    first_row = True
    for row in csv_data:
        if not first_row:
            project_dict = {'day': row[0],
                            'name': row[1],
                            'category': row[2],
                            'description': row[3]}
            list_of_dicts.append(project_dict)
        first_row = False
    # print(type(csv_file), type(csv_data), type(list_of_rows), type(row))
    # print(list_of_dicts)


# Display landing page
@app.route('/', methods=['GET', 'POST'])
def get_all_posts():
    return render_template("index.html")


# Display project page
@app.route("/day/<day_number>", methods=["GET", "POST"])
def show_day(day_number):
    print("day_number", type(day_number), day_number)
    for project in list_of_dicts:
        if project['day'] == str(day_number):
            selected_project = project
    print('Day:', selected_project)
    return render_template("portfolio-details.html", project=selected_project)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
