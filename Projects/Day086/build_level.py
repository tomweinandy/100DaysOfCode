import blocks
import turtle

# Sets constants
PADDLE_YCOR = -340
CEILING_YCOR = 330
LEFT_WALL_XCOR = -495
RIGHT_WALL_XCOR = 485
TEXT_YCOR = 350


def build_screen():
    # todo move to separate file
    # # Write instructions on screen
    # instructions = turtle.Turtle()
    # instructions.color('white')
    # instructions.penup()
    # instructions.goto(0, TEXT_YCOR)
    # instructions_text = 'Press Backspace to begin.'
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


def build_level_one():
    row = blocks.Row()
    row.build(-395, 240, 16, 60, 'red')
    row.build(-395, 210, 16, 60, 'red')
    row.build(-395, 180, 16, 60, 'orange')
    row.build(-395, 150, 16, 60, 'orange')
    row.build(-395, 120, 16, 60, 'yellow')
    row.build(-395, 90, 16, 60, 'yellow')
    row.build(-395, 60, 16, 60, 'green')
    row.build(-395, 30, 16, 60, 'green')


