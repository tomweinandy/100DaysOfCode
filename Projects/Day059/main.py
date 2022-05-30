"""
Day 59

Template: https://startbootstrap.com/previews/clean-blog/
Solution: https://repl.it/@appbrewery/day-59-end.zip
"""
from flask import Flask, render_template, request
import datetime as dt
import requests

# Add name of current directory
app = Flask(__name__)
print('Root path:', app.root_path)

year = dt.datetime.now().year


def send_email(name, email, phone, message):
    print('Send email', name, email, phone, message)


@app.route('/')
def home():
    response_blog = requests.get(url='https://api.npoint.io/dc5220ec8c05b895e7ee')
    all_posts = response_blog.json()

    return render_template('index.html', year=year, posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html', year=year)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        send_email(name, email, phone, message)

        return render_template('contact.html', year=year, message_sent=True)

    else:
        return render_template('contact.html', year=year, message_sent=False)


@app.route('/post/<number>')
def blogger(number):
    response_blog = requests.get(url='https://api.npoint.io/dc5220ec8c05b895e7ee')
    all_posts = response_blog.json()
    num = int(number)

    print('Showing page', num)

    return render_template("post.html", year=year, posts=all_posts, num=num)


@app.route('/form-entry', methods=['POST'])
def receive_date():

    name = request.name
    email = request.email
    phone = request.phone
    message = request.message

    return "<h1>Successfully sent your message</h1>"


if __name__ == '__main__':
    app.run(debug=True)
