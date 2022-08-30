"""
Day 91: Website to

One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.
https://flatuicolors.com/palette/defo
It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and use it in my CSS or any design software.
On day 76, you learnt about image processing with NumPy. Using this knowledge and your developer skills (that means Googling), build a website where a user can upload an image and you will tell them what are the top 10 most common colours in that image.
This is a good example of this functionality:
http://www.coolphptools.com/color_extract#demo
"""
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
# from werkzeug import secure_filename
import csv
import pandas as pd
import numpy as np
import colorgram


# todo add photo upload

# Convert rbg colors to hex
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


# Extract colors from the jpg
def extract_colors(img, num):
    color_list = []
    num = int(num)
    colors = colorgram.extract(img, num)

    # Convert colors to a list of RGB values
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        hex = rgb_to_hex((r, g, b))
        proportion = round(color.proportion, 3)
        color_tuple = ((r, g, b), hex, proportion)
        color_list.append(color_tuple)

    return color_list


akira_colors = extract_colors('static/img/akira.jpg', 13)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class PhotoForm(FlaskForm):
    cafe = StringField('Café name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])

    # coffee = SelectField('Coffee', choices=coffee_choices, validators=[DataRequired()])
    # wifi = SelectField('Wifi', choices=wifi_choices, validators=[DataRequired()])
    # power = SelectField('Power', choices=power_choices, validators=[DataRequired()])
    submit = SubmitField('Run')


# def add_cafe_to_csv(cafe, location, open, close, coffee, wifi, power):
#     df = pd.read_csv('cafe-data.csv')
#     new_cafe = np.array([[cafe, location, open, close, coffee, wifi, power]])
#     new_entry = pd.DataFrame(data=new_cafe, columns=df.columns)
#     df = pd.concat([df, new_entry])
#     df.to_csv('cafe-data.csv', index=False)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html", color_list=akira_colors)


# @app.route('/add', methods=['POST', 'GET'])
# def add_cafe():
#     form = CafeForm()
#     if form.validate_on_submit():
#         add_cafe_to_csv(form.cafe.data, form.location.data, form.open.data,
#                         form.close.data, form.coffee.data, form.wifi.data, form.power.data)
#         return redirect(url_for('add_cafe'))
#     return render_template('add.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['imgFile']
        n = request.form.get('num_results')
        c = extract_colors(f, n)
        print(len(c), c)
        return render_template("index.html", color_list=c)

# @app.route('/color_extract', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['imgFile']
#         n = request.form.get('num_results')
#         c = extract_colors(f, n)
#         print(len(c), c)
#         return 'file uploaded successfully'


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
