"""
Day 22: Pong
"""
import turtle
import paddle
import ball
import scoreboard
import time

# Initialize screen
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
t.goto(0, -290)
instructions = 'Left moves with Esc/Tab. Right moves with Up/Down. First to 5 points wins. Press Backspace to begin.'
t.write(instructions, align='center', font=('Courier', 12, 'normal'))
t.goto(0, 1000)


# Use solution by Joseph to allow for both paddles to move at once
    # Details: https://www.udemy.com/course/100-days-of-code/learn/lecture/20414753#questions/13216834
def pressed(event):
    """
    Callback for KeyPress event listener. Sets key pressed state to True
    :param event: A key press
    """
    keys_pressed[event.keysym] = True


def released(event):
    """
    Callback for KeyPress event listener. Sets key pressed state to False
    :param event: A key press
    """
    keys_pressed[event.keysym] = False


# Set up the event listeners, bypassing the Turtle Screen to use the underlying TKinter canvas directly
# This needs to be done to get access to the event object so the state machine can determine which key was pressed
def set_key_binds():
    """
    Bind together key presses into single input
    """
    for key in ["Up", "Down", "Escape", "Tab", "BackSpace"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


# State machine to track which keys are pressed
keys_pressed = {}

# Begin listening
screen.listen()
set_key_binds()

game_on = True
while game_on:
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

        # Detect if a paddle misses
        if ball.xcor() > 350:
            scoreboard.point('left')
            ball.color('red')
            screen.update()

            # Check if 5 points reached
            if scoreboard.left_score == 5:
                scoreboard.win('left')
                ball.pause()
                game_on = False
            else:
                ball.reset()
                screen.update()
                time.sleep(1)

        if ball.xcor() < -350:
            scoreboard.point('right')
            ball.color('red')
            screen.update()

            # Check if 5 points reached
            if scoreboard.right_score == 5:
                scoreboard.win('right')
                ball.pause()
                game_on = False
            else:
                ball.reset()
                screen.update()
                time.sleep(1)

screen.update()
screen.exitonclick()
