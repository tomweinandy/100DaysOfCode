from flask import Flask, render_template
import json
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Set secret key
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day61Creds.json') as file:
    creds = json.loads(file.read())
app.secret_key = creds['SECRET']


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = MyForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
