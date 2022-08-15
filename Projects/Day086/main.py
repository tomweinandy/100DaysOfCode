"""
Day 86: Breakout

https://en.wikipedia.org/wiki/Breakout_(video_game)
"""
import turtle
import paddle
import ball
import scoreboard
import build_level
import time
import math

# Sets constants
BALL_START_ORIENTATION = 135
BALL_START_CORS = (0, -300)
PADDLE_YCOR = -340
CEILING_YCOR = 330
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350
PROX = 20   # proximity


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


def block_hit(side):
    game_ball.bounce(side)
    print(f'[{side.upper()}] X Distance: {x_distance}, Y Distance: {y_distance}')
    # print(f'[{side.upper()}] Ball coordinates: {ball.position()}, Block coordinates: {block.position()}')
    add_points = block.popped_points()
    scoreboard.points += add_points
    scoreboard.update_scoreboard()

    if add_points == 5:
        game_ball.speed_event('orange block')

    # Check if game was won
    # if scoreboard.points == 512:
        scoreboard.game_won()
        for i in range(40, 3600, 10):
            bonus_ball = ball.Ball((0, 0), i)
            for j in range(40):
                screen.update()
                bonus_ball.forward(2 + 0.004*i)
        scoreboard.lives += 999


# Initialize screen
screen = turtle.Screen()
screen.title('Breakout')
screen.setup(width=1000, height=1000)
screen.bgcolor('black')
screen.tracer(0)  # only updates on screen.update()

# Create ball, paddle and scoreboard
game_ball = ball.Ball(BALL_START_CORS, BALL_START_ORIENTATION)
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
    if keys_pressed["BackSpace"]: #todo remove
        ball.pause()

    screen.update()
    time.sleep(0.01 / game_ball.speed)
    game_ball.forward(5)

    # Detect if ball hits a block
    for row in block_rows:
        for block in row.blocks:
            x_distance = abs(block.xcor() - game_ball.xcor())
            y_distance = abs(block.ycor() - game_ball.ycor())
            block_below_ball = block.ycor() < game_ball.ycor()
            block_left_of_ball = block.xcor() < game_ball.xcor()

            # Detects if block is hit by the left of the ball
            if x_distance < 45 and y_distance < 15 and block_left_of_ball:
                block_hit('left')

            # Detects if block is hit by the right of the ball
            if x_distance < 45 and y_distance < 15 and not block_left_of_ball:
                block_hit('right')

            # Detects if block is hit by the bottom of the ball
            if x_distance < 30 and y_distance < 20 and block_below_ball:
                block_hit('bottom')

            # Detects if block is hit by the top of the ball
            if x_distance < 30 and y_distance < 20 and not block_below_ball:
                block_hit('top')

    # Detect if the ball hits the left wall
    if game_ball.xcor() < LEFT_WALL_XCOR + PROX:
        game_ball.bounce('left')

    # Detect if the ball hits the right wall
    if game_ball.xcor() > RIGHT_WALL_XCOR - PROX:
        game_ball.bounce('right')

    # If ball goes past a wall (for debugging)
    if game_ball.xcor() > RIGHT_WALL_XCOR or game_ball.xcor() < LEFT_WALL_XCOR or game_ball.ycor() > CEILING_YCOR:
        print(f'Paddle Bounce Angle: {game_ball.paddle_bounce_angle}, Orientation: {game_ball.orientation}')
        game_ball.orientation += 180

    # Detect if the ball hits the ceiling
    if game_ball.ycor() > CEILING_YCOR - PROX:
        game_ball.bounce('top')
        if not game_ball.ceiling_hit:
            print('HIT CEILING: Shorten the paddle')
            game_paddle.paddle_cors = game_paddle.paddle_cors_short
            game_paddle.spindex = game_paddle.spindex_short
            game_paddle.last_x_cor = game_paddle.segments[0].xcor()
            game_paddle.banish()
            game_paddle.create_paddle()
            game_ball.ceiling_hit = True

    # Detect if the ball hits the paddle
    for seg in game_paddle.segments:
        if game_ball.distance(seg.position()) < PROX and game_ball.ycor() < PADDLE_YCOR + PROX and 180 < game_ball.orientation < 360: #todo fix
            # Spin ball according to the where it hits on the paddle
            segment_index = game_paddle.segments.index(seg)
            spin = game_paddle.spindex[segment_index]
            game_ball.bounce('bottom', spin)

            game_ball.paddle_hits += 1
            if game_ball.paddle_hits == 4:
                game_ball.speed_event('four hits')
            if game_ball.paddle_hits == 12:
                game_ball.speed_event('twelve hits')

    # Detect if the ball misses the paddle
    if game_ball.ycor() < PADDLE_YCOR - 20:
        scoreboard.lives -= 1
        game_ball.color('red')
        screen.update()

        # Check if game over
        if scoreboard.lives < 0:
            scoreboard.game_over()
            game_on = False
        else:
            game_ball.reset(BALL_START_CORS)
            scoreboard.update_scoreboard()
            screen.update()
            time.sleep(2)

screen.update()
screen.exitonclick()
