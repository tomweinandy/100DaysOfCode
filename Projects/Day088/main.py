"""
Day 88: To-Do List Website
"""
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import requests
import json

# # Set secret key
# with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day64Creds.json') as file:
#     creds = json.loads(file.read())

# # Define URLs for The Movie Data Base
# MOVIE_DB_API_KEY = creds['KEY']
# MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
# MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
# MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silences warnings
db = SQLAlchemy(app)


# Create task table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    urgency = db.Column(db.Float, nullable=True)
    importance = db.Column(db.Float, nullable=True)
    tags = db.Column(db.String(250), nullable=True)
    status = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        task_dict = {'id': id,
                     'title': title,
                     'description': description,
                     'urgency': urgency,
                     'importance': importance,
                     'tags': tags,
                     'status': status}
        return task_dict


db.create_all()


# Create form for searching for tasks
class FindTaskForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired()])
    description = TextAreaField("Task Description", validators=[DataRequired()])
    urgency = StringField("Task Urgency", validators=[DataRequired()])
    importance = StringField("Task Importance", validators=[DataRequired()])
    tags = StringField("Task Tags", validators=[DataRequired()])
    status = StringField("Task Status", validators=[DataRequired()])
    submit = SubmitField("Add Task")


# Create form to rate movies
class TaskForm(FlaskForm):
    title = StringField("Task Name")
    description = TextAreaField("Task Description")
    urgency = StringField("Urgency from 1 (low) to 5 (high)")
    importance = StringField("Importance from 1 (low) to 5 (high)")
    tags = StringField("Task Tags, separated by a comma")
    status = StringField("'Waiting', 'Progressing', or 'Done'")
    submit = SubmitField("Done")


# Create homepage
@app.route("/")
def home():
    all_tasks = Task.query.order_by(Task.urgency).all()
    for i in range(len(all_tasks)):
        all_tasks[i].ranking = len(all_tasks) - i
    db.session.commit()
    return render_template("index.html", tasks=all_tasks)


# Create page for adding tasks
@app.route("/add", methods=["GET", "POST"])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task_title = form.title.data
        task_description = form.description.data
        task_urgency = form.urgency.data
        task_importance = form.importance.data
        task_tags = form.tags.data
        task_status = form.status.data

        # Package submission and add to database
        new_task = Task(title=task_title, description=task_description, urgency=task_urgency,
                        importance=task_importance, tags=task_tags, status=task_status)

        db.session.add(new_task)
        db.session.commit()

        # Clear form on submission
        return redirect(url_for('add_task'))

    return render_template("add.html", form=form)


# # Create page for searching for tasks
# @app.route("/find")
# def find_task():
#     task_api_id = request.args.get("id")
#     if task_api_id:
#         movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
#         response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
#         data = response.json()
#         new_movie = Movie(
#             title=data["title"],
#             year=data["release_date"].split("-")[0],
#             img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
#             description=data["overview"]
#         )
#         db.session.add(new_movie)
#         db.session.commit()
#         return redirect(url_for("rate_movie", id=new_movie.id))


# Create page for editing movies
@app.route("/edit", methods=["GET", "POST"])
def edit_task():
    task_id = request.args.get("id")
    print(task_id)
    task = Task.query.get(task_id)
    print('checkpoint')
    # edit_form = TaskForm(title=task.title,
    #                      )
    edit_form = TaskForm(
        title=task.title,
        description=task.description,
        urgency=task.urgency,
        importance=task.importance,
        tags=task.tags,
        status=task.status
    )

    if edit_form.validate_on_submit():
        task.title = edit_form.title.data
        task.description = edit_form.description.data
        task.urgency = edit_form.urgency.data
        task.importance = edit_form.importance.data
        task.tags = edit_form.tags.data
        task.status = edit_form.status.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", task=task, form=edit_form)

# # Create page for editing movies
# @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
# def show_task(task_id):
#     task = Task.query.get(task_id)
#     edit_form = TaskForm(
#         title=task.title,
#         description=task.description,
#         urgency=task.urgency,
#         importance=task.importance,
#         tags=task.tags,
#         status=task.status
#     )
#
#     if edit_form.validate_on_submit():
#         task.title = edit_form.title.data
#         task.description = edit_form.description.data
#         task.urgency = edit_form.urgency.data
#         task.importance = edit_form.importance.data
#         task.tags = edit_form.tags.data
#         task.status = edit_form.status.data
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template("edit.html", task=task, form=edit_form)


# Create path for deleting a movie
@app.route("/delete")
def delete_task():
    task_id = request.args.get("id")
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
