"""
Snake class
"""
import turtle

# Define constants
STARTING_X = -200
MOVING_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self, x=STARTING_X):
        for i in range(3):
            new_turtle = turtle.Turtle('square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(x, 0)
            x -= 20
            self.segments.append(new_turtle)


    def move(self):
        # Make snake continuously move forward
        # Starting from the end of the snek, move each segment to position of previous segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def turn_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def turn_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def turn_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)


def difficulty():
    screen = turtle.Screen()
    mode = screen.textinput(title='Mode', prompt='Set level of difficulty (easy/normal/hard): ').lower()
    if mode == 'easy':
        pause_length = 0.15
    elif mode == 'hard':
        pause_length = 0.05
    else:
        pause_length = 0.1
    return pause_length