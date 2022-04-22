"""
Day 20-21: Snake Game
"""
import turtle
import snake
import time
import food
from scoreboard import Scoreboard

# Set initial conditions
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakes on a Plane')
screen.tracer(0)  # only updates on screen.update()

# My pet snake is named "snek"
snek = snake.Snake()
difficulty = snake.difficulty()
food = food.Food()
scoreboard = Scoreboard()

# "Listens" for keystrokes
screen.listen()
screen.onkey(snek.turn_up, "Up")
screen.onkey(snek.turn_down, "Down")
screen.onkey(snek.turn_left, "Left")
screen.onkey(snek.turn_right, "Right")

# Begin the game
game_on = True
while game_on:
    screen.update()
    time.sleep(difficulty)
    snek.move()

    # Detect collision with food

    if snek.segments[0].distance(food) <= 15:
        food.refresh()
        scoreboard.refresh()

screen.exitonclick()
