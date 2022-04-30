"""
Day 22: Pong
"""

import turtle
import paddle
import ball
import scoreboard
import time

# todo fix glitch of ball sticking to paddle
# todo have ball appear at random point in center
# todo Add game over at 10 points
# todo add random spin to ball

screen = turtle.Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)  # only updates on screen.update()

# Create two paddles
right_paddle = paddle.Paddle(350, 0)
left_paddle = paddle.Paddle(-350, 0)

# Create ball and scoreboard
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

# Write instructions on screen
t = turtle.Turtle()
t.color('white')
t.penup()
t.goto(-328, -290)
instructions = 'Left player moves with Esc/Tab. Right player moves with Up/Down. Press Space to pause/unpause.'
t.write(instructions, font=('Courier', 12, 'normal'))
t.goto(0, 1000)

######################### test
# State machine to track which keys are pressed
keys_pressed = {}


# Callback for KeyPress event listener. Sets key pressed state to True
def pressed(event):
    keys_pressed[event.keysym] = True


# Callback for KeyRelease event listener. Sets key pressed state to False
def released(event):
    keys_pressed[event.keysym] = False


# Set up the event listeners, bypassing the Turtle Screen to use the underlying TKinter canvas directly
# This needs to be done to get access to the event object so the state machine can determine which key was pressed
def set_key_binds():
    for key in ["Up", "Down", "Escape", "Tab", "BackSpace"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


# Begin listening
screen.listen()
set_key_binds()

game_on = True
while game_on:
    # Check state of keypresses and respond accordingly
    if keys_pressed["Escape"]: left_paddle.move_up()
    if keys_pressed["Tab"]: left_paddle.move_down()
    if keys_pressed["Up"]: right_paddle.move_up()
    if keys_pressed["Down"]: right_paddle.move_down()
    if keys_pressed["BackSpace"]: ball.pause()

    screen.update()
    time.sleep(0.1 * ball.speed)
    screen.listen()

    # Ball does not move when paused
    while not ball.paused:
        # Check state of keypresses and respond accordingly
        if keys_pressed["Escape"]:
            left_paddle.move_up()
        if keys_pressed["Tab"]:
            left_paddle.move_down()
        if keys_pressed["Up"]:
            right_paddle.move_up()
        if keys_pressed["Down"]:
            right_paddle.move_down()
        if keys_pressed["BackSpace"]:
            ball.pause()

        screen.update()
        time.sleep(0.1 * ball.speed)
        ball.move()

        # Detect if the ball hits the ceiling or floor
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce(y=True)

        # Detect if the ball hits a paddle (three conditions must be met for right paddle or left)
        if ball.distance(right_paddle.position()) < 60 and ball.xcor() > 320 and ball.x_direction == 1 or \
                ball.distance(left_paddle.position()) < 60 and ball.xcor() < -320 and ball.x_direction == -1:
            ball.bounce(x=True)
            ball.increase_speed()
    #
        # Detect if a paddle misses
        if ball.xcor() > 350:
            scoreboard.point('left')
            ball.color('red')
            screen.update()
            ball.reset()

        if ball.xcor() < -350:
            scoreboard.point('right')
            ball.color('red')
            screen.update()
            ball.reset()


ball.color('red')
screen.update()
screen.exitonclick()
