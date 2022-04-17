from turtle import Turtle, Screen
import time
import random
import math

# Docs: https://docs.python.org/3/library/turtle.html

# Initialize classes
danklin = Turtle()
screen = Screen()

# Configure our reptile
danklin.shape('turtle')
danklin.color('red')
danklin.pensize(2)
danklin.speed(10)


def shimmy():
    danklin.right(45)
    time.sleep(0.2)
    danklin.left(45)
    time.sleep(0.2)
    danklin.right(45)
    danklin.left(45)
    danklin.right(45)
    danklin.left(45)
    danklin.right(45)
    danklin.left(45)

# Challenge 1: Draw a square
def square(t, distance):
    t.forward(distance)
    t.right(90)
    t.forward(distance)
    t.right(90)
    t.forward(distance)
    t.right(90)
    t.forward(distance)

# square(danklin, 100)
# shimmy()

# Challenge 2: Draw a dashed line
def dash(t, interval, distance):
    full_loops = distance // (2*interval)
    remainder = distance % (2*interval)
    for loop in range(full_loops):
        t.forward(interval)
        t.penup()
        t.forward(interval)
        t.pendown()
    t.forward(remainder)

# dash(danklin, 10, 100)

def dashed_square(t, interval, distance):
    dash(t, interval, distance)
    t.right(90)
    dash(t, interval, distance)
    t.right(90)
    dash(t, interval, distance)
    t.right(90)
    dash(t, interval, distance)
#
# dashed_square(danklin, 10, 100)
# shimmy()


# Challenge 3: Drawing nested shapes

def ploygon(t, sides, side_length, color='red'):
    t.color(color)
    for side in range(sides):
        t.forward(side_length)
        t.right(360/sides)


color_list = ['red', 'orange', 'blue', 'black', 'brown', 'grey', 'yellow', 'pink', 'purple', 'green', 'light blue',
              'light green', 'gold', 'dark blue', 'coral', 'teal', 'magenta', 'cyan', 'lime green', 'indian red',
              'cornflower blue', 'slate gray', 'beige', 'peru', 'firebrick', 'dark orange', 'dark magenta',
              'steel blue', 'medium blue', 'medium purple', 'white smoke', 'light green', 'light pink', 'blue violet',
              'deep sky blue']
random.shuffle(color_list)

def center_polygon(t, sides, side_length):
    theta = 180/sides
    theta_radians = math.radians(theta)
    hypotenuse = (side_length/2) / math.sin(theta_radians)

    t.penup()
    t.left(90 + theta)
    t.forward(hypotenuse)
    t.right(90 + theta)
    t.pendown()

side_length = 200
max_sides = 10
center_polygon(danklin, max_sides, side_length)
for poly in range(3, max_sides + 1):
    color = color_list[poly - 3]
    ploygon(danklin, poly, side_length, color)


# Goes through ALL the colors!
# side_length = 50
# max_sides = len(color_list)
# center_polygon(danklin, max_sides, side_length)
# for poly in range(3, max_sides + 1):
#     color = color_list[poly - 3]
#     ploygon(danklin, poly, side_length, color)

shimmy()





screen.exitonclick()