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
    bar.turtlesize(stretch_len=0.5, stretch_wid=40)

    # Add vertical bar for right wall
    bar = turtle.Turtle()
    bar.penup()
    bar.goto(RIGHT_WALL_XCOR, 0)
    bar.shape('square')
    bar.color('white')
    bar.turtlesize(stretch_len=0.5, stretch_wid=40)


def build_level_one():
    """
    Build the columns of blocks
    """
    spacing = 40
    stack = 3
    ycor = 240

    c1 = invaders.Column()
    c1.build(-160, ycor, stack, spacing)
    c2 = invaders.Column()
    c2.build(-100, ycor, stack, spacing)
    c3 = invaders.Column()
    c3.build(-40, ycor, stack, spacing)
    c4 = invaders.Column()
    c4.build(20, ycor, stack, spacing)
    c5 = invaders.Column()
    c5.build(80, ycor, stack, spacing)
    c6 = invaders.Column()
    c6.build(140, ycor, stack, spacing)

    list_of_rows = [c1, c2, c3, c4, c5, c6]
    return list_of_rows
