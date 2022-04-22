"""
Day 22: Pong
"""

import turtle
import paddle
import time

screen = turtle.Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)  # only updates on screen.update()

# Create two paddles
right_paddle = paddle.Paddle(350, 0)
left_paddle = paddle.Paddle(-350, 0)

# "Listens" for keystrokes
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")

# todo add instructions on bottom of screen
# todo start with the spacebar

game_on = True
while game_on:
    screen.update()
    # time.sleep(0.1)



screen.exitonclick()