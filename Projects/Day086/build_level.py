import blocks
import turtle

# Set constants
CEILING_YCOR = 330
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350


def build_screen():
    """
    Adds the on-screen design elements that fill the display
    """
    # # Write instructions on screen
    # instructions = turtle.Turtle()
    # instructions.color('white')
    # instructions.penup()
    # instructions.goto(0, TEXT_YCOR)
    # instructions_text = 'Don\'t let the balloon touch the floor.'
    # instructions.write(instructions_text, align='center', font=('Courier', 12, 'normal'))
    # instructions.goto(0, 1000)

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
    bar.turtlesize(stretch_len=0.5, stretch_wid=33)

    # Add vertical bar for right wall
    bar = turtle.Turtle()
    bar.penup()
    bar.goto(RIGHT_WALL_XCOR, 0)
    bar.shape('square')
    bar.color('white')
    bar.turtlesize(stretch_len=0.5, stretch_wid=33)


def build_level_one():
    """
    Build the rows of blocks
    """
    r1 = blocks.Row()
    r1.build(-395, 240, 16, 60, 'red')
    r2 = blocks.Row()
    r2.build(-395, 210, 16, 60, 'red')
    r3 = blocks.Row()
    r3.build(-395, 180, 16, 60, 'orange')
    r4 = blocks.Row()
    r4.build(-395, 150, 16, 60, 'orange')
    r4.first_orange_hit = True
    r5 = blocks.Row()
    r5.build(-395, 120, 16, 60, 'green')
    r6 = blocks.Row()
    r6.build(-395, 90, 16, 60, 'green')
    r7 = blocks.Row()
    r7.build(-395, 60, 16, 60, 'yellow')
    r8 = blocks.Row()
    r8.build(-395, 30, 16, 60, 'yellow')

    list_of_rows = [r1, r2, r3, r4, r5, r6, r7, r8]
    return list_of_rows
