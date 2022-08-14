"""
Day 22: Pong
"""
import turtle
import paddle
import ball
import scoreboard
import build_level
import time

# Sets constants
PADDLE_YCOR = -340
CEILING_YCOR = 330
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350
PROX = 20   # proximity
SPINDEX = [14.0, 10.0, 6.0, 2.0, -2.0, -6.0, -10.0, -14.0]
# SPINDEX = [10, 10, 10, 10, -10, -10, -10, -10]


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

# Add screen elements
build_level.build_screen()
block_rows = build_level.build_level_one()

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
        # instructions.clear()

    screen.update()
    time.sleep(0.005 / ball.speed)
    ball.forward(5)



    # Detect if ball hits a block
    for row in block_rows:
        for block in row.blocks:
            x_diff = block.xcor() - ball.xcor()
            y_diff = block.ycor() - ball.ycor()

            # Detects if block is hit by the left of the ball

            # Detects if block is hit by the right of the ball

            # Detects if block is hit by the top of the ball

            # Detects if block is hit by the bottom of the ball
            X_PROX = 30
            Y_PROX = 20

            if abs(x_diff) < X_PROX and 0 < y_diff < Y_PROX:
                ball.bounce('top')
                print(f'Ball coordinates: {ball.position()}, Block coordinates: {block.position()}')
                print(block.popped_points())

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
