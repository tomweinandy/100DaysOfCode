"""
Challenges from Day 55
"""

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold_wrapper():
        return f"<b>{function()}</b>"

    return bold_wrapper


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there, {name}!"


if __name__ == '__main__':
    app.run(debug=True)


# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f'You called: {function.__name__}')
        result = function(args[0], args[1], args[2])
        print(f'It returned: {result}')

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(1, 2, 3)
