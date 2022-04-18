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
# danklin.speed(10)
turtle.tracer(0, 0)  # Comment out to watch the turtle draw



turtle.update()
shimmy(danklin)
screen.exitonclick()
