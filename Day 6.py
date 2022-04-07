"""
Day 6: Maze Solver
"""

# Help Reeborg get to the end of a maze
print('Visit https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json')
print('\n The strategy is to gave Reeborg follow the right wall until it leads to the goal.')
print('\nFun fact: this can solve any maze :)')

# Define helper functions
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

# Follow right wall until we reach the end
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_left()

# Note: The above strategy also works to solce the "Hurdle 4" challenge on Reeborg's World