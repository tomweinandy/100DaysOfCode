"""
Day 57: HTML Blog with Jinja and Flask
"""
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(url='https://api.npoint.io/445214455c1934eb12ff')
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)


@app.route('/<number>')
def blogger(number):
    response = requests.get(url='https://api.npoint.io/445214455c1934eb12ff')
    all_posts = response.json()

    for post in all_posts:
        if post['id'] == int(number):
            blog_post = post

    return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
