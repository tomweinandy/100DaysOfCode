from turtle import Turtle, Screen
import time
import random

# Docs: https://docs.python.org/3/library/turtle.html

# Initialize classes
danklin = Turtle()
screen = Screen()

# Configure our reptile
danklin.shape('turtle')
danklin.color('red')
danklin.pensize(2)


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

def ploygon(t, sides, distance, color='red'):
    t.color(color)
    for side in range(sides):
        t.forward(distance)
        t.right(360/sides)


color_list = ['red', 'orange', 'blue', 'black', 'brown', 'grey', 'yellow', 'pink', 'purple', 'green', 'light blue',
              'light green', 'gold', 'dark blue', 'coral', 'teal', 'magenta', 'cyan', 'lime green', 'indian red',
              'cornflower blue', 'slate gray', 'beige', 'peru', 'firebrick', 'dark orange', 'dark magenta',
              'steel blue', 'medium blue', 'medium purple', 'white smoke', 'light green', 'light pink', 'blue violet',
              'deep sky blue']
random.shuffle(color_list)

import math


# def center_polygon(t, sides, distance):
#
#     theta = 180/sides
#     hypotenuse = (distance/2) / math.sin(theta)
#     print(theta, hypotenuse)
#
#     t.penup()
#     t.right(90 - theta)
#     t.forward(hypotenuse)
#     t.left(90 - theta)
#     t.pendown()


# def reposition(t, north, west):
#     t.penup()
#     t.left(90)
#     t.forward(north)
#     t.left(90)
#     t.forward(west)
#     t.right(180)
#     t.pendown()

# distance = 200
# reposition(danklin, 150, distance/2)
# max_poly = 3
# center_polygon(danklin, max_poly, distance)
# for poly in range(3, max_poly + 1):
#     rando = color_list[poly-3]
#     ploygon(danklin, poly, distance, rando)



# # Goes through ALL the colors!
# reposition(danklin, 150, 50)
# for poly in range(3, len(color_list)+3):
#     rando = color_list[poly-3]
#     ploygon(danklin, poly, 25, rando)

# shimmy()

distance = 100
sides = 3
theta = 180/sides
hypotenuse = (distance/2) / math.sin(theta)

# danklin.right(90 + theta)
danklin.forward(hypotenuse)
# danklin.right(270 + theta)
# ploygon(danklin, sides, distance, 'blue')


screen.exitonclick()