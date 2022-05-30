"""
Day 60: Responsive HTML forms

Note: Most of the project for this day was to improve the contact form from the Day 59 blog.

Example for HTML <form> method attribute: https://www.w3schools.com/tags/att_form_method.asp
Example for HTML <form> action attribute: https://www.w3schools.com/tags/att_form_action.asp
More on methods parameter: https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods
Catching inputs with Flask request object: https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
"""

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_date():
    un, pw, er = None, None, None

    try:
        un = request.form['username']
        pw = request.form['password']

    except:
        er = 'Invalid username/password'

    return render_template('login.html', username=un, password=pw, error=er)


if __name__ == '__main__':
    app.run(debug=True)
