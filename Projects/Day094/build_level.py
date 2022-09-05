import bunkers
import invaders
import turtle

# Set constants
CEILING_YCOR = 390
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350


def build_screen():
    """
    Adds the on-screen design elements that fill the display
    """
    # Write instructions on screen
    instructions = turtle.Turtle()
    instructions.color('white')
    instructions.penup()
    instructions.goto(0, TEXT_YCOR)
    instructions_text = 'It\'s a trap! Press tab to fire laser.'
    instructions.write(instructions_text, align='center', font=('Courier', 14, 'normal'))
    instructions.goto(0, 1000)

    # Write labels on screen
    labels = turtle.Turtle()
    labels.color('white')
    labels.penup()
    labels.goto(-450, TEXT_YCOR)
    label_text = 'POINTS'
    labels.write(label_text, align='center', font=('Courier', 18, 'normal'))
    labels.goto(410, TEXT_YCOR)
    label_text = 'EXTRA LIVES'
    labels.write(label_text, align='center', font=('Courier', 18, 'normal'))
    labels.goto(0, 1000)

    # Add horizontal bar for ceiling
    bar = turtle.Turtle()
    bar.penup()
    bar.goto(0, CEILING_YCOR)
    bar.shape('square')
    bar.color('white')
    bar.turtlesize(stretch_len=50, stretch_wid=0.5)

    # Add vertical bar for left wall
    bar = turtle.Turtle()
    bar.penup()
    bar.goto(LEFT_WALL_XCOR, 0)
    bar.shape('square')
    bar.color('white')
    bar.turtlesize(stretch_len=0.5, stretch_wid=40)

    # Add vertical bar for right wall
    bar = turtle.Turtle()
    bar.penup()
    bar.goto(RIGHT_WALL_XCOR, 0)
    bar.shape('square')
    bar.color('white')
    bar.turtlesize(stretch_len=0.5, stretch_wid=40)


def build_bunkers():
    """
    Builds a barrier of bunkers, each from a model of blocks
    """
    ycor = -170

    b1 = bunkers.Bunker()
    b1.build(-400, ycor)
    b2 = bunkers.Bunker()
    b2.build(-220, ycor)
    b3 = bunkers.Bunker()
    b3.build(-40, ycor)
    b4 = bunkers.Bunker()
    b4.build(140, ycor)
    b5 = bunkers.Bunker()
    b5.build(320, ycor)

    list_of_bunkers = [b1, b2, b3, b4, b5]
    return list_of_bunkers


def build_level_one():
    """
    Build the columns of invaders
    """
    spacing = 40
    stack = 3
    ycor = 160

    c1 = invaders.Column()
    c1.build(-225, ycor, stack, spacing)
    c2 = invaders.Column()
    c2.build(-175, ycor, stack, spacing)
    c3 = invaders.Column()
    c3.build(-125, ycor, stack, spacing)
    c4 = invaders.Column()
    c4.build(-75, ycor, stack, spacing)
    c5 = invaders.Column()
    c5.build(-25, ycor, stack, spacing)
    c6 = invaders.Column()
    c6.build(25, ycor, stack, spacing)
    c7 = invaders.Column()
    c7.build(75, ycor, stack, spacing)
    c8 = invaders.Column()
    c8.build(125, ycor, stack, spacing)
    c9 = invaders.Column()
    c9.build(175, ycor, stack, spacing)
    c10 = invaders.Column()
    c10.build(225, ycor, stack, spacing)
    list_of_columns = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

    return list_of_columns
