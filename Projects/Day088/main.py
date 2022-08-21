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
    status = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        task_dict = {'id': id,
                     'title': title,
                     'description': description,
                     'urgency': urgency,
                     'importance': importance,
                     'status': status}
        return task_dict


db.create_all()


# Create form to add tasks
class TaskForm(FlaskForm):
    title = StringField("Task Name", validators=[DataRequired()])
    description = TextAreaField("Task Description", validators=[DataRequired()])
    urgency = StringField("Urgency: 1 (low) to 5 (high)", validators=[DataRequired()])
    importance = StringField("Importance: 1 (low) to 5 (high)", validators=[DataRequired()])
    status = StringField('Status: "to begin", "in progress", or "done"', validators=[DataRequired()])
    submit = SubmitField("Add Task")


# Create form to add tasks
class EditTaskForm(FlaskForm):
    title = StringField("Task Name", validators=[DataRequired()])
    description = TextAreaField("Task Description", validators=[DataRequired()])
    urgency = StringField("Urgency: 1 (low) to 5 (high)", validators=[DataRequired()])
    importance = StringField("Importance: 1 (low) to 5 (high)", validators=[DataRequired()])
    status = StringField('Status: "to begin", "in progress", or "done"', validators=[DataRequired()])
    submit = SubmitField("Update Task")


# Create homepage
@app.route("/")
def home():
    # Return non-completed tasks in descending order of combined urgency and importance
    all_tasks = Task.query.filter(Task.status != 'done' and Task.status != 'Done')\
        .order_by((Task.urgency + Task.importance).desc()).all()
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
        task_status = form.status.data

        # Package submission and add to database
        new_task = Task(title=task_title,
                        description=task_description,
                        urgency=task_urgency,
                        importance=task_importance,
                        status=task_status)

        db.session.add(new_task)
        db.session.commit()

        # Clear form on submission
        return redirect(url_for('add_task'))

    return render_template("add.html", form=form)


# Create page for editing movies
@app.route("/edit", methods=["GET", "POST"])
def edit_task():
    task_id = request.args.get("id")
    task = Task.query.get(task_id)
    edit_form = EditTaskForm(
        title=task.title,
        description=task.description,
        urgency=task.urgency,
        importance=task.importance,
        status=task.status
    )

    if edit_form.validate_on_submit():
        task.title = edit_form.title.data
        task.description = edit_form.description.data
        task.urgency = edit_form.urgency.data
        task.importance = edit_form.importance.data
        task.status = edit_form.status.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", task=task, form=edit_form)


# Create path for deleting a movie
@app.route("/delete")
def delete_task():
    task_id = request.args.get("id")
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/done')
def get_all():
    # completed_tasks = Task.query.all()
    completed_tasks = Task.query.filter(Task.status == 'done' or Task.status == 'Done').all()
    return render_template("done.html", completed_tasks=completed_tasks)


if __name__ == '__main__':
    app.run(debug=True)
