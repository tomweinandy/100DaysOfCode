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

# Pick which style art to make
style = ''
while style not in ['hirst', 'pollock']:
    title = 'Many of the great Renaissance artists were turtles'
    prompt = 'Do you want a "Hirst" painting with dots or a "Pollock" painting with random lines?'
    style = screen.textinput(title=title, prompt=prompt).lower()

# Day 18 Project
if style == 'hirst':
    # Position the turtle
    turtle.colormode(255)
    t.penup()
    t.goto(-305, 305)
    t.pendown()

    # Set seed
    seed = random.randint(0, 1000)
    print('Seed:', seed)

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

# Bonus: Random Walk with extracted colors
if style == 'pollock':
    def random_walk(t, steps, step_length, color='random'):
        """
        Draws a line according to a random walk
        :param t: The turtle of interest
        :param steps: Number of steps in the walk
        :param step_length: The length of each step in the random walk
        :param color: Line color in (r,g,b) format from
        """
        # Begins at the origin
        t.penup()
        t.goto(0, 0)
        t.pendown()

        turtle.colormode(255)
        t.color(color)

        # Random walk
        for step in range(steps):
            t.right(random.randint(0, 360))
            t.forward(step_length)

    turtle.write('          This may take a minute...')
    turtle.tracer(0, 0)  # Comment out this line to watch the turtle draw

    # Take a million steps
    t.pensize(5)
    seed = random.randint(0, 1000)
    print('Seed:', seed)
    random.seed(seed)
    for i in range(0, 1000):
        color = random.choice(colorgram_list)
        random_walk(t, 1000, 50, color=color)
    turtle.update()

screen.exitonclick()
