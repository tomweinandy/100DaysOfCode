"""
Day 62: Coffee and Wifi Website
"""
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Café name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])

    coffee_choices = ['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️', '✘']
    wifi_choices = ['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪', '✘']
    power_choices = ['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌', '✘']

    coffee = SelectField('Coffee', choices=coffee_choices, validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=wifi_choices, validators=[DataRequired()])
    power = SelectField('Power', choices=power_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


def add_cafe_to_csv(cafe, location, open, close, coffee, wifi, power):
    df = pd.read_csv('cafe-data.csv')
    new_cafe = np.array([[cafe, location, open, close, coffee, wifi, power]])
    new_entry = pd.DataFrame(data=new_cafe, columns=df.columns)
    df = pd.concat([df, new_entry])
    df.to_csv('cafe-data.csv', index=False)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        add_cafe_to_csv(form.cafe.data, form.location.data, form.open.data,
                        form.close.data, form.coffee.data, form.wifi.data, form.power.data)
        return redirect(url_for('add_cafe'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
