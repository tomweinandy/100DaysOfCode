"""
Day 68: User Authentication with Flask
"""
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Manage Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    # Every render_template has a logged_in variable set
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # Check if user already exists
        if User.query.filter_by(email=request.form.get('email')).first():
            flash('You have already signed up with that email. Please log in instead.')
            return redirect(url_for('login'))

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=generate_password_hash(request.form.get('password'))
        )
        db.session.add(new_user)
        db.session.commit()
        print(new_user.name)

        # Log in and authenticate user after info added to db
        login_user(new_user)

        return render_template("secrets.html", name=new_user.name)

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email
        user = User.query.filter_by(email=email).first()

        # Check if email exists
        if not user:
            flash('That email does not exist. Please try again.')
            return redirect(url_for('login'))

        # Check stored password hash against entered password hash
        elif not check_password_hash(user.password, password):
            flash('Password incorrect. Please try again')
            return redirect(url_for('login'))

        else:
            login_user(user)
            return render_template("secrets.html", name=user.name, logged_in=current_user.is_authenticated)

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
