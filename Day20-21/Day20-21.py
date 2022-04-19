"""
Day 20-21: Snake Game
"""
import turtle
import snake
import time

# Set initial conditions
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakes on a Plane')
screen.tracer(0)  # only updates on screen.update()

# My pet snake is named "snek"
snek = snake.Snake()

# Define constants
STARTING_X = 0
MOVING_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

screen.exitonclick()
