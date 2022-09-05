"""
Day 94: Space Invaders Game

Using Python Turtle, build the classic shoot 'em up game - space invaders game.
Space Invaders Wikipedia Page
Your spaceship can move left and right and it can hit some alien ships. Every second the aliens will move closer to your ship. Once the aliens touch your ship then it's game over. There are usually some barriers between you and the aliens which offers you defensive positions.
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

# Add screen elements
build_level.build_screen()
invader_columns = build_level.build_level_one()

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
        # print('Fire laser from', start)`
        # laser.Laser('defender', start).fire()
        defender_ship.fire_laser()

    # Slow down updates and add movement to ball
    screen.update()
    time.sleep(0.01)

    # Recharge and move defender lasers
    defender_ship.laser_recharge -= 1
    for each_laser in defender_ship.lasers:
        each_laser.move()

    # Loop though each invader in each column
    for col in invader_columns:
        greedo_shot_first = False
        for invader in col.invaders:
            invader.laser.move()

            # First living invader in column recharges and fires their laser
            if invader.alive and not greedo_shot_first:
                invader.laser_recharge -= 1
                invader.fire_laser(scoreboard.invaders_hit)

                # Stops remaining invaders in column from firing
                greedo_shot_first = True

            # Check if invader is hit by any of the defender's lasers
            for pew_pew in defender_ship.lasers:
                y_proximity = invader.ycor() - pew_pew.ycor()
                x_proximity = invader.xcor() - pew_pew.xcor()
                if -10 < y_proximity < 10 and -15 < x_proximity < 15 and invader.alive:
                    pew_pew.goto(ISLAND_OF_MISFIT_TOYS)
                    invader.hit()
                    scoreboard.points += 5
                    scoreboard.invaders_hit += 1
                    scoreboard.update_scoreboard()
                    print('Invader hit')

            # Check if defender is hit by any of the invaders' lasers
            y_prox = defender_ship.ship.ycor() - invader.laser.ycor()
            x_prox = defender_ship.ship.xcor() - invader.laser.xcor()
            if -10 < y_prox < 10 and -30 < x_prox < 30:
                print('Defender hit')
                invader.laser.goto(ISLAND_OF_MISFIT_TOYS)
                defender_ship.change_color('red')
                scoreboard.lives -= 1

    # Check if game over
    if scoreboard.lives < 0:
        scoreboard.game_over()
        game_on = False
    # Check if it's time to update the scoreboard
    elif scoreboard.lives_since_last_update != scoreboard.lives:
        scoreboard.update_scoreboard()
        scoreboard.lives_since_last_update = scoreboard.lives
    # Check if the game has been won
    elif scoreboard.invaders_hit == 24:
        scoreboard.game_won()
        break

    # ------------------------------------------  Monitor Ball Actions  -----------------------------------------------



screen.update()
screen.exitonclick()
