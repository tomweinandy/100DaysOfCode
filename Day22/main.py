"""
Day 22: Pong
"""

import turtle
import paddle
import ball
import time

screen = turtle.Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)  # only updates on screen.update()


# Create two paddles
right_paddle = paddle.Paddle(350, 0)
left_paddle = paddle.Paddle(-350, 0)

print(left_paddle.position(), right_paddle.position())

# Create ball
ball = ball.Ball()

# "Listens" for keystrokes
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")

# todo add instructions on bottom of screen
# todo start with the spacebar
# todo limit paddle movement to stay on screen
# todo fix glitch of ball sticking to paddle


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect if the ball hits the ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(y=True)

    # Detect if the ball hits a paddle
    if ball.distance(right_paddle.position()) < 50 and ball.xcor() > 320:
        ball.bounce(x=True)
    if ball.distance(left_paddle.position()) < 50 and ball.xcor() < -320:
        ball.bounce(x=True)

    # Detect if a paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
    if ball.xcor() < -350:
        ball.reset_position()


ball.color('red')
screen.update()
screen.exitonclick()