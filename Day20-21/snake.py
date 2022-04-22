"""
Snake class
"""
import turtle

# Define constants
STARTING_POSITIONS = [(-250, 0), (-270, 0), (-290, 0)]
MOVING_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = turtle.Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        # Make snake continuously move forward
        # Starting from the end of the snek, move each segment to position of previous segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)
        # self.segments[0].forward(MOVING_DISTANCE)

    def turn_up(self):
        # if self.segments[0].heading() != DOWN:
        if self.head.heading() != DOWN:
            # self.segments[0].setheading(90)
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != UP:
        # if self.segments[0].heading() != UP:
            self.head.setheading(270)
            # self.segments[0].setheading(270)

    def turn_left(self):
        if self.head.heading() != RIGHT:
        # if self.segments[0].heading() != RIGHT:
            self.head.setheading(180)
            # self.segments[0].setheading(180)

    def turn_right(self):
        if self.head.heading() != LEFT:
        # if self.segments[0].heading() != LEFT:
            self.head.setheading(0)
            # self.segments[0].setheading(0)


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
