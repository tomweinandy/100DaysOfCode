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

# dashed_square(danklin, 10, 100)


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
    """
    * Moves turtle to the west corner of the northernmost side of a polygon.
    * There are two possible ways of reaching this point.
      The first way is to travel due north, turn left 90 degrees, and then travel due west.
      The second way is to turn directly to the corner and travel diagonally (northwest) to the same destination.
    * Image plotting those two paths together to form a right triangle.
      Then we can use known measurements to calculate the length of the hypotenuse.
    * We know the angle between the adjacent triangle side and the hypotenuse as 360 degrees / (2 * the # of sides).
      E.g., a square has 8 right triangles that pinwheel out in 360 degrees from the centroid (8 = 2 * 4 sides).
      Therefore, this inner angle for a square is 360/(2*4) = 45 degrees. I call this angle 'theta'.
    * We also know the length of the opposite side from theta as half the length of the polygon side.
    * Since sin(theta) = opposite / hypotenuse, we can solve for hypotenuse = (side length / 2) / sin(360/(2*sides)).
    * Now we turn theta degrees and move a distance equal to the hypotenuse to reach the northwest corner.
      From here we begin drawing the polygon so that the centroid aligns with the origin of our turtle.

    :param t: the Turtle() class object
    :param sides: number of sides in an equilateral polygon
    :param side_length: length of each polygon side
    :return:
    """
    # Define variables
    theta = 360/(2*sides)
    sine_theta = math.sin(math.radians(theta))  # math.sin() takes input as radians
    hypotenuse = (side_length/2) / sine_theta

    # Move turtle
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