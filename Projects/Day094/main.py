"""
Day 94: Space Invaders Game
"""
import turtle
import defender
import scoreboard
import mothership
import build_level
import time

ISLAND_OF_MISFIT_TOYS = (-1000, 1000)


# --------------------------------------  Define Simultaneous Key Presses  ----------------------------------------
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

# Create defender and scoreboard
defender_ship = defender.Defender()
game_scoreboard = scoreboard.Scoreboard()

# Add screen elements
build_level.build_screen()
bunker_barrier = build_level.build_bunkers()
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
        defender_ship.fire_laser()

    # Slow down updates with sleep (may need to be adjusted depending on compute power)
    screen.update()
    time.sleep(0.01)
    game_scoreboard.timer += 1

    # Track last color change
    if defender_ship.ship.color()[0] == 'red':
        # Change from red to green if 100 units have passed
        if game_scoreboard.timer - game_scoreboard.time_when_defender_last_hit >= 100:
            defender_ship.change_color('green')

    # Track last invader movement
    for col in invader_columns:
        for invader in col.invaders:
            invader.move()

    # ------------------------------------------  Manage Defender Lasers  --------------------------------------------
    # Recharge and move defender lasers
    defender_ship.laser_recharge -= 1
    for each_laser in defender_ship.lasers:
        each_laser.move()

        # Check if any defender lasers are in the bunker space
        if -250 < each_laser.ycor() < -160:
            # Loop through each block in each bunker
            for bunker in bunker_barrier:
                for block in bunker.blocks:
                    # Check if a block is hit by a defender's laser
                    x_proximity_defender = block.xcor() - each_laser.xcor()
                    y_proximity_defender = block.ycor() - each_laser.ycor()
                    if -7 < y_proximity_defender < 7 and -7 < x_proximity_defender < 7:
                        block.hit()
                        each_laser.goto(ISLAND_OF_MISFIT_TOYS)

    # ----------------------------------------  Manage Invaders' Behavior  --------------------------------------------
    # Loop though each invader in each column
    for col in invader_columns:
        greedo_shot_first = False
        for invader in col.invaders:
            invader.laser.move()

            # First living invader in column recharges and fires their laser
            if invader.alive and not greedo_shot_first:
                invader.laser_recharge -= 1
                invader.fire_laser(game_scoreboard.invaders_hit)

                # Stops remaining invaders in column from firing
                greedo_shot_first = True

            # Check if invader is hit by any of the defender's lasers
            for pew_pew in defender_ship.lasers:
                y_proximity = invader.ycor() - pew_pew.ycor()
                x_proximity = invader.xcor() - pew_pew.xcor()
                if -10 < y_proximity < 10 and -15 < x_proximity < 15 and invader.alive:
                    # Clear old points, show new points earned and reset displayed timer
                    try:
                        plus_points.clear()
                    except NameError:
                        pass
                    plus_points = scoreboard.show_points('white', invader.position())
                    game_scoreboard.time_when_last_points_displayed = game_scoreboard.timer

                    # Update scoreboard
                    game_scoreboard.points += 10
                    game_scoreboard.invaders_hit += 1
                    game_scoreboard.update_scoreboard()

                    # Banish items
                    pew_pew.goto(ISLAND_OF_MISFIT_TOYS)
                    invader.hit()
                    print('Invader hit')

            # Check any invader's laser is near the bunkers (otherwise no need to go through expensive loop)
            if -250 < invader.laser.ycor() < -160:
                # Loop through each block in each bunker
                for bunker in bunker_barrier:
                    for block in bunker.blocks:
                        # Check if a block is hit by an invader's laser
                        x_proximity_laser = block.xcor() - invader.laser.xcor()
                        y_proximity_laser = block.ycor() - invader.laser.ycor()
                        if -7 < y_proximity_laser < 7 and -7 < x_proximity_laser < 7:
                            block.hit()
                            invader.laser.goto(ISLAND_OF_MISFIT_TOYS)

            # Check invader is near the bunkers (otherwise no need to go through expensive loop)
            if -250 < invader.ycor() < -160:
                # Loop through each block in each bunker
                for bunker in bunker_barrier:
                    for block in bunker.blocks:
                        # Check if a block is hit by an invader
                        x_proximity_invader = block.xcor() - invader.xcor()
                        y_proximity_invader = block.ycor() - invader.ycor()
                        if -25 < y_proximity_invader < 25 and -10 < x_proximity_invader < 10:
                            block.hit()

            # Lose life if invader hits defender
            if invader.ycor() <= -250:
                x_prox_invader = defender_ship.blaster.xcor() - invader.xcor()
                y_prox_invader = defender_ship.blaster.ycor() - invader.ycor()
                if -25 < y_prox_invader < 25 and -40 < x_prox_invader < 40:
                    defender_ship.change_color('red')
                    game_scoreboard.lives -= 1

                # Check if an invader has passed the defenses:
                if invader.ycor() <= -370:
                    game_on = False
                    game_scoreboard.game_over()

            # Check if defender is hit by any of the invaders' lasers
            y_prox = defender_ship.ship.ycor() - invader.laser.ycor()
            x_prox = defender_ship.ship.xcor() - invader.laser.xcor()
            if -10 < y_prox < 10 and -30 < x_prox < 30:
                print('Defender hit')
                invader.laser.goto(ISLAND_OF_MISFIT_TOYS)
                defender_ship.change_color('red')
                game_scoreboard.time_when_defender_last_hit = game_scoreboard.timer
                game_scoreboard.lives -= 1

    # ------------------------------------------  Manage the Mothership  ----------------------------------------------
    # Periodically add a mothership
    if game_scoreboard.timer - game_scoreboard.time_when_last_mothership_appeared >= 1200:
        # If mothership exists, move it; otherwise, create mothership
        try:
            the_mothership.goto(500, 320)
            print('A wild Mothership has appeared!')
        except NameError:
            the_mothership = mothership.Mothership()
        game_scoreboard.time_when_last_mothership_appeared = game_scoreboard.timer

    # Perform actions if the mothership exists
    try:
        # Move the mothership
        the_mothership.move()

        # Periodically fire a laser
        if game_scoreboard.timer % 25 == 0:
            the_mothership.fire_laser()

        # Move the mothership's lasers
        for mother_laser in the_mothership.lasers:
            mother_laser.move()

            # Check if a laser hits the defender
            if -380 < mother_laser.ycor() < -320 and -500 < mother_laser.xcor() < 500:
                y_prox = defender_ship.ship.ycor() - mother_laser.ycor()
                x_prox = defender_ship.ship.xcor() - mother_laser.xcor()
                if -10 < y_prox < 10 and -30 < x_prox < 30:
                    print('Defender hit')
                    mother_laser.goto(ISLAND_OF_MISFIT_TOYS)
                    defender_ship.change_color('red')
                    game_scoreboard.time_when_defender_last_hit = game_scoreboard.timer
                    game_scoreboard.lives -= 1

            # Check if a laser hits a bunker block
            if -250 < mother_laser.ycor() < -160 and -450 < mother_laser.xcor() < 450:
                # Loop through each block in each bunker
                for bunker in bunker_barrier:
                    for block in bunker.blocks:
                        y_prox = block.ycor() - mother_laser.ycor()
                        x_prox = block.xcor() - mother_laser.xcor()
                        if -10 < y_prox < 10 and -10 < x_prox < 10:
                            mother_laser.goto(ISLAND_OF_MISFIT_TOYS)
                            block.goto(ISLAND_OF_MISFIT_TOYS)

        # Check if laser hits mother turtle
        for defender_laser in defender_ship.lasers:
            if 260 < defender_laser.ycor() < 340:
                y_prox = the_mothership.ycor() - defender_laser.ycor()
                x_prox = the_mothership.xcor() - defender_laser.xcor()
                if -20 < y_prox < 20 and -40 < x_prox < 40:
                    # Clear old points, show new points earned and reset displayed timer
                    try:
                        plus_points.clear()
                    except NameError:
                        pass
                    plus_points = scoreboard.show_points('yellow', the_mothership.position())
                    game_scoreboard.time_when_last_points_displayed = game_scoreboard.timer

                    # Banish items and update score
                    the_mothership.goto(ISLAND_OF_MISFIT_TOYS)
                    defender_laser.goto(ISLAND_OF_MISFIT_TOYS)
                    game_scoreboard.points += 100
                    game_scoreboard.update_scoreboard()
                    print('Mothership hit')

    # Pass if no mothership
    except NameError:
        pass

    # ------------------------------------------  Manage Game Status  ------------------------------------------------
    # After 50 time units, clear the points text
    try:
        if game_scoreboard.timer - game_scoreboard.time_when_last_points_displayed >= 50:
            plus_points.clear()
    except NameError:
        pass

    # Check if game over
    if game_scoreboard.lives < 0:
        game_on = False
        game_scoreboard.game_over()

    # Check if it's time to update the scoreboard
    elif game_scoreboard.lives_since_last_update != game_scoreboard.lives:
        game_scoreboard.update_scoreboard()
        game_scoreboard.lives_since_last_update = game_scoreboard.lives

    # Check if the game has been won
    elif game_scoreboard.invaders_hit == 30:
        game_scoreboard.game_won()
        break
# ------------------------------------------  End Game Play  ----------------------------------------------------

screen.update()
screen.exitonclick()
