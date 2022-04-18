"""
Day 18: Turtle Drawings
"""
import turtle
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
turtle.tracer(0, 0)  # Comment out to watch the turtle draw

def shimmy(t):
    """
    Makes the turtle do a shimmy and a shake
    :param t: The turtle of interest
    """
    # The shimmy
    t.right(45)
    time.sleep(0.2)
    t.left(45)
    time.sleep(0.2)

    # The shake
    t.right(45)
    t.left(45)
    t.right(45)
    t.left(45)
    t.right(45)
    t.left(45)


# Challenge 1: Draw a square
def square(t, distance):
    """
    Draws an equilateral square
    :param t: The turtle of interest
    :param distance: Side length of the square
    :return:
    """
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
    """
    Draws a dashed line
    :param t: The turtle of interest
    :param interval: Length of the dash and space between each dash
    :param distance: Line length
    """
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
    """
    An equilateral square, but dashed
    :param t: The turtle of interest
    :param interval: Length of the dash and space between each dash
    :param distance: Length of each side
    """
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
    """
    Draws an equilateral polygon
    :param t: The turtle of interest
    :param sides: Number of sides in the polygon
    :param side_length: Side length
    :param color: Named color
    """
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


# Draws 8 polygons
# side_length = 200
# max_sides = 10
# center_polygon(danklin, max_sides, side_length)
# for poly in range(3, max_sides + 1):
#     color = color_list[poly - 3]
#     ploygon(danklin, poly, side_length, color)

# Goes through ALL the colors!
# side_length = 50
# max_sides = len(color_list)
# center_polygon(danklin, max_sides, side_length)
# for poly in range(3, max_sides + 1):
#     color = color_list[poly - 3]
#     ploygon(danklin, poly, side_length, color)


# Challenge 4: Random Walk with random RGB colors
def random_walk(t, steps, step_length, color='random'):
    """
    Draws a line according to a random walk
    :param t: The turtle of interest
    :param steps: Number of steps in the walk
    :param step_length: The length of each step in the random walk
    :param color: Line color in (r,g,b) format. If 'random', will select random RBG values
    """
    if color == 'random':
        turtle.colormode(255)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        t.color(r, g, b)
    else:
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
# danklin.pensize(5)
# seed = random.randint(0, 1000)  # seed = 6 was cool
# seed = 6
# print('Seed:', seed)
# random.seed(seed)
# for i in range(0, 1000):
#     random_walk(danklin, 1000, 50, color='random')

danklin.color('black')


# Challenge 5: Spirograph

# Set initial conditions
def spiral(t, loops, circle_size, distance_from_origin, rgb='b'):
    """
    Makes a spiral shape using disjoint, overlapping circles
    :param t: The turtle of interest
    :param loops: Number of equi-distant circles
    :param circle_size: Circle size
    :param distance_from_origin: Distance from origin to the circle base
    :param rgb: Shows a spectrum of color (supports 'r', 'g', and 'b')
    """
    turtle.colormode(255)

    spectrum = []
    half_loop = math.ceil(loops/2)
    for i in range(255, -255, -round(255/half_loop)):
        spectrum.append(abs(i))

    # Changes the color for each loop
    spectrum = spectrum[0:loops]
    for i in range(loops):
        # Define r, b, or g
        r, b, g = 0, 0, 0
        if rgb == 'r':
            r = spectrum[i]
        elif rgb == 'g':
            g = spectrum[i]
        else:
            b = spectrum[i]
        t.color((r, g, b))

        # Move from origin
        t.penup()
        t.forward(distance_from_origin)
        t.pendown()

        # Draw circle
        t.circle(circle_size)
        t.right(360/loops)

        # Return to origin
        t.penup()
        t.goto(0, 0)
        t.pendown()


# Draws three spiral circles, one of each color
# spiral(danklin, 50, 200, 195, 'r')
# spiral(danklin, 50, 200, 200, 'g')
# spiral(danklin, 50, 200, 205, 'b')


turtle.update()
shimmy(danklin)
screen.exitonclick()
