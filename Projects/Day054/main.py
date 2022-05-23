"""
Day 54: Intro to Web Development with Flask

Quickstart documentation: https://flask.palletsprojects.com/en/2.1.x/quickstart/
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Goodbye, World"


if __name__ == '__main__':
    app.run()
