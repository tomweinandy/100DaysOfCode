"""
Day 19: Turtle Race
"""
import turtle
import random

# Docs: https://docs.python.org/3/library/turtle.html

# Set initial conditions
screen = turtle.Screen()
screen.setup(width=1000, height=500)

# Make a turtle for each color and save to a list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y = 200
turtle_list = []

for color in colors:
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-425, y)
    y -= 75
    turtle_list.append(new_turtle)

# Player guesses which turtle will win
bet = screen.textinput(title='Place your bets!',
                       prompt='Which color turtle do you think will win? (red/orange/yellow/green/blue/purple): '
                       ).lower()

# Begin the race
race_on = True
while race_on:
    for t in turtle_list:
        random_distance = random.randint(0, 10)
        t.forward(random_distance)

        # Stop after a turtle reaches the end
        if t.xcor() > 475:
            winner = t.color()[0]
            print(f'The {winner} turtle won!')
            race_on = False

# Check if the bet was correct
if bet == winner:
    print('You get all the monies!')
else:
    print('And this is why people don\'t bet on turtle races')

screen.exitonclick()
