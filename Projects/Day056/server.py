"""
Day 56: HTML Name Card

Using the following template: https://html5up.net/twenty
"""
from flask import Flask, render_template

# Add name of current directory
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('lesson.html')


if __name__ == '__main__':
    app.run(debug=True)
