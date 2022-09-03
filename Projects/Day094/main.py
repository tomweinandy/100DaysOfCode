"""
Day 94: Space Invaders Game

Using Python Turtle, build the classic shoot 'em up game - space invaders game.
Space Invaders Wikipedia Page
Your space ship can move left and right and it can hit some alien ships. Every second the aliens will move closer to your ship. Once the aliens touch your ship then it's game over. There are usually some barriers between you and the aliens which offers you defensive positions.
You can play the game here:
https://elgoog.im/space-invaders/

"""
import turtle
import defender
import laser
import scoreboard
import build_level
import time

# ------------------------------------------  to do list  ----------------------------------------------------
# todo add shooting function from ball
# todo create a list of laser beams for defender and invader
# todo make invaders shoot
# todo detect if invader or defender hit
# todo lose life if defender hit
# todo pop invader if hit
# todo update score keeper
# todo build bunkers from blocks
# todo break bunkers blocks if hit by laser
# todo make invaders move
# todo add mothership (optional)
# todo remove unused functions
# todo clean up code

# ------------------------------------------  Set Constants  ----------------------------------------------------
BALL_START_ORIENTATION = 135
BALL_START_CORS = (0, -300)
PADDLE_YCOR = -340
CEILING_YCOR = 330
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350
PROXIMITY = 20
ISLAND_OF_MISFIT_TOYS = (1000, 1000)



# ------------------------------------------  Define Helper Functions  ------------------------------------------------
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
    for key in ["Right", "Left", "Tab"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


def block_hit(side):
    """
    Performs checks and actions when a block is hit by the ball
    :param side: The side of the ball that hits a block, e.g., 'right' is the right side of the ball hitting the left
                 side of a block.
    """
    game_ball.bounce(side)
    # print(f'[{side.upper()}] X Distance: {x_distance}, Y Distance: {y_distance}') # Uncomment when debugging

    # Add points according to value of the block
    add_points = invader.popped_points()
    # scoreboard.points += add_points todo add back
    scoreboard.update_scoreboard()

    # # Check if first orange block is popped
    # if add_points == 5:
    #     game_ball.speed_event('orange block')
    #
    # # Check if game is won
    # if scoreboard.points == 512:
    #     scoreboard.game_won()
    #
    #     # Create animation to celebrate the victory
    #     for i in range(40, 3600, 10):
    #         bonus_ball = laser.Laser((0, 0), i)
    #         for j in range(40):
    #             screen.update()
    #             bonus_ball.forward(2 + 0.004*i)
    #     scoreboard.lives += 999


# ------------------------------------------  Create Display and Initialize Key Inputs --------------------------------
# Initialize screen
screen = turtle.Screen()
screen.title('Space Turtles!')
screen.setup(width=1000, height=1000)
screen.bgcolor('black')
screen.tracer(0)  # only updates on screen.update()

# Create ball, defender and scoreboard
defender_ship = defender.Defender()
scoreboard = scoreboard.Scoreboard()

# todo execute on fire
game_ball = laser.Laser('invader', ISLAND_OF_MISFIT_TOYS)
# game_ball = laser.Laser('defender', defender_ship.blaster.position())


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


# ------------------------------------------  Begin Game Play  ----------------------------------------------------
game_on = True
while game_on:
    # Check state of key presses and respond accordingly
    if keys_pressed["Right"]:
        defender_ship.move_right()
    if keys_pressed["Left"]:
        defender_ship.move_left()
    if keys_pressed["Tab"]:
        # # todo execute on fire
        # start = defender_ship.blaster.position()
        # print('Fire laser from', start)
        # laser.Laser('defender', start).fire()
        defender_ship.fire_laser()

    # Slow down updates and add movement to ball
    screen.update()
    time.sleep(0.01 / game_ball.speed)
    # game_ball.fire()

    defender_ship.laser_recharge -= 1

    for each_laser in defender_ship.lasers:
        each_laser.move()

    # ------------------------------------------  Monitor Ball Actions  -----------------------------------------------
    # Detect if ball hits a block
    for row in block_rows:
        for invader in row.invaders:
            x_distance = abs(invader.xcor() - game_ball.xcor())
            y_distance = abs(invader.ycor() - game_ball.ycor())
            block_below_ball = invader.ycor() < game_ball.ycor()
            block_left_of_ball = invader.xcor() < game_ball.xcor()

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
    if game_ball.xcor() < LEFT_WALL_XCOR + PROXIMITY:
        # game_ball.bounce('left')
        pass

    # Detect if the ball hits the right wall
    if game_ball.xcor() > RIGHT_WALL_XCOR - PROXIMITY:
        # game_ball.bounce('right')
        pass

    # Detect if the ball hits the ceiling
    if game_ball.ycor() > CEILING_YCOR - PROXIMITY:
        # game_ball.bounce('top')
        pass

    # Detect if the ball hits the paddle
    if game_ball.distance(defender_ship.position()) < PROXIMITY \
            and game_ball.ycor() < PADDLE_YCOR + PROXIMITY \
            and 180 < game_ball.orientation < 360:

        # Track paddle hits for speed boosts
        game_ball.paddle_hits += 1
        # todo add penalty for getting hit

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
