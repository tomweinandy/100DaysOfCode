"""
Day 22: Pong
"""

import turtle
import paddle
import ball
import scoreboard
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

# Create ball and scoreboard
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

# Write instructions on screen
t = turtle.Turtle()
t.color('white')
t.penup()
t.goto(-300, -290)
instructions = 'Left player moves with A/Z. Right player moves with Up/Down. Press space bar to begin.'
t.write(instructions, font=('Courier', 12))
t.goto(0, 1000)

# "Listens" for keystrokes
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")

# todo start with the space bar
# todo limit paddle movement to stay on screen
# todo fix glitch of ball sticking to paddle
# todo have ball appear at random point in center
# todo Add game over at 10 points

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1 * ball.speed)
    ball.move()

    # Detect if the ball hits the ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(y=True)

    # Detect if the ball hits a paddle
    if ball.distance(right_paddle.position()) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle.position()) < 50 and ball.xcor() < -320:
        ball.bounce(x=True)
        ball.increase_speed()

    # Detect if a paddle misses
    if ball.xcor() > 350:
        scoreboard.point('left')
        ball.reset_position()
        ball.reset_speed()

    if ball.xcor() < -350:
        scoreboard.point('right')
        ball.reset_position()
        ball.reset_speed()

ball.color('red')
screen.update()
screen.exitonclick()