"""
Day 18: Turtle Drawings
"""
import turtle
import colorgram
import random

# Docs: https://docs.python.org/3/library/turtle.html

# Initialize classes
t = turtle.Turtle()
screen = turtle.Screen()

# Configure our reptile
t.shape('turtle')
t.color('red')
t.pensize(2)
t.speed(10)


# Extract colors from the jpg
colorgram_list = []
colors = colorgram.extract('kill_bill.jpeg', 8)

# Convert colors to a list of RGB values
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    colorgram_list.append(tup)

# Position the turtle
turtle.colormode(255)
t.penup()
t.goto(-305, 305)
t.pendown()

# Set dots for a 7x7 grid
dots = 49
for i in range(dots):
    # Make a dot
    color = random.choice(colorgram_list)
    t.dot(50, color)

    # Move the turtle
    t.penup()
    # Move to the next line after every 7th dot is placed
    if (i+1) % 7 == 0:
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(600)
        t.right(180)
    else:
        t.forward(100)
    t.pendown()

screen.exitonclick()
