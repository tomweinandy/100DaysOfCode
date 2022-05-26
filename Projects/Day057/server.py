"""
Day 57 Lessons
"""
from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

year = dt.datetime.now().year


@app.route('/')
def home():
    return render_template("lesson.html", year=year)


@app.route('/blog/<number>')
def blogger(number):
    response_blog = requests.get(url='https://api.npoint.io/445214455c1934eb12ff')
    all_posts = response_blog.json()

    num = int(number)

    return render_template("blog.html", year=year, posts=all_posts, num=num)


@app.route('/<name>')
def namer(name):
    response = requests.get(url=f'https://api.genderize.io/?name={name}')
    response_dict = response.json()
    gender = response_dict['gender']
    prob = response_dict['probability'] * 100

    response2 = requests.get(url=f'https://api.agify.io/?name={name}')
    response_dict2 = response2.json()
    age = response_dict2['age']

    return render_template("name_guesser.html", year=year, gender=gender, prob=prob, name=name, age=age)


if __name__ == "__main__":
    app.run(debug=True)
