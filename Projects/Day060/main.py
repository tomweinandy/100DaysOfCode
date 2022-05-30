"""
Day 60: Build HTML Form
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

