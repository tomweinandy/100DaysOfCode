"""
Day 20-21: Snake Game
"""
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakes on a Plane')

snake = []
x = 0

for i in range(3):
    new_turtle = turtle.Turtle(shape='square')
    new_turtle.color('white')
    new_turtle.goto(x, 0)
    x -= 20

    snake.append(new_turtle)



screen.exitonclick()

