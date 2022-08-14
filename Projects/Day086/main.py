"""
Day 22: Pong
"""
import turtle
import paddle
import ball
import scoreboard
import blocks
import time

# Sets constants
PADDLE_YCOR = -340
CEILING_YCOR = 330
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350
PROX = 20   # proximity
SPINDEX = [14.0, 10.0, 6.0, 2.0, -2.0, -6.0, -10.0, -14.0]

# Initialize screen
screen = turtle.Screen()
screen.title('Breakout')
screen.setup(width=1000, height=1000)
screen.bgcolor('black')
screen.tracer(0)  # only updates on screen.update()

# Create ball, paddle and scoreboard
ball = ball.Ball()
game_paddle = paddle.Paddle(0, PADDLE_YCOR)
scoreboard = scoreboard.Scoreboard()

# todo move to separate file
# Write instructions on screen
instructions = turtle.Turtle()
instructions.color('white')
instructions.penup()
instructions.goto(0, TEXT_YCOR)
instructions_text = 'Press Backspace to begin.'
instructions.write(instructions_text, align='center', font=('Courier', 12, 'normal'))
instructions.goto(0, 1000)

# Write labels on screen
labels = turtle.Turtle()
labels.color('white')
labels.penup()
labels.goto(-450, TEXT_YCOR)
label_text = 'POINTS'
labels.write(label_text, align='center', font=('Courier', 18, 'normal'))
labels.goto(450, TEXT_YCOR)
label_text = 'LIVES'
labels.write(label_text, align='center', font=('Courier', 18, 'normal'))
labels.goto(0, 1000)

# Add horizontal bar for ceiling
bar = turtle.Turtle()
bar.goto(0, CEILING_YCOR)
bar.shape('square')
bar.color('white')
bar.turtlesize(stretch_len=50, stretch_wid=0.5)

# Add vertical bar for left wall
bar = turtle.Turtle()
bar.goto(LEFT_WALL_XCOR, 0)
bar.shape('square')
bar.color('white')
bar.turtlesize(stretch_len=0.5, stretch_wid=33)

# Add vertical bar for right wall
bar = turtle.Turtle()
bar.goto(RIGHT_WALL_XCOR, 0)
bar.shape('square')
bar.color('white')
bar.turtlesize(stretch_len=0.5, stretch_wid=33)

# todo move to separate file
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
    for key in ["Right", "Left", "BackSpace"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


# State machine to track which keys are pressed
keys_pressed = {}

# Begin listening
screen.listen()
set_key_binds()

screen.update()
time.sleep(2)

game_on = True
while game_on:
    # Check state of key presses and respond accordingly
    if keys_pressed["Right"]:
        game_paddle.move_right()
    if keys_pressed["Left"]:
        game_paddle.move_left()
    if keys_pressed["BackSpace"]:
        ball.pause()
        instructions.clear()

    screen.update()
    time.sleep(0.005 / ball.speed)
    ball.forward(5)

    # Detect if the ball hits the left wall
    if ball.xcor() < LEFT_WALL_XCOR + PROX:
        ball.bounce('left')

    # Detect if the ball hits the right wall
    if ball.xcor() > RIGHT_WALL_XCOR - PROX:
        ball.bounce('right')

    # Detect if the ball hits the ceiling
    if ball.ycor() > CEILING_YCOR - PROX:
        ball.bounce('top')
        ball.ceiling_hit = True

    # Detect if the ball hits the paddle
    for seg in game_paddle.segments:
        if ball.distance(seg.position()) < PROX and ball.ycor() < PADDLE_YCOR + PROX and 180 < ball.orientation < 360:
            # Spin ball according to the where it hits on the paddle
            segment_index = game_paddle.segments.index(seg)
            spin = SPINDEX[segment_index]
            ball.bounce('bottom', spin)
            ball.paddle_hits += 1

    # Detect if the ball misses the paddle
    if ball.ycor() < PADDLE_YCOR - 20:
        scoreboard.lives -= 1
        ball.color('red')
        screen.update()

        # Check if game over
        if scoreboard.lives < 0:
            scoreboard.game_over()
            game_on = False
        else:
            ball.reset()
            scoreboard.update_scoreboard()
            screen.update()
            time.sleep(2)

screen.update()
screen.exitonclick()
