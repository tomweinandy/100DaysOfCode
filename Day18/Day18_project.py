"""
Day 18: Turtle Drawings
"""
import turtle
import colorgram
import time
import random
import math

# Docs: https://docs.python.org/3/library/turtle.html

# Initialize classes
danklin = turtle.Turtle()
screen = turtle.Screen()

# Configure our reptile
danklin.shape('turtle')
danklin.color('red')
danklin.pensize(2)
danklin.speed(10)
# turtle.tracer(0, 0)  # Comment out to watch the turtle draw



# colorgram_list.reverse()

# Challenge 4: Random Walk with random RGB colors
def random_walk(t, steps, step_length, color):
    """
    Draws a line according to a random walk
    :param t: The turtle of interest
    :param steps: Number of steps in the walk
    :param step_length: The length of each step in the random walk
    :param color: Line color in (r,g,b) format. If 'random', will select random RBG values
    """
    turtle.colormode(255)
    t.color(color)

    # Random walk
    for step in range(steps):
        t.right(random.randint(0, 360))
        t.forward(step_length)

    # Return to origin
    t.penup()
    t.goto(0, 0)
    t.pendown()


# Take a million steps
danklin.pensize(5)
# seed = random.randint(0, 1000)  # seed = 6 was cool
# seed = 6
# print('Seed:', seed)
# random.seed(seed)

# for i in range(0, 100):
#     # color = random.choice(colorgram_list)
#     print(color)
#     random_walk(danklin, 100, 50, color)

colorgram_list = []
colors = colorgram.extract('kill_bill.jpeg', 8)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    colorgram_list.append(tup)

t = danklin

turtle.colormode(255)
t.penup()
t.goto(-305, 305)
t.pendown()

color = colorgram_list[0]

print(len(colorgram_list))

dots = 100
for i in range(dots):
    color = random.choice(colorgram_list)
    t.dot(50, color)

    t.penup()
    if (i+1) % 7 == 0:
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(600)
        t.right(180)
    else:
        t.forward(100)
    t.pendown()




turtle.update()
# shimmy(danklin)
screen.exitonclick()
