from flask import Flask, render_template
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from email_validator import validate_email, EmailNotValidError
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Set secret key
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day61Creds.json') as file:
    creds = json.loads(file.read())
app.secret_key = creds['SECRET']


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    too_short = 'Field must be at least 8 characters long.'
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = MyForm()
    form.validate_on_submit()

    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)

        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
