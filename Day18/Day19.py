"""
Day 19: Turtle Race
"""
import turtle

# Docs: https://docs.python.org/3/library/turtle.html


t = turtle.Turtle()
t.shape('turtle')
screen = turtle.Screen()


# Challenge 1: Make an Etch-A-Sketch
# Define action functions
def move_forward():
    t.forward(10)


def move_backward():
    t.forward(-10)


def turn_right():
    t.right(10)


def turn_left():
    t.left(10)


def clear_screen():
    t.clear()


# "Listens" for keystrokes
screen.listen()

# Links keystrokes to functions
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)










screen.exitonclick()

