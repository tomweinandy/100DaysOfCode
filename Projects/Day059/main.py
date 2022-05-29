"""
Day 59

Template: https://startbootstrap.com/previews/clean-blog/
"""
from flask import Flask, render_template
import datetime as dt
import requests

# Add name of current directory
app = Flask(__name__)
print('Root path:', app.root_path)

year = dt.datetime.now().year


@app.route('/')
def home():
    response_blog = requests.get(url='https://api.npoint.io/dc5220ec8c05b895e7ee')
    all_posts = response_blog.json()

    return render_template('index.html', year=year, posts=all_posts)


@app.route('/blog/<number>')
def blogger(number):
    response_blog = requests.get(url='https://www.npoint.io/docs/dc5220ec8c05b895e7ee')
    all_posts = response_blog.json()
    num = int(number)

    return render_template("blog.html", year=year, posts=all_posts, num=num)


if __name__ == '__main__':
    app.run(debug=True)
