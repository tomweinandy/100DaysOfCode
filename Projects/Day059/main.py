"""
Day 59: HTML Blog with Jinja and Flask

Template: https://startbootstrap.com/previews/clean-blog/
Solution: https://repl.it/@appbrewery/day-59-end.zip
"""
import json
import smtplib
from flask import Flask, render_template, request
import datetime as dt
import requests

# Add name of current directory
app = Flask(__name__)
print('Root path:', app.root_path)

year = dt.datetime.now().year


def send_email(name, email, phone, message):
    # Load credentials
    with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day59Creds.json') as file:
        creds = json.loads(file.read())

    DEV_EMAIL = creds['EMAIL']
    DEV_PASSWORD = creds['PASSWORD']
    TOM_EMAIL = creds['TOM_EMAIL']

    # Set up SMTP connection
    # Gmail is smtp.gmail.com, Hotmail is smtp.live.com, Yahoo is smtp.mail.yahoo.com
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Start Transfer Layer Security encryption
        connection.starttls()
        connection.login(user=DEV_EMAIL, password=DEV_PASSWORD)
        connection.sendmail(from_addr=DEV_EMAIL,
                            to_addrs=TOM_EMAIL,
                            msg=f'Subject: New Contact Form Message\n\n'
                                f'Name: {name}\n'
                                f'Email: {email}\n'
                                f'Phone: {phone}\n'
                                f'Message: {message}\n')

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
